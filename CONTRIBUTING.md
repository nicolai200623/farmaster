# 🤝 Contributing to AsterDEX Farm Bot

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🎯 Ways to Contribute

### 1. Report Bugs
- Use GitHub Issues
- Include error messages
- Provide steps to reproduce
- Share logs (remove sensitive data)

### 2. Suggest Features
- Open GitHub Issue with "Feature Request" label
- Describe use case
- Explain expected behavior

### 3. Improve Documentation
- Fix typos
- Add examples
- Clarify confusing sections
- Translate to other languages

### 4. Submit Code
- Bug fixes
- New features
- Performance improvements
- Tests

## 🔧 Development Setup

### 1. Fork & Clone
```bash
# Fork on GitHub first
git clone https://github.com/YOUR_USERNAME/FarmAster.git
cd FarmAster
```

### 2. Create Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### 3. Install Dev Dependencies
```bash
pip install -r requirements.txt
pip install pytest black flake8  # Dev tools
```

### 4. Make Changes
- Follow code style (PEP 8)
- Add comments (Vietnamese OK)
- Update documentation
- Add tests if applicable

### 5. Test
```bash
# Run tests
pytest

# Check code style
black .
flake8 .

# Test bot
python scripts/test_signal.py
python run_backtest.py
```

### 6. Commit
```bash
git add .
git commit -m "feat: add new feature"
# or
git commit -m "fix: resolve issue #123"
```

**Commit Message Format:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `style:` Code style
- `refactor:` Code refactoring
- `test:` Tests
- `chore:` Maintenance

### 7. Push & PR
```bash
git push origin feature/your-feature-name
```

Then create Pull Request on GitHub.

## 📝 Code Style

### Python
- Follow PEP 8
- Use type hints where possible
- Max line length: 100
- Use meaningful variable names

**Good:**
```python
def calculate_position_size(balance: float, price: float, leverage: int) -> float:
    """
    Tính position size dựa trên balance và leverage.
    
    Args:
        balance: Account balance
        price: Current price
        leverage: Leverage multiplier
        
    Returns:
        Position quantity
    """
    capital = balance * Config.SIZE_PCT
    quantity = (capital * leverage) / price
    return quantity
```

**Bad:**
```python
def calc(b, p, l):
    c = b * 0.1
    q = (c * l) / p
    return q
```

### Comments
- Vietnamese OK for inline comments
- English for docstrings
- Explain WHY, not WHAT

**Good:**
```python
# Giảm position size khi volatility cao để giảm risk
if volatility > threshold:
    size *= 0.5
```

**Bad:**
```python
# Set size to size times 0.5
size *= 0.5
```

## 🧪 Testing

### Unit Tests
```python
# tests/test_features.py
import pytest
from ml.features import FeatureEngine

def test_calculate_indicators():
    df = create_sample_df()
    result = FeatureEngine.calculate_indicators(df)
    
    assert 'rsi' in result.columns
    assert result['rsi'].notna().all()
    assert (result['rsi'] >= 0).all()
    assert (result['rsi'] <= 100).all()
```

### Integration Tests
```python
# tests/test_bot.py
def test_signal_generation():
    client = AsterDEXClient(testnet=True)
    signal = signal_gen.generate_signal(client, 'BTCUSDT')
    
    assert signal in ['LONG', 'SHORT', 'HOLD']
```

## 📚 Documentation

### Code Documentation
- Add docstrings to all functions/classes
- Include parameters and return types
- Provide examples

### README Updates
- Update if adding new features
- Add to table of contents
- Include examples

### API Documentation
- Update `docs/API.md` for new APIs
- Include usage examples
- Document parameters

## 🎨 Feature Guidelines

### Before Adding Feature
1. Check if already exists
2. Open issue to discuss
3. Get feedback from maintainers

### Feature Requirements
- Solves real problem
- Well documented
- Tested
- Doesn't break existing functionality
- Configurable (via .env if possible)

### Example: Adding New Indicator

1. **Update features.py:**
```python
# ml/features.py
def calculate_indicators(df):
    # ... existing code ...
    
    # Add Stochastic RSI
    stoch = ta.stochrsi(df['close'])
    df['stoch_k'] = stoch['STOCHRSIk_14_14_3_3']
    df['stoch_d'] = stoch['STOCHRSId_14_14_3_3']
    
    return df

# Update FEATURE_COLUMNS
FEATURE_COLUMNS = [
    # ... existing ...
    'stoch_k',
    'stoch_d'
]
```

2. **Update signal_generator.py:**
```python
# trading/signal_generator.py
def generate_signal(self, client, symbol):
    # ... existing code ...
    
    # Stochastic signal
    stoch_k = df['stoch_k'].iloc[-1]
    if stoch_k < 20:
        score_long += 1
    elif stoch_k > 80:
        score_short += 1
```

3. **Update documentation:**
```markdown
# docs/STRATEGY.md
### 4. Stochastic RSI
- K < 20: Oversold → LONG
- K > 80: Overbought → SHORT
```

4. **Test:**
```bash
python ml/train.py  # Retrain with new features
python run_backtest.py  # Verify performance
```

## 🐛 Bug Fix Guidelines

### Bug Report Should Include
- Description
- Steps to reproduce
- Expected behavior
- Actual behavior
- Logs/screenshots
- Environment (OS, Python version)

### Bug Fix Process
1. Create issue
2. Reproduce bug
3. Write test that fails
4. Fix bug
5. Verify test passes
6. Submit PR

### Example Bug Fix

**Issue:** Bot crashes when API returns empty klines

**Fix:**
```python
# Before
def generate_signal(self, client, symbol):
    klines = client.get_klines(symbol, interval='1m', limit=100)
    df = self._parse_klines(klines)  # Crashes if klines empty
    
# After
def generate_signal(self, client, symbol):
    klines = client.get_klines(symbol, interval='1m', limit=100)
    
    if not klines or len(klines) < 60:
        logger.warning(f"Insufficient klines for {symbol}")
        return 'HOLD'
    
    df = self._parse_klines(klines)
```

## 🔍 Code Review

### What Reviewers Look For
- Code quality
- Test coverage
- Documentation
- Performance
- Security
- Breaking changes

### Responding to Reviews
- Be respectful
- Explain your approach
- Make requested changes
- Ask questions if unclear

## 📋 Pull Request Checklist

Before submitting PR:

- [ ] Code follows style guidelines
- [ ] Comments added (Vietnamese OK)
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] No breaking changes (or documented)
- [ ] Commit messages clear
- [ ] PR description explains changes

## 🏆 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in documentation

## 📞 Questions?

- Open GitHub Issue
- Join Telegram group
- Email maintainers

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing! 🚀**

