# ============================================
# 🎯 SYMBOL-SPECIFIC OPTIMIZER
# Optimize parameters cho từng symbol
# ============================================

import json
import os
from utils.logger import logger

class SymbolOptimizer:
    """
    Quản lý parameters riêng cho từng symbol
    Dựa trên backtest performance
    """
    
    def __init__(self, config_file='config/symbol_params.json'):
        """
        Initialize symbol optimizer
        
        Args:
            config_file: Path to symbol parameters file
        """
        self.config_file = config_file
        self.symbol_params = self._load_params()
        
    def _load_params(self):
        """Load symbol parameters from file"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load symbol params: {e}")
                return {}
        return {}
    
    def _save_params(self):
        """Save symbol parameters to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.symbol_params, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save symbol params: {e}")
    
    def get_symbol_params(self, symbol):
        """
        Get parameters for specific symbol
        
        Args:
            symbol: Trading pair
            
        Returns:
            dict: Symbol-specific parameters
        """
        # Default parameters
        default_params = {
            'enabled': True,
            'lstm_threshold': 0.45,
            'min_confluence_score': 4,
            'tp_pct': 1.0,
            'sl_pct': None,  # No SL by default
            'position_size_multiplier': 1.0,
            'min_volume_ratio': 1.2,
            'use_filters': True,
            'use_trailing_stop': True,
            'trailing_activation_pct': 0.5,
            'trailing_distance_pct': 0.3,
            'notes': 'Default parameters'
        }
        
        # Get symbol-specific params or use default
        symbol_params = self.symbol_params.get(symbol, default_params.copy())
        
        # Merge with defaults (in case new params added)
        for key, value in default_params.items():
            if key not in symbol_params:
                symbol_params[key] = value
        
        return symbol_params
    
    def update_symbol_params(self, symbol, params):
        """
        Update parameters for symbol
        
        Args:
            symbol: Trading pair
            params: Dict of parameters to update
        """
        if symbol not in self.symbol_params:
            self.symbol_params[symbol] = {}
        
        self.symbol_params[symbol].update(params)
        self._save_params()
        logger.info(f"✅ Updated parameters for {symbol}")
    
    def disable_symbol(self, symbol, reason=''):
        """Disable trading for symbol"""
        self.update_symbol_params(symbol, {
            'enabled': False,
            'notes': f'Disabled: {reason}'
        })
    
    def enable_symbol(self, symbol):
        """Enable trading for symbol"""
        self.update_symbol_params(symbol, {
            'enabled': True,
            'notes': 'Enabled'
        })
    
    def get_enabled_symbols(self, symbols):
        """
        Filter enabled symbols
        
        Args:
            symbols: List of symbols
            
        Returns:
            list: Enabled symbols only
        """
        enabled = []
        for symbol in symbols:
            params = self.get_symbol_params(symbol)
            if params.get('enabled', True):
                enabled.append(symbol)
            else:
                logger.info(f"⏭️ Skipping {symbol}: {params.get('notes', 'Disabled')}")
        
        return enabled
    
    def optimize_from_backtest_results(self, backtest_results):
        """
        Auto-optimize parameters based on backtest results
        
        Args:
            backtest_results: Dict of backtest results per symbol
                {
                    'BTCUSDT': {
                        'trades': 10,
                        'win_rate': 0.6,
                        'pnl_pct': 5.0,
                        'avg_win': 1.5,
                        'avg_loss': -0.5
                    },
                    ...
                }
        """
        logger.info("🎯 Optimizing symbol parameters from backtest results...")
        
        for symbol, results in backtest_results.items():
            trades = results.get('trades', 0)
            win_rate = results.get('win_rate', 0)
            pnl_pct = results.get('pnl_pct', 0)
            
            params = self.get_symbol_params(symbol)
            
            # Disable if poor performance
            if trades > 10 and (win_rate < 0.15 or pnl_pct < -5.0):
                self.disable_symbol(symbol, f'Poor performance: WR={win_rate:.1%}, PnL={pnl_pct:.1f}%')
                continue
            
            # Adjust parameters based on performance
            if trades > 10:
                # Good performance: relax thresholds
                if win_rate > 0.3 and pnl_pct > 5.0:
                    params['lstm_threshold'] = max(0.40, params['lstm_threshold'] - 0.02)
                    params['min_confluence_score'] = max(3, params['min_confluence_score'] - 1)
                    params['position_size_multiplier'] = min(1.5, params['position_size_multiplier'] + 0.2)
                    params['notes'] = f'Good performance: WR={win_rate:.1%}, PnL={pnl_pct:.1f}%'
                
                # Poor performance: tighten thresholds
                elif win_rate < 0.2 or pnl_pct < 0:
                    params['lstm_threshold'] = min(0.55, params['lstm_threshold'] + 0.02)
                    params['min_confluence_score'] = min(6, params['min_confluence_score'] + 1)
                    params['position_size_multiplier'] = max(0.5, params['position_size_multiplier'] - 0.2)
                    params['notes'] = f'Poor performance: WR={win_rate:.1%}, PnL={pnl_pct:.1f}%'
                
                # Update
                self.update_symbol_params(symbol, params)
        
        logger.info("✅ Symbol optimization complete!")
    
    def get_optimization_summary(self):
        """Get summary of symbol optimizations"""
        summary = {
            'total_symbols': len(self.symbol_params),
            'enabled': 0,
            'disabled': 0,
            'symbols': {}
        }
        
        for symbol, params in self.symbol_params.items():
            if params.get('enabled', True):
                summary['enabled'] += 1
            else:
                summary['disabled'] += 1
            
            summary['symbols'][symbol] = {
                'enabled': params.get('enabled', True),
                'lstm_threshold': params.get('lstm_threshold', 0.45),
                'min_confluence_score': params.get('min_confluence_score', 4),
                'notes': params.get('notes', '')
            }
        
        return summary


# Pre-configured optimal parameters based on backtest
OPTIMAL_SYMBOL_PARAMS = {
    'LTCUSDT': {
        'enabled': True,
        'lstm_threshold': 0.42,  # Lower threshold (best performer)
        'min_confluence_score': 3,
        'tp_pct': 1.0,
        'position_size_multiplier': 1.3,  # Larger size
        'use_trailing_stop': True,
        'trailing_activation_pct': 0.4,
        'notes': 'Best performer in backtest: 21.47% PnL, 201 trades'
    },
    'AVAXUSDT': {
        'enabled': True,
        'lstm_threshold': 0.45,
        'min_confluence_score': 4,
        'tp_pct': 1.0,
        'position_size_multiplier': 1.0,
        'use_trailing_stop': True,
        'notes': 'Good performer: 0.78% PnL, 91 trades'
    },
    'BTCUSDT': {
        'enabled': True,
        'lstm_threshold': 0.48,  # Higher threshold (fewer but better trades)
        'min_confluence_score': 5,
        'tp_pct': 1.0,
        'position_size_multiplier': 1.2,
        'use_trailing_stop': True,
        'notes': 'Low trade count but stable'
    },
    'ETHUSDT': {
        'enabled': True,
        'lstm_threshold': 0.48,
        'min_confluence_score': 5,
        'tp_pct': 1.0,
        'position_size_multiplier': 1.0,
        'use_trailing_stop': True,
        'notes': 'Low trade count'
    },
    'SOLUSDT': {
        'enabled': True,
        'lstm_threshold': 0.48,
        'min_confluence_score': 5,
        'tp_pct': 1.0,
        'position_size_multiplier': 1.0,
        'use_trailing_stop': True,
        'notes': 'Low trade count'
    },
    'DOTUSDT': {
        'enabled': False,  # Disabled due to poor performance
        'lstm_threshold': 0.50,
        'min_confluence_score': 6,
        'tp_pct': 1.0,
        'position_size_multiplier': 0.5,
        'use_trailing_stop': True,
        'notes': 'Disabled: Poor performance -11.15% PnL in backtest'
    },
    'XRPUSDT': {
        'enabled': True,
        'lstm_threshold': 0.48,
        'min_confluence_score': 5,
        'tp_pct': 1.0,
        'position_size_multiplier': 0.8,
        'use_trailing_stop': True,
        'notes': 'Very low trade count'
    }
}


def initialize_optimal_params(config_file='config/symbol_params.json'):
    """Initialize symbol params with optimal values from backtest"""
    optimizer = SymbolOptimizer(config_file)
    
    for symbol, params in OPTIMAL_SYMBOL_PARAMS.items():
        optimizer.update_symbol_params(symbol, params)
    
    logger.info("✅ Initialized optimal symbol parameters from backtest results")
    return optimizer

