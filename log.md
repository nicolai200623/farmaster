2025-12-04 13:36:23,684 [INFO] 
ðŸ›‘ Shutdown signal received...
2025-12-04 13:37:54,705 [INFO] âœ… Telegram bot initialized
2025-12-04 13:38:04,271 [INFO] ============================================================
2025-12-04 13:38:04,272 [INFO] ðŸš€ ASTERDEX PERP FARM BOT - INITIALIZING
2025-12-04 13:38:04,273 [INFO] ============================================================
2025-12-04 13:38:04,456 [INFO] ðŸ”Œ AsterDEX Client initialized (MAINNET)
2025-12-04 13:38:04,456 [INFO]    URL: https://fapi.asterdex.com/fapi
2025-12-04 13:38:04,457 [INFO] ðŸ“‚ Loaded 3 position timestamps
2025-12-04 13:38:04,457 [INFO] ðŸ“ˆ Trailing Stop enabled (PnL-based): Activation=3.5% PnL, Trail=2.2% PnL
2025-12-04 13:38:04,457 [INFO] ðŸŽ­ Loading Ensemble models...
2025-12-04 13:38:04,488 [INFO] ðŸ§  LSTM Model initialized on cpu
2025-12-04 13:38:04,488 [INFO]    Input: 23, Hidden: 128, Layers: 2, Dropout: 0.35
2025-12-04 13:38:04,488 [INFO] ðŸ’¡ LightGBM Trainer initialized with 23 features
2025-12-04 13:38:04,488 [INFO] ðŸ± CatBoost Trainer initialized with 23 features
2025-12-04 13:38:04,488 [INFO] ðŸŽ­ Ensemble initialized with 4 models
2025-12-04 13:38:04,489 [INFO]    Models: ['lstm', 'xgboost', 'lightgbm', 'catboost']
2025-12-04 13:38:04,489 [INFO]    Weights: [0.15 0.35 0.3  0.2 ]
2025-12-04 13:38:04,514 [INFO] âœ… Model loaded from models/lstm_model.pt (input_size=23)
2025-12-04 13:38:04,514 [INFO] âœ… LSTM loaded
2025-12-04 13:38:04,590 [INFO] âœ… XGBoost model loaded from models/xgboost_model.json
2025-12-04 13:38:04,590 [INFO] âœ… XGBoost loaded
2025-12-04 13:38:04,627 [INFO] âœ… LightGBM loaded from models/lightgbm_model.txt
2025-12-04 13:38:04,627 [INFO] âœ… LightGBM loaded
2025-12-04 13:38:04,641 [INFO] âœ… CatBoost loaded from models/catboost_model.cbm
2025-12-04 13:38:04,641 [INFO] âœ… CatBoost loaded
2025-12-04 13:38:04,641 [INFO] âœ… Ensemble loaded: 4/4 models
2025-12-04 13:38:04,641 [INFO] ðŸŽ­ Using Ensemble predictor: ['lstm', 'xgboost', 'lightgbm', 'catboost']
2025-12-04 13:38:04,642 [INFO]    Weights: [0.15, 0.35, 0.3, 0.2]
2025-12-04 13:38:04,642 [INFO] ðŸŽ¯ SmartEntrySystemV2 enabled (min score: 5, min R:R: 0.0:1)
2025-12-04 13:38:04,642 [INFO] ðŸš« Signal Cooldown enabled: 60m signal, 15m post-trade
2025-12-04 13:38:04,643 [INFO] ðŸŽ¯ Entry Quality Checker enabled
2025-12-04 13:38:04,643 [INFO] âœ… Bot initialized successfully!
2025-12-04 13:38:04,643 [INFO]    Symbols: ['ADAUSDT', 'BNBUSDT', 'DOGEUSDT', 'UNIUSDT', 'LINKUSDT', 'BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'XRPUSDT', 'DOTUSDT', 'AVAXUSDT', 'NEARUSDT']
2025-12-04 13:38:04,643 [INFO]    Leverage: 10x
2025-12-04 13:38:04,643 [INFO]    Position Size: 20.0%
2025-12-04 13:38:04,643 [INFO]    TP/SL: 10.00% / Disabled
2025-12-04 13:38:04,643 [INFO]    Position Timeout: 72.0h
2025-12-04 13:38:04,643 [INFO] ============================================================
2025-12-04 13:38:04,643 [INFO] ðŸ BOT STARTED!
2025-12-04 13:38:05,366 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-12-04 13:38:05,549 [INFO] ðŸ“Š Daily start balance: $39.11
2025-12-04 13:38:05,549 [INFO] ðŸ’° Starting balance: $39.11
2025-12-04 13:38:05,999 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-12-04 13:38:06,001 [INFO] 
============================================================
2025-12-04 13:38:06,002 [INFO] ðŸ”„ LOOP #1 - 2025-12-04 13:38:06
2025-12-04 13:38:06,002 [INFO] ============================================================
2025-12-04 13:38:06,087 [INFO] ðŸ’° Current balance: $39.11
2025-12-04 13:38:06,087 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-04 13:38:06,169 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-04 13:38:06,983 [INFO] ðŸŽ¯ ADAUSDT LONG Signal | Score: 12/15
2025-12-04 13:38:06,983 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:38:06,983 [INFO]    âœ… Perfect pullback to EMA21
2025-12-04 13:38:06,983 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:38:06,983 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:38:06,983 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:38:06,984 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:38:06,984 [INFO]    ðŸš« ML Conviction too low: 0.447
2025-12-04 13:38:06,984 [INFO] ðŸ“¡ ADAUSDT Signal: HOLD (score: 12/15)
2025-12-04 13:38:06,984 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=12
2025-12-04 13:38:06,984 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âœ… Perfect pullback to EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:38:06,984 [INFO]    âšª No signal - HOLD
2025-12-04 13:38:07,485 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-04 13:38:07,571 [INFO]    Current position: LONG 0.11
2025-12-04 13:38:07,571 [INFO]    Entry: $924.70 | Mark: $905.70
2025-12-04 13:38:07,571 [INFO]    PnL: -20.55% ($-2.09)
2025-12-04 13:38:07,571 [INFO]    Age: 11.2h / 72.0h
2025-12-04 13:38:08,072 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-04 13:38:08,156 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-04 13:38:08,852 [INFO] ðŸ“¡ DOGEUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:38:08,853 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:38:08,853 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:38:08,853 [INFO]    âšª No signal - HOLD
2025-12-04 13:38:09,354 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-04 13:38:09,442 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-04 13:38:10,235 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 7/15
2025-12-04 13:38:10,235 [INFO]    âš ï¸ HTF aligned (RANGING), LTF diverging
2025-12-04 13:38:10,235 [INFO]    No clear pullback
2025-12-04 13:38:10,235 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:38:10,236 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:38:10,236 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:38:10,236 [INFO]    ðŸš« ML Conviction too low: 0.490
2025-12-04 13:38:10,236 [INFO] ðŸ“¡ UNIUSDT Signal: HOLD (score: 7/15)
2025-12-04 13:38:10,236 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-12-04 13:38:10,236 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (RANGING), LTF diverging, No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:38:10,237 [INFO]    âšª No signal - HOLD
2025-12-04 13:38:10,737 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-04 13:38:10,825 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-04 13:38:11,549 [INFO] ðŸŽ¯ LINKUSDT LONG Signal | Score: 9/15
2025-12-04 13:38:11,554 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:38:11,554 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:38:11,554 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:38:11,554 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:38:11,554 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:38:11,554 [INFO]    ðŸš« ML Conviction too low: 0.416
2025-12-04 13:38:11,554 [INFO] ðŸ“¡ LINKUSDT Signal: HOLD (score: 9/15)
2025-12-04 13:38:11,555 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-12-04 13:38:11,555 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:38:11,555 [INFO]    âšª No signal - HOLD
2025-12-04 13:38:12,056 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-04 13:38:12,140 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-04 13:38:12,848 [INFO] ðŸŽ¯ BTCUSDT LONG Signal | Score: 10/15
2025-12-04 13:38:12,849 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:38:12,849 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:38:12,849 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:38:12,849 [INFO]    âš¡ RSI acceptable range
2025-12-04 13:38:12,849 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:38:12,849 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:38:12,849 [INFO]    ðŸš« Cooldown active: 25.6m remaining (last: LONG at 13:03)
2025-12-04 13:38:12,849 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 10/15)
2025-12-04 13:38:12,850 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=10
2025-12-04 13:38:12,850 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI acceptable range, ðŸ—½ NY session (high liquidity)
2025-12-04 13:38:12,850 [INFO]    âšª No signal - HOLD
2025-12-04 13:38:13,351 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-04 13:38:13,436 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-04 13:38:14,115 [INFO] ðŸŽ¯ ETHUSDT LONG Signal | Score: 10/15
2025-12-04 13:38:14,115 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:38:14,116 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:38:14,116 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:38:14,116 [INFO]    âš¡ RSI acceptable range
2025-12-04 13:38:14,116 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:38:14,116 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:38:14,116 [INFO]    ðŸš« ML Conviction too low: 0.403
2025-12-04 13:38:14,116 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 10/15)
2025-12-04 13:38:14,116 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=10
2025-12-04 13:38:14,116 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI acceptable range, ðŸ—½ NY session (high liquidity)
2025-12-04 13:38:14,117 [INFO]    âšª No signal - HOLD
2025-12-04 13:38:14,617 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-04 13:38:14,704 [INFO]    Current position: LONG 0.69
2025-12-04 13:38:14,704 [INFO]    Entry: $145.48 | Mark: $142.36
2025-12-04 13:38:14,704 [INFO]    PnL: -21.47% ($-2.16)
2025-12-04 13:38:14,704 [INFO]    Age: 12.0h / 72.0h
2025-12-04 13:38:15,205 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-04 13:38:15,290 [INFO]    Current position: LONG 45.3
2025-12-04 13:38:15,290 [INFO]    Entry: $2.21 | Mark: $2.14
2025-12-04 13:38:15,290 [INFO]    PnL: -32.51% ($-3.25)
2025-12-04 13:38:15,290 [INFO]    Age: 15.6h / 72.0h
2025-12-04 13:38:15,791 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-04 13:38:15,875 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-04 13:38:16,560 [INFO] ðŸ“¡ DOTUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:38:16,570 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:38:16,570 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:38:16,571 [INFO]    âšª No signal - HOLD
2025-12-04 13:38:17,071 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-04 13:38:17,157 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-04 13:38:17,827 [INFO] ðŸŽ¯ AVAXUSDT LONG Signal | Score: 11/15
2025-12-04 13:38:17,827 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:38:17,827 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:38:17,827 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:38:17,827 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:38:17,827 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:38:17,827 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:38:17,827 [INFO]    ðŸš« Cooldown active: 57.9m remaining (last: LONG at 13:36)
2025-12-04 13:38:17,828 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:38:17,828 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:38:17,828 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:38:17,828 [INFO]    âšª No signal - HOLD
2025-12-04 13:38:18,329 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-04 13:38:18,420 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-04 13:38:19,277 [INFO] ðŸ“¡ NEARUSDT Signal: HOLD (score: 6/15)
2025-12-04 13:38:19,277 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=6
2025-12-04 13:38:19,278 [INFO]    ðŸ“ Signal reasons: âš ï¸ 4H & Primary aligned (RANGING), No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:38:19,278 [INFO]    âšª No signal - HOLD
2025-12-04 13:38:19,278 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-04 13:41:19,378 [INFO] 
============================================================
2025-12-04 13:41:19,378 [INFO] ðŸ”„ LOOP #2 - 2025-12-04 13:41:19
2025-12-04 13:41:19,378 [INFO] ============================================================
2025-12-04 13:41:19,466 [INFO] ðŸ’° Current balance: $39.11
2025-12-04 13:41:19,466 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-04 13:41:19,573 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-04 13:41:20,360 [INFO] ðŸŽ¯ ADAUSDT LONG Signal | Score: 12/15
2025-12-04 13:41:20,360 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:41:20,360 [INFO]    âœ… Perfect pullback to EMA21
2025-12-04 13:41:20,360 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:41:20,360 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:41:20,360 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:41:20,360 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:41:20,361 [INFO]    ðŸš« ML Conviction too low: 0.443
2025-12-04 13:41:20,361 [INFO] ðŸ“¡ ADAUSDT Signal: HOLD (score: 12/15)
2025-12-04 13:41:20,361 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=12
2025-12-04 13:41:20,362 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âœ… Perfect pullback to EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:41:20,362 [INFO]    âšª No signal - HOLD
2025-12-04 13:41:20,862 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-04 13:41:20,952 [INFO]    Current position: LONG 0.11
2025-12-04 13:41:20,953 [INFO]    Entry: $924.70 | Mark: $906.65
2025-12-04 13:41:20,953 [INFO]    PnL: -19.52% ($-1.99)
2025-12-04 13:41:20,953 [INFO]    Age: 11.2h / 72.0h
2025-12-04 13:41:21,454 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-04 13:41:21,547 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-04 13:41:22,303 [INFO] ðŸ“¡ DOGEUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:41:22,304 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:41:22,304 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:41:22,304 [INFO]    âšª No signal - HOLD
2025-12-04 13:41:22,805 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-04 13:41:22,899 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-04 13:41:23,592 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 7/15
2025-12-04 13:41:23,593 [INFO]    âš ï¸ HTF aligned (RANGING), LTF diverging
2025-12-04 13:41:23,593 [INFO]    No clear pullback
2025-12-04 13:41:23,593 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:41:23,593 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:41:23,593 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:41:23,593 [INFO]    ðŸš« ML Conviction too low: 0.478
2025-12-04 13:41:23,593 [INFO] ðŸ“¡ UNIUSDT Signal: HOLD (score: 7/15)
2025-12-04 13:41:23,594 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-12-04 13:41:23,594 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (RANGING), LTF diverging, No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:41:23,594 [INFO]    âšª No signal - HOLD
2025-12-04 13:41:24,095 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-04 13:41:24,182 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-04 13:41:24,867 [INFO] ðŸŽ¯ LINKUSDT LONG Signal | Score: 9/15
2025-12-04 13:41:24,868 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:41:24,868 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:41:24,868 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:41:24,868 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:41:24,868 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:41:24,868 [INFO]    ðŸš« ML Conviction too low: 0.403
2025-12-04 13:41:24,868 [INFO] ðŸ“¡ LINKUSDT Signal: HOLD (score: 9/15)
2025-12-04 13:41:24,869 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-12-04 13:41:24,869 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:41:24,869 [INFO]    âšª No signal - HOLD
2025-12-04 13:41:25,370 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-04 13:41:25,458 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-04 13:41:26,171 [INFO] ðŸŽ¯ BTCUSDT LONG Signal | Score: 11/15
2025-12-04 13:41:26,171 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:41:26,171 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:41:26,171 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:41:26,171 [INFO]    ðŸ“Š Above average volume
2025-12-04 13:41:26,171 [INFO]    âš¡ RSI acceptable range
2025-12-04 13:41:26,171 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:41:26,171 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:41:26,172 [INFO]    ðŸš« Cooldown active: 22.3m remaining (last: LONG at 13:03)
2025-12-04 13:41:26,172 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:41:26,172 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:41:26,172 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ“Š Above average volume, âš¡ RSI acceptable range
2025-12-04 13:41:26,172 [INFO]    âšª No signal - HOLD
2025-12-04 13:41:26,673 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-04 13:41:26,760 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-04 13:41:27,540 [INFO] ðŸŽ¯ ETHUSDT LONG Signal | Score: 11/15
2025-12-04 13:41:27,540 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:41:27,540 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:41:27,540 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:41:27,540 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:41:27,540 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:41:27,540 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:41:27,541 [INFO]    ðŸš« Cooldown active: 41.8m remaining (last: LONG at 13:23)
2025-12-04 13:41:27,541 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:41:27,542 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:41:27,542 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:41:27,542 [INFO]    âšª No signal - HOLD
2025-12-04 13:41:28,043 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-04 13:41:28,142 [INFO]    Current position: LONG 0.69
2025-12-04 13:41:28,142 [INFO]    Entry: $145.48 | Mark: $142.78
2025-12-04 13:41:28,142 [INFO]    PnL: -18.59% ($-1.87)
2025-12-04 13:41:28,142 [INFO]    Age: 12.1h / 72.0h
2025-12-04 13:41:28,643 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-04 13:41:28,727 [INFO]    Current position: LONG 45.3
2025-12-04 13:41:28,728 [INFO]    Entry: $2.21 | Mark: $2.14
2025-12-04 13:41:28,728 [INFO]    PnL: -30.24% ($-3.03)
2025-12-04 13:41:28,728 [INFO]    Age: 15.6h / 72.0h
2025-12-04 13:41:29,228 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-04 13:41:29,320 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-04 13:41:30,029 [INFO] ðŸ“¡ DOTUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:41:30,030 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:41:30,030 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:41:30,030 [INFO]    âšª No signal - HOLD
2025-12-04 13:41:30,530 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-04 13:41:30,617 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-04 13:41:31,349 [INFO] ðŸŽ¯ AVAXUSDT LONG Signal | Score: 11/15
2025-12-04 13:41:31,349 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:41:31,349 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:41:31,349 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:41:31,349 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:41:31,349 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:41:31,349 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:41:31,349 [INFO]    ðŸš« Cooldown active: 54.7m remaining (last: LONG at 13:36)
2025-12-04 13:41:31,349 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:41:31,350 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:41:31,350 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:41:31,350 [INFO]    âšª No signal - HOLD
2025-12-04 13:41:31,851 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-04 13:41:31,939 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-04 13:41:32,628 [INFO] ðŸ“¡ NEARUSDT Signal: HOLD (score: 6/15)
2025-12-04 13:41:32,629 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=6
2025-12-04 13:41:32,629 [INFO]    ðŸ“ Signal reasons: âš ï¸ 4H & Primary aligned (RANGING), No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:41:32,629 [INFO]    âšª No signal - HOLD
2025-12-04 13:41:32,629 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-04 13:44:32,728 [INFO] 
============================================================
2025-12-04 13:44:32,728 [INFO] ðŸ”„ LOOP #3 - 2025-12-04 13:44:32
2025-12-04 13:44:32,728 [INFO] ============================================================
2025-12-04 13:44:32,817 [INFO] ðŸ’° Current balance: $39.11
2025-12-04 13:44:32,817 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-04 13:44:32,902 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-04 13:44:33,576 [INFO] ðŸŽ¯ ADAUSDT LONG Signal | Score: 11/15
2025-12-04 13:44:33,577 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:44:33,577 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:44:33,577 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:44:33,577 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:44:33,577 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:44:33,577 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:44:33,577 [INFO]    ðŸš« ML Conviction too low: 0.443
2025-12-04 13:44:33,577 [INFO] ðŸ“¡ ADAUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:44:33,578 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:44:33,578 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:44:33,578 [INFO]    âšª No signal - HOLD
2025-12-04 13:44:34,079 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-04 13:44:34,162 [INFO]    Current position: LONG 0.11
2025-12-04 13:44:34,162 [INFO]    Entry: $924.70 | Mark: $905.65
2025-12-04 13:44:34,163 [INFO]    PnL: -20.60% ($-2.10)
2025-12-04 13:44:34,163 [INFO]    Age: 11.3h / 72.0h
2025-12-04 13:44:34,663 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-04 13:44:34,748 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-04 13:44:35,404 [INFO] ðŸ“¡ DOGEUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:44:35,405 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:44:35,405 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:44:35,406 [INFO]    âšª No signal - HOLD
2025-12-04 13:44:35,906 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-04 13:44:35,993 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-04 13:44:36,661 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 7/15
2025-12-04 13:44:36,661 [INFO]    âš ï¸ HTF aligned (RANGING), LTF diverging
2025-12-04 13:44:36,661 [INFO]    No clear pullback
2025-12-04 13:44:36,661 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:44:36,661 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:44:36,661 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:44:36,661 [INFO]    ðŸš« ML Conviction too low: 0.468
2025-12-04 13:44:36,661 [INFO] ðŸ“¡ UNIUSDT Signal: HOLD (score: 7/15)
2025-12-04 13:44:36,662 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-12-04 13:44:36,662 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (RANGING), LTF diverging, No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:44:36,662 [INFO]    âšª No signal - HOLD
2025-12-04 13:44:37,163 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-04 13:44:37,245 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-04 13:44:37,901 [INFO] ðŸŽ¯ LINKUSDT LONG Signal | Score: 9/15
2025-12-04 13:44:37,901 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:44:37,901 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:44:37,902 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:44:37,902 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:44:37,902 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:44:37,902 [INFO]    ðŸš« ML Conviction too low: 0.402
2025-12-04 13:44:37,902 [INFO] ðŸ“¡ LINKUSDT Signal: HOLD (score: 9/15)
2025-12-04 13:44:37,902 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-12-04 13:44:37,903 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:44:37,903 [INFO]    âšª No signal - HOLD
2025-12-04 13:44:38,403 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-04 13:44:38,496 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-04 13:44:39,134 [INFO] ðŸŽ¯ BTCUSDT LONG Signal | Score: 11/15
2025-12-04 13:44:39,134 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:44:39,134 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:44:39,134 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:44:39,134 [INFO]    ðŸ“Š Above average volume
2025-12-04 13:44:39,135 [INFO]    âš¡ RSI acceptable range
2025-12-04 13:44:39,135 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:44:39,135 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:44:39,135 [INFO]    ðŸš« Cooldown active: 19.1m remaining (last: LONG at 13:03)
2025-12-04 13:44:39,135 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:44:39,136 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:44:39,136 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ“Š Above average volume, âš¡ RSI acceptable range
2025-12-04 13:44:39,136 [INFO]    âšª No signal - HOLD
2025-12-04 13:44:39,637 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-04 13:44:39,719 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-04 13:44:40,441 [INFO] ðŸŽ¯ ETHUSDT LONG Signal | Score: 11/15
2025-12-04 13:44:40,441 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:44:40,441 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:44:40,441 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:44:40,441 [INFO]    ðŸ“Š Above average volume
2025-12-04 13:44:40,441 [INFO]    âš¡ RSI acceptable range
2025-12-04 13:44:40,442 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:44:40,442 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:44:40,442 [INFO]    ðŸš« ML Conviction too low: 0.449
2025-12-04 13:44:40,442 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:44:40,442 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:44:40,443 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ“Š Above average volume, âš¡ RSI acceptable range
2025-12-04 13:44:40,443 [INFO]    âšª No signal - HOLD
2025-12-04 13:44:40,943 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-04 13:44:41,024 [INFO]    Current position: LONG 0.69
2025-12-04 13:44:41,024 [INFO]    Entry: $145.48 | Mark: $142.26
2025-12-04 13:44:41,024 [INFO]    PnL: -22.11% ($-2.22)
2025-12-04 13:44:41,024 [INFO]    Age: 12.1h / 72.0h
2025-12-04 13:44:41,525 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-04 13:44:41,612 [INFO]    Current position: LONG 45.3
2025-12-04 13:44:41,612 [INFO]    Entry: $2.21 | Mark: $2.14
2025-12-04 13:44:41,612 [INFO]    PnL: -32.14% ($-3.22)
2025-12-04 13:44:41,612 [INFO]    Age: 15.7h / 72.0h
2025-12-04 13:44:42,113 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-04 13:44:42,201 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-04 13:44:42,855 [INFO] ðŸ“¡ DOTUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:44:42,856 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:44:42,856 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:44:42,857 [INFO]    âšª No signal - HOLD
2025-12-04 13:44:43,357 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-04 13:44:43,442 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-04 13:44:44,085 [INFO] ðŸŽ¯ AVAXUSDT LONG Signal | Score: 11/15
2025-12-04 13:44:44,085 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:44:44,085 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:44:44,085 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:44:44,085 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:44:44,085 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:44:44,085 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:44:44,086 [INFO]    ðŸš« Cooldown active: 51.5m remaining (last: LONG at 13:36)
2025-12-04 13:44:44,086 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:44:44,086 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:44:44,086 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:44:44,086 [INFO]    âšª No signal - HOLD
2025-12-04 13:44:44,587 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-04 13:44:44,675 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-04 13:44:45,373 [INFO] ðŸ“¡ NEARUSDT Signal: HOLD (score: 8/15)
2025-12-04 13:44:45,374 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=8
2025-12-04 13:44:45,374 [INFO]    ðŸ“ Signal reasons: âš ï¸ 4H & Primary aligned (RANGING), No clear pullback, ðŸ”‘ At swing low (support), ðŸ“ˆ Strong volume spike (2x), ðŸ—½ NY session (high liquidity)
2025-12-04 13:44:45,374 [INFO]    âšª No signal - HOLD
2025-12-04 13:44:45,374 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-04 13:47:45,474 [INFO] 
============================================================
2025-12-04 13:47:45,474 [INFO] ðŸ”„ LOOP #4 - 2025-12-04 13:47:45
2025-12-04 13:47:45,474 [INFO] ============================================================
2025-12-04 13:47:45,559 [INFO] ðŸ’° Current balance: $39.11
2025-12-04 13:47:45,559 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-04 13:47:45,647 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-04 13:47:46,321 [INFO] ðŸŽ¯ ADAUSDT LONG Signal | Score: 11/15
2025-12-04 13:47:46,321 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:47:46,322 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:47:46,322 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:47:46,322 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:47:46,322 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:47:46,322 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:47:46,322 [INFO]    ðŸš« ML Conviction too low: 0.498
2025-12-04 13:47:46,322 [INFO] ðŸ“¡ ADAUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:47:46,323 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:47:46,323 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:47:46,323 [INFO]    âšª No signal - HOLD
2025-12-04 13:47:46,824 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-04 13:47:46,911 [INFO]    Current position: LONG 0.11
2025-12-04 13:47:46,911 [INFO]    Entry: $924.70 | Mark: $903.70
2025-12-04 13:47:46,911 [INFO]    PnL: -22.71% ($-2.31)
2025-12-04 13:47:46,911 [INFO]    Age: 11.3h / 72.0h
2025-12-04 13:47:47,412 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-04 13:47:47,497 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-04 13:47:48,186 [INFO] ðŸ“¡ DOGEUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:47:48,187 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:47:48,187 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:47:48,187 [INFO]    âšª No signal - HOLD
2025-12-04 13:47:48,688 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-04 13:47:48,773 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-04 13:47:49,418 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 9/15
2025-12-04 13:47:49,418 [INFO]    âš ï¸ HTF aligned (RANGING), LTF diverging
2025-12-04 13:47:49,419 [INFO]    No clear pullback
2025-12-04 13:47:49,419 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:47:49,419 [INFO]    ðŸ“ˆ Strong volume spike (2x)
2025-12-04 13:47:49,419 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:47:49,419 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:47:49,419 [INFO]    ðŸš« Cooldown active: 38.6m remaining (last: SHORT at 13:26)
2025-12-04 13:47:49,419 [INFO] ðŸ“¡ UNIUSDT Signal: HOLD (score: 9/15)
2025-12-04 13:47:49,420 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-12-04 13:47:49,420 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (RANGING), LTF diverging, No clear pullback, ðŸ”‘ At swing low (support), ðŸ“ˆ Strong volume spike (2x), ðŸ—½ NY session (high liquidity)
2025-12-04 13:47:49,420 [INFO]    âšª No signal - HOLD
2025-12-04 13:47:49,921 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-04 13:47:50,006 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-04 13:47:50,824 [INFO] ðŸŽ¯ LINKUSDT LONG Signal | Score: 9/15
2025-12-04 13:47:50,826 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:47:50,826 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:47:50,826 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:47:50,826 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:47:50,826 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:47:50,826 [INFO]    ðŸš« ML Conviction too low: 0.429
2025-12-04 13:47:50,826 [INFO] ðŸ“¡ LINKUSDT Signal: HOLD (score: 9/15)
2025-12-04 13:47:50,827 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-12-04 13:47:50,827 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:47:50,827 [INFO]    âšª No signal - HOLD
2025-12-04 13:47:51,328 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-04 13:47:51,410 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-04 13:47:52,124 [INFO] ðŸŽ¯ BTCUSDT LONG Signal | Score: 10/15
2025-12-04 13:47:52,125 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:47:52,125 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:47:52,125 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:47:52,125 [INFO]    âš¡ RSI acceptable range
2025-12-04 13:47:52,125 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:47:52,125 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:47:52,125 [INFO]    ðŸš« Cooldown active: 15.9m remaining (last: LONG at 13:03)
2025-12-04 13:47:52,125 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 10/15)
2025-12-04 13:47:52,126 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=10
2025-12-04 13:47:52,126 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI acceptable range, ðŸ—½ NY session (high liquidity)
2025-12-04 13:47:52,126 [INFO]    âšª No signal - HOLD
2025-12-04 13:47:52,627 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-04 13:47:52,710 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-04 13:47:53,367 [INFO] ðŸŽ¯ ETHUSDT LONG Signal | Score: 11/15
2025-12-04 13:47:53,367 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:47:53,367 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:47:53,367 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:47:53,367 [INFO]    ðŸ“Š Above average volume
2025-12-04 13:47:53,367 [INFO]    âš¡ RSI acceptable range
2025-12-04 13:47:53,367 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:47:53,367 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:47:53,368 [INFO]    ðŸš« ML Conviction too low: 0.468
2025-12-04 13:47:53,368 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:47:53,368 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:47:53,368 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ“Š Above average volume, âš¡ RSI acceptable range
2025-12-04 13:47:53,369 [INFO]    âšª No signal - HOLD
2025-12-04 13:47:53,869 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-04 13:47:53,953 [INFO]    Current position: LONG 0.69
2025-12-04 13:47:53,954 [INFO]    Entry: $145.48 | Mark: $141.94
2025-12-04 13:47:53,954 [INFO]    PnL: -24.33% ($-2.44)
2025-12-04 13:47:53,954 [INFO]    Age: 12.2h / 72.0h
2025-12-04 13:47:54,455 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-04 13:47:54,539 [INFO]    Current position: LONG 45.3
2025-12-04 13:47:54,540 [INFO]    Entry: $2.21 | Mark: $2.13
2025-12-04 13:47:54,540 [INFO]    PnL: -37.17% ($-3.72)
2025-12-04 13:47:54,540 [INFO]    Age: 15.8h / 72.0h
2025-12-04 13:47:55,041 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-04 13:47:55,129 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-04 13:47:55,796 [INFO] ðŸ“¡ DOTUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:47:55,797 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:47:55,797 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:47:55,797 [INFO]    âšª No signal - HOLD
2025-12-04 13:47:56,297 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-04 13:47:56,386 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-04 13:47:57,280 [INFO] ðŸŽ¯ AVAXUSDT LONG Signal | Score: 11/15
2025-12-04 13:47:57,281 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:47:57,281 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:47:57,281 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:47:57,281 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:47:57,281 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:47:57,281 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:47:57,281 [INFO]    ðŸš« Cooldown active: 48.3m remaining (last: LONG at 13:36)
2025-12-04 13:47:57,281 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:47:57,282 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:47:57,282 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:47:57,282 [INFO]    âšª No signal - HOLD
2025-12-04 13:47:57,783 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-04 13:47:57,869 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-04 13:47:58,536 [INFO] ðŸ“¡ NEARUSDT Signal: HOLD (score: 6/15)
2025-12-04 13:47:58,537 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=6
2025-12-04 13:47:58,537 [INFO]    ðŸ“ Signal reasons: âš ï¸ 4H & Primary aligned (RANGING), No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:47:58,537 [INFO]    âšª No signal - HOLD
2025-12-04 13:47:58,537 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-04 13:50:58,633 [INFO] 
============================================================
2025-12-04 13:50:58,634 [INFO] ðŸ”„ LOOP #5 - 2025-12-04 13:50:58
2025-12-04 13:50:58,634 [INFO] ============================================================
2025-12-04 13:50:59,644 [INFO] ðŸ’“ Bot alive - Loop #5 - Active positions: 3
2025-12-04 13:50:59,867 [INFO] ðŸ’° Current balance: $39.11
2025-12-04 13:50:59,867 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-04 13:50:59,952 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-04 13:51:00,618 [INFO] ðŸŽ¯ ADAUSDT LONG Signal | Score: 11/15
2025-12-04 13:51:00,619 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:51:00,619 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:51:00,619 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:51:00,619 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:51:00,619 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:51:00,619 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:51:00,619 [INFO]    ðŸš« ML Conviction too low: 0.455
2025-12-04 13:51:00,619 [INFO] ðŸ“¡ ADAUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:51:00,620 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:51:00,620 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:51:00,620 [INFO]    âšª No signal - HOLD
2025-12-04 13:51:01,121 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-04 13:51:01,208 [INFO]    Current position: LONG 0.11
2025-12-04 13:51:01,208 [INFO]    Entry: $924.70 | Mark: $903.49
2025-12-04 13:51:01,208 [INFO]    PnL: -22.93% ($-2.33)
2025-12-04 13:51:01,209 [INFO]    Age: 11.4h / 72.0h
2025-12-04 13:51:01,709 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-04 13:51:01,791 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-04 13:51:02,436 [INFO] ðŸ“¡ DOGEUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:51:02,437 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:51:02,437 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:51:02,437 [INFO]    âšª No signal - HOLD
2025-12-04 13:51:02,938 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-04 13:51:03,024 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-04 13:51:03,671 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 9/15
2025-12-04 13:51:03,671 [INFO]    âš ï¸ HTF aligned (RANGING), LTF diverging
2025-12-04 13:51:03,671 [INFO]    No clear pullback
2025-12-04 13:51:03,671 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:51:03,671 [INFO]    ðŸ“ˆ Strong volume spike (2x)
2025-12-04 13:51:03,671 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:51:03,671 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:51:03,672 [INFO]    ðŸš« Cooldown active: 35.4m remaining (last: SHORT at 13:26)
2025-12-04 13:51:03,672 [INFO] ðŸ“¡ UNIUSDT Signal: HOLD (score: 9/15)
2025-12-04 13:51:03,672 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-12-04 13:51:03,672 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (RANGING), LTF diverging, No clear pullback, ðŸ”‘ At swing low (support), ðŸ“ˆ Strong volume spike (2x), ðŸ—½ NY session (high liquidity)
2025-12-04 13:51:03,672 [INFO]    âšª No signal - HOLD
2025-12-04 13:51:04,173 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-04 13:51:04,261 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-04 13:51:04,896 [INFO] ðŸŽ¯ LINKUSDT LONG Signal | Score: 9/15
2025-12-04 13:51:04,897 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:51:04,897 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:51:04,897 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:51:04,897 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:51:04,897 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:51:04,897 [INFO]    ðŸš« ML Conviction too low: 0.454
2025-12-04 13:51:04,897 [INFO] ðŸ“¡ LINKUSDT Signal: HOLD (score: 9/15)
2025-12-04 13:51:04,898 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-12-04 13:51:04,898 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:51:04,898 [INFO]    âšª No signal - HOLD
2025-12-04 13:51:05,398 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-04 13:51:05,482 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-04 13:51:06,105 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:51:06,106 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:51:06,106 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:51:06,106 [INFO]    âšª No signal - HOLD
2025-12-04 13:51:06,606 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-04 13:51:06,689 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-04 13:51:07,317 [INFO] ðŸŽ¯ ETHUSDT LONG Signal | Score: 12/15
2025-12-04 13:51:07,317 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:51:07,317 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:51:07,317 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:51:07,317 [INFO]    ðŸ“ˆ Strong volume spike (2x)
2025-12-04 13:51:07,317 [INFO]    âš¡ RSI acceptable range
2025-12-04 13:51:07,317 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:51:07,317 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:51:07,317 [INFO]    ðŸš« ML Conviction too low: 0.491
2025-12-04 13:51:07,317 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 12/15)
2025-12-04 13:51:07,318 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=12
2025-12-04 13:51:07,318 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ“ˆ Strong volume spike (2x), âš¡ RSI acceptable range
2025-12-04 13:51:07,318 [INFO]    âšª No signal - HOLD
2025-12-04 13:51:07,819 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-04 13:51:07,903 [INFO]    Current position: LONG 0.69
2025-12-04 13:51:07,904 [INFO]    Entry: $145.48 | Mark: $141.80
2025-12-04 13:51:07,904 [INFO]    PnL: -25.30% ($-2.54)
2025-12-04 13:51:07,904 [INFO]    Age: 12.3h / 72.0h
2025-12-04 13:51:08,404 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-04 13:51:08,490 [INFO]    Current position: LONG 45.3
2025-12-04 13:51:08,490 [INFO]    Entry: $2.21 | Mark: $2.13
2025-12-04 13:51:08,490 [INFO]    PnL: -36.31% ($-3.63)
2025-12-04 13:51:08,490 [INFO]    Age: 15.8h / 72.0h
2025-12-04 13:51:08,991 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-04 13:51:09,074 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-04 13:51:09,702 [INFO] ðŸ“¡ DOTUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:51:09,703 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:51:09,703 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:51:09,703 [INFO]    âšª No signal - HOLD
2025-12-04 13:51:10,204 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-04 13:51:10,292 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-04 13:51:10,919 [INFO] ðŸŽ¯ AVAXUSDT LONG Signal | Score: 11/15
2025-12-04 13:51:10,920 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:51:10,920 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:51:10,920 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:51:10,920 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:51:10,920 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:51:10,920 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:51:10,920 [INFO]    ðŸš« Cooldown active: 45.1m remaining (last: LONG at 13:36)
2025-12-04 13:51:10,920 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:51:10,921 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:51:10,921 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:51:10,921 [INFO]    âšª No signal - HOLD
2025-12-04 13:51:11,422 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-04 13:51:11,510 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-04 13:51:12,279 [INFO] ðŸ“¡ NEARUSDT Signal: HOLD (score: 6/15)
2025-12-04 13:51:12,280 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=6
2025-12-04 13:51:12,280 [INFO]    ðŸ“ Signal reasons: âš ï¸ 4H & Primary aligned (RANGING), No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:51:12,280 [INFO]    âšª No signal - HOLD
2025-12-04 13:51:12,280 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-04 13:54:12,354 [INFO] 
============================================================
2025-12-04 13:54:12,354 [INFO] ðŸ”„ LOOP #6 - 2025-12-04 13:54:12
2025-12-04 13:54:12,354 [INFO] ============================================================
2025-12-04 13:54:12,438 [INFO] ðŸ’° Current balance: $39.11
2025-12-04 13:54:12,438 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-04 13:54:12,521 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-04 13:54:13,170 [INFO] ðŸŽ¯ ADAUSDT LONG Signal | Score: 11/15
2025-12-04 13:54:13,170 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:54:13,170 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:54:13,170 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:54:13,170 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:54:13,170 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:54:13,170 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:54:13,170 [INFO]    ðŸš« ML Conviction too low: 0.456
2025-12-04 13:54:13,170 [INFO] ðŸ“¡ ADAUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:54:13,171 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:54:13,171 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:54:13,171 [INFO]    âšª No signal - HOLD
2025-12-04 13:54:13,672 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-04 13:54:13,756 [INFO]    Current position: LONG 0.11
2025-12-04 13:54:13,756 [INFO]    Entry: $924.70 | Mark: $903.85
2025-12-04 13:54:13,756 [INFO]    PnL: -22.55% ($-2.29)
2025-12-04 13:54:13,756 [INFO]    Age: 11.4h / 72.0h
2025-12-04 13:54:14,257 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-04 13:54:14,338 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-04 13:54:14,952 [INFO] ðŸ“¡ DOGEUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:54:14,953 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:54:14,953 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:54:14,953 [INFO]    âšª No signal - HOLD
2025-12-04 13:54:15,453 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-04 13:54:15,534 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-04 13:54:16,132 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 9/15
2025-12-04 13:54:16,132 [INFO]    âš ï¸ HTF aligned (RANGING), LTF diverging
2025-12-04 13:54:16,132 [INFO]    No clear pullback
2025-12-04 13:54:16,132 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:54:16,132 [INFO]    ðŸ“ˆ Strong volume spike (2x)
2025-12-04 13:54:16,132 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:54:16,132 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:54:16,133 [INFO]    ðŸš« Cooldown active: 32.2m remaining (last: SHORT at 13:26)
2025-12-04 13:54:16,133 [INFO] ðŸ“¡ UNIUSDT Signal: HOLD (score: 9/15)
2025-12-04 13:54:16,133 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-12-04 13:54:16,133 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (RANGING), LTF diverging, No clear pullback, ðŸ”‘ At swing low (support), ðŸ“ˆ Strong volume spike (2x), ðŸ—½ NY session (high liquidity)
2025-12-04 13:54:16,133 [INFO]    âšª No signal - HOLD
2025-12-04 13:54:16,634 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-04 13:54:16,722 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-04 13:54:17,509 [INFO] ðŸŽ¯ LINKUSDT LONG Signal | Score: 9/15
2025-12-04 13:54:17,509 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:54:17,509 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:54:17,509 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:54:17,509 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:54:17,509 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:54:17,509 [INFO]    ðŸš« ML Conviction too low: 0.454
2025-12-04 13:54:17,509 [INFO] ðŸ“¡ LINKUSDT Signal: HOLD (score: 9/15)
2025-12-04 13:54:17,510 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-12-04 13:54:17,510 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:54:17,510 [INFO]    âšª No signal - HOLD
2025-12-04 13:54:18,011 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-04 13:54:18,098 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-04 13:54:18,757 [INFO] ðŸŽ¯ BTCUSDT LONG Signal | Score: 10/15
2025-12-04 13:54:18,757 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:54:18,757 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:54:18,757 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:54:18,757 [INFO]    âš¡ RSI acceptable range
2025-12-04 13:54:18,757 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:54:18,757 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:54:18,757 [INFO]    ðŸš« Cooldown active: 9.5m remaining (last: LONG at 13:03)
2025-12-04 13:54:18,758 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 10/15)
2025-12-04 13:54:18,758 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=10
2025-12-04 13:54:18,758 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI acceptable range, ðŸ—½ NY session (high liquidity)
2025-12-04 13:54:18,758 [INFO]    âšª No signal - HOLD
2025-12-04 13:54:19,259 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-04 13:54:19,343 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-04 13:54:20,052 [INFO] ðŸŽ¯ ETHUSDT LONG Signal | Score: 12/15
2025-12-04 13:54:20,053 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:54:20,053 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:54:20,053 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:54:20,053 [INFO]    ðŸ“ˆ Strong volume spike (2x)
2025-12-04 13:54:20,053 [INFO]    âš¡ RSI acceptable range
2025-12-04 13:54:20,053 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:54:20,053 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:54:20,053 [INFO]    ðŸš« ML Conviction too low: 0.458
2025-12-04 13:54:20,053 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 12/15)
2025-12-04 13:54:20,054 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=12
2025-12-04 13:54:20,054 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ“ˆ Strong volume spike (2x), âš¡ RSI acceptable range
2025-12-04 13:54:20,054 [INFO]    âšª No signal - HOLD
2025-12-04 13:54:20,555 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-04 13:54:20,637 [INFO]    Current position: LONG 0.69
2025-12-04 13:54:20,637 [INFO]    Entry: $145.48 | Mark: $142.04
2025-12-04 13:54:20,637 [INFO]    PnL: -23.61% ($-2.37)
2025-12-04 13:54:20,637 [INFO]    Age: 12.3h / 72.0h
2025-12-04 13:54:21,138 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-04 13:54:21,224 [INFO]    Current position: LONG 45.3
2025-12-04 13:54:21,224 [INFO]    Entry: $2.21 | Mark: $2.13
2025-12-04 13:54:21,224 [INFO]    PnL: -36.31% ($-3.63)
2025-12-04 13:54:21,224 [INFO]    Age: 15.9h / 72.0h
2025-12-04 13:54:21,725 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-04 13:54:21,808 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-04 13:54:22,434 [INFO] ðŸ“¡ DOTUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:54:22,435 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:54:22,435 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:54:22,435 [INFO]    âšª No signal - HOLD
2025-12-04 13:54:22,936 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-04 13:54:23,021 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-04 13:54:23,658 [INFO] ðŸŽ¯ AVAXUSDT LONG Signal | Score: 11/15
2025-12-04 13:54:23,658 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:54:23,658 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:54:23,658 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:54:23,658 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:54:23,658 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:54:23,658 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:54:23,658 [INFO]    ðŸš« Cooldown active: 41.8m remaining (last: LONG at 13:36)
2025-12-04 13:54:23,658 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:54:23,659 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:54:23,659 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:54:23,659 [INFO]    âšª No signal - HOLD
2025-12-04 13:54:24,160 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-04 13:54:24,243 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-04 13:54:24,879 [INFO] ðŸ“¡ NEARUSDT Signal: HOLD (score: 6/15)
2025-12-04 13:54:24,880 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=6
2025-12-04 13:54:24,880 [INFO]    ðŸ“ Signal reasons: âš ï¸ 4H & Primary aligned (RANGING), No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:54:24,880 [INFO]    âšª No signal - HOLD
2025-12-04 13:54:24,880 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-04 13:57:24,973 [INFO] 
============================================================
2025-12-04 13:57:24,973 [INFO] ðŸ”„ LOOP #7 - 2025-12-04 13:57:24
2025-12-04 13:57:24,973 [INFO] ============================================================
2025-12-04 13:57:25,057 [INFO] ðŸ’° Current balance: $39.11
2025-12-04 13:57:25,058 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-04 13:57:25,146 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-04 13:57:25,856 [INFO] ðŸŽ¯ ADAUSDT LONG Signal | Score: 11/15
2025-12-04 13:57:25,857 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:57:25,857 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:57:25,857 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:57:25,857 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:57:25,857 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:57:25,857 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:57:25,857 [INFO]    ðŸš« ML Conviction too low: 0.506
2025-12-04 13:57:25,857 [INFO] ðŸ“¡ ADAUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:57:25,858 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:57:25,858 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:57:25,858 [INFO]    âšª No signal - HOLD
2025-12-04 13:57:26,359 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-04 13:57:26,450 [INFO]    Current position: LONG 0.11
2025-12-04 13:57:26,450 [INFO]    Entry: $924.70 | Mark: $904.05
2025-12-04 13:57:26,450 [INFO]    PnL: -22.33% ($-2.27)
2025-12-04 13:57:26,450 [INFO]    Age: 11.5h / 72.0h
2025-12-04 13:57:26,951 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-04 13:57:27,034 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-04 13:57:27,749 [INFO] ðŸ“¡ DOGEUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:57:27,750 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:57:27,751 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:57:27,751 [INFO]    âšª No signal - HOLD
2025-12-04 13:57:28,252 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-04 13:57:28,334 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-04 13:57:29,015 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 9/15
2025-12-04 13:57:29,015 [INFO]    âš ï¸ HTF aligned (RANGING), LTF diverging
2025-12-04 13:57:29,015 [INFO]    No clear pullback
2025-12-04 13:57:29,015 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:57:29,015 [INFO]    ðŸ“ˆ Strong volume spike (2x)
2025-12-04 13:57:29,015 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:57:29,015 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:57:29,015 [INFO]    ðŸš« Cooldown active: 28.9m remaining (last: SHORT at 13:26)
2025-12-04 13:57:29,015 [INFO] ðŸ“¡ UNIUSDT Signal: HOLD (score: 9/15)
2025-12-04 13:57:29,016 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-12-04 13:57:29,016 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (RANGING), LTF diverging, No clear pullback, ðŸ”‘ At swing low (support), ðŸ“ˆ Strong volume spike (2x), ðŸ—½ NY session (high liquidity)
2025-12-04 13:57:29,016 [INFO]    âšª No signal - HOLD
2025-12-04 13:57:29,517 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-04 13:57:29,601 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-04 13:57:30,334 [INFO] ðŸŽ¯ LINKUSDT LONG Signal | Score: 9/15
2025-12-04 13:57:30,335 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:57:30,335 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:57:30,335 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:57:30,335 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:57:30,335 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:57:30,335 [INFO]    ðŸš« ML Conviction too low: 0.454
2025-12-04 13:57:30,335 [INFO] ðŸ“¡ LINKUSDT Signal: HOLD (score: 9/15)
2025-12-04 13:57:30,336 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-12-04 13:57:30,336 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:57:30,336 [INFO]    âšª No signal - HOLD
2025-12-04 13:57:30,837 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-04 13:57:30,926 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-04 13:57:31,668 [INFO] ðŸŽ¯ BTCUSDT LONG Signal | Score: 11/15
2025-12-04 13:57:31,669 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:57:31,669 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:57:31,669 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:57:31,669 [INFO]    ðŸ“Š Above average volume
2025-12-04 13:57:31,669 [INFO]    âš¡ RSI acceptable range
2025-12-04 13:57:31,669 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:57:31,669 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:57:31,669 [INFO]    ðŸš« Cooldown active: 6.2m remaining (last: LONG at 13:03)
2025-12-04 13:57:31,669 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:57:31,670 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:57:31,670 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ“Š Above average volume, âš¡ RSI acceptable range
2025-12-04 13:57:31,670 [INFO]    âšª No signal - HOLD
2025-12-04 13:57:32,171 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-04 13:57:32,256 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-04 13:57:33,082 [INFO] ðŸŽ¯ ETHUSDT LONG Signal | Score: 12/15
2025-12-04 13:57:33,082 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:57:33,082 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:57:33,082 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:57:33,082 [INFO]    ðŸ“ˆ Strong volume spike (2x)
2025-12-04 13:57:33,082 [INFO]    âš¡ RSI acceptable range
2025-12-04 13:57:33,082 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:57:33,082 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:57:33,083 [INFO]    ðŸš« ML Conviction too low: 0.476
2025-12-04 13:57:33,083 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 12/15)
2025-12-04 13:57:33,083 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=12
2025-12-04 13:57:33,084 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ“ˆ Strong volume spike (2x), âš¡ RSI acceptable range
2025-12-04 13:57:33,084 [INFO]    âšª No signal - HOLD
2025-12-04 13:57:33,584 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-04 13:57:33,669 [INFO]    Current position: LONG 0.69
2025-12-04 13:57:33,670 [INFO]    Entry: $145.48 | Mark: $142.25
2025-12-04 13:57:33,670 [INFO]    PnL: -22.24% ($-2.23)
2025-12-04 13:57:33,670 [INFO]    Age: 12.4h / 72.0h
2025-12-04 13:57:34,171 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-04 13:57:34,256 [INFO]    Current position: LONG 45.3
2025-12-04 13:57:34,257 [INFO]    Entry: $2.21 | Mark: $2.13
2025-12-04 13:57:34,257 [INFO]    PnL: -36.67% ($-3.67)
2025-12-04 13:57:34,257 [INFO]    Age: 15.9h / 72.0h
2025-12-04 13:57:34,758 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-04 13:57:34,843 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-04 13:57:35,518 [INFO] ðŸ“¡ DOTUSDT Signal: HOLD (score: 0/15)
2025-12-04 13:57:35,519 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 13:57:35,519 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 13:57:35,519 [INFO]    âšª No signal - HOLD
2025-12-04 13:57:36,020 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-04 13:57:36,105 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-04 13:57:36,780 [INFO] ðŸŽ¯ AVAXUSDT LONG Signal | Score: 11/15
2025-12-04 13:57:36,781 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 13:57:36,781 [INFO]    âš ï¸ Near EMA21
2025-12-04 13:57:36,781 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 13:57:36,781 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 13:57:36,781 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 13:57:36,781 [INFO]    âœ… R:R = 2.0:1
2025-12-04 13:57:36,781 [INFO]    ðŸš« Cooldown active: 38.6m remaining (last: LONG at 13:36)
2025-12-04 13:57:36,781 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 11/15)
2025-12-04 13:57:36,782 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 13:57:36,782 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 13:57:36,783 [INFO]    âšª No signal - HOLD
2025-12-04 13:57:37,283 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-04 13:57:37,368 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-04 13:57:38,040 [INFO] ðŸ“¡ NEARUSDT Signal: HOLD (score: 6/15)
2025-12-04 13:57:38,041 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=6
2025-12-04 13:57:38,041 [INFO]    ðŸ“ Signal reasons: âš ï¸ 4H & Primary aligned (RANGING), No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 13:57:38,041 [INFO]    âšª No signal - HOLD
2025-12-04 13:57:38,041 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-04 14:00:38,133 [INFO] 
============================================================
2025-12-04 14:00:38,134 [INFO] ðŸ”„ LOOP #8 - 2025-12-04 14:00:38
2025-12-04 14:00:38,134 [INFO] ============================================================
2025-12-04 14:00:38,221 [INFO] ðŸ’° Current balance: $39.11
2025-12-04 14:00:38,222 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-04 14:00:38,306 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-04 14:00:38,958 [INFO] ðŸŽ¯ ADAUSDT LONG Signal | Score: 11/15
2025-12-04 14:00:38,958 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:00:38,958 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:00:38,959 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:00:38,959 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:00:38,959 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:00:38,959 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:00:38,959 [INFO]    ðŸš« ML Conviction too low: 0.456
2025-12-04 14:00:38,959 [INFO] ðŸ“¡ ADAUSDT Signal: HOLD (score: 11/15)
2025-12-04 14:00:38,959 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 14:00:38,960 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 14:00:38,960 [INFO]    âšª No signal - HOLD
2025-12-04 14:00:39,460 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-04 14:00:39,557 [INFO]    Current position: LONG 0.11
2025-12-04 14:00:39,557 [INFO]    Entry: $924.70 | Mark: $903.51
2025-12-04 14:00:39,558 [INFO]    PnL: -22.91% ($-2.33)
2025-12-04 14:00:39,558 [INFO]    Age: 11.5h / 72.0h
2025-12-04 14:00:40,058 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-04 14:00:40,142 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-04 14:00:40,806 [INFO] ðŸ“¡ DOGEUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:00:40,807 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:00:40,807 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:00:40,807 [INFO]    âšª No signal - HOLD
2025-12-04 14:00:41,308 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-04 14:00:41,392 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-04 14:00:42,045 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 7/15
2025-12-04 14:00:42,045 [INFO]    âš ï¸ HTF aligned (RANGING), LTF diverging
2025-12-04 14:00:42,045 [INFO]    No clear pullback
2025-12-04 14:00:42,045 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:00:42,045 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:00:42,046 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:00:42,046 [INFO]    ðŸš« Cooldown active: 25.7m remaining (last: SHORT at 13:26)
2025-12-04 14:00:42,046 [INFO] ðŸ“¡ UNIUSDT Signal: HOLD (score: 7/15)
2025-12-04 14:00:42,046 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-12-04 14:00:42,047 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (RANGING), LTF diverging, No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 14:00:42,047 [INFO]    âšª No signal - HOLD
2025-12-04 14:00:42,547 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-04 14:00:42,636 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-04 14:00:43,333 [INFO] ðŸŽ¯ LINKUSDT LONG Signal | Score: 9/15
2025-12-04 14:00:43,333 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:00:43,333 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:00:43,333 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:00:43,333 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:00:43,333 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:00:43,333 [INFO]    ðŸš« ML Conviction too low: 0.494
2025-12-04 14:00:43,334 [INFO] ðŸ“¡ LINKUSDT Signal: HOLD (score: 9/15)
2025-12-04 14:00:43,334 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-12-04 14:00:43,334 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 14:00:43,335 [INFO]    âšª No signal - HOLD
2025-12-04 14:00:43,835 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-04 14:00:43,922 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-04 14:00:44,624 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:00:44,625 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:00:44,625 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:00:44,626 [INFO]    âšª No signal - HOLD
2025-12-04 14:00:45,126 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-04 14:00:45,214 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-04 14:00:45,964 [INFO] ðŸŽ¯ ETHUSDT LONG Signal | Score: 10/15
2025-12-04 14:00:45,965 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:00:45,965 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:00:45,965 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:00:45,965 [INFO]    âš¡ RSI acceptable range
2025-12-04 14:00:45,965 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:00:45,965 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:00:45,965 [INFO]    ðŸš« ML Conviction too low: 0.479
2025-12-04 14:00:45,965 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 10/15)
2025-12-04 14:00:45,966 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=10
2025-12-04 14:00:45,966 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI acceptable range, ðŸ—½ NY session (high liquidity)
2025-12-04 14:00:45,966 [INFO]    âšª No signal - HOLD
2025-12-04 14:00:46,467 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-04 14:00:46,551 [INFO]    Current position: LONG 0.69
2025-12-04 14:00:46,551 [INFO]    Entry: $145.48 | Mark: $142.22
2025-12-04 14:00:46,551 [INFO]    PnL: -22.37% ($-2.25)
2025-12-04 14:00:46,551 [INFO]    Age: 12.4h / 72.0h
2025-12-04 14:00:47,052 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-04 14:00:47,277 [INFO]    Current position: LONG 45.3
2025-12-04 14:00:47,277 [INFO]    Entry: $2.21 | Mark: $2.13
2025-12-04 14:00:47,277 [INFO]    PnL: -37.03% ($-3.71)
2025-12-04 14:00:47,277 [INFO]    Age: 16.0h / 72.0h
2025-12-04 14:00:47,778 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-04 14:00:47,863 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-04 14:00:48,571 [INFO] ðŸ“¡ DOTUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:00:48,572 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:00:48,573 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:00:48,573 [INFO]    âšª No signal - HOLD
2025-12-04 14:00:49,074 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-04 14:00:49,163 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-04 14:00:49,993 [INFO] ðŸŽ¯ AVAXUSDT LONG Signal | Score: 11/15
2025-12-04 14:00:49,993 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:00:49,993 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:00:49,993 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:00:49,993 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:00:49,993 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:00:49,993 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:00:49,994 [INFO]    ðŸš« ML Conviction too low: 0.412
2025-12-04 14:00:49,994 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 11/15)
2025-12-04 14:00:49,994 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 14:00:49,994 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 14:00:49,994 [INFO]    âšª No signal - HOLD
2025-12-04 14:00:50,495 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-04 14:00:50,580 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-04 14:00:51,301 [INFO] ðŸ“¡ NEARUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:00:51,302 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:00:51,302 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:00:51,303 [INFO]    âšª No signal - HOLD
2025-12-04 14:00:51,303 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-04 14:03:51,381 [INFO] 
============================================================
2025-12-04 14:03:51,382 [INFO] ðŸ”„ LOOP #9 - 2025-12-04 14:03:51
2025-12-04 14:03:51,382 [INFO] ============================================================
2025-12-04 14:03:51,471 [INFO] ðŸ’° Current balance: $39.11
2025-12-04 14:03:51,471 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-04 14:03:51,552 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-04 14:03:52,206 [INFO] ðŸŽ¯ ADAUSDT LONG Signal | Score: 11/15
2025-12-04 14:03:52,206 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:03:52,206 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:03:52,206 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:03:52,206 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:03:52,206 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:03:52,206 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:03:52,206 [INFO]    ðŸš« ML Conviction too low: 0.453
2025-12-04 14:03:52,206 [INFO] ðŸ“¡ ADAUSDT Signal: HOLD (score: 11/15)
2025-12-04 14:03:52,207 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 14:03:52,207 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 14:03:52,207 [INFO]    âšª No signal - HOLD
2025-12-04 14:03:52,708 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-04 14:03:52,792 [INFO]    Current position: LONG 0.11
2025-12-04 14:03:52,793 [INFO]    Entry: $924.70 | Mark: $904.81
2025-12-04 14:03:52,793 [INFO]    PnL: -21.51% ($-2.19)
2025-12-04 14:03:52,793 [INFO]    Age: 11.6h / 72.0h
2025-12-04 14:03:53,293 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-04 14:03:53,375 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-04 14:03:54,041 [INFO] ðŸ“¡ DOGEUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:03:54,044 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:03:54,045 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:03:54,045 [INFO]    âšª No signal - HOLD
2025-12-04 14:03:54,545 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-04 14:03:54,625 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-04 14:03:55,277 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 7/15
2025-12-04 14:03:55,277 [INFO]    âš ï¸ HTF aligned (RANGING), LTF diverging
2025-12-04 14:03:55,277 [INFO]    No clear pullback
2025-12-04 14:03:55,277 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:03:55,277 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:03:55,277 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:03:55,277 [INFO]    ðŸš« Cooldown active: 22.5m remaining (last: SHORT at 13:26)
2025-12-04 14:03:55,277 [INFO] ðŸ“¡ UNIUSDT Signal: HOLD (score: 7/15)
2025-12-04 14:03:55,278 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-12-04 14:03:55,278 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (RANGING), LTF diverging, No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 14:03:55,278 [INFO]    âšª No signal - HOLD
2025-12-04 14:03:55,779 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-04 14:03:55,865 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-04 14:03:56,674 [INFO] ðŸŽ¯ LINKUSDT LONG Signal | Score: 9/15
2025-12-04 14:03:56,675 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:03:56,675 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:03:56,675 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:03:56,675 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:03:56,675 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:03:56,675 [INFO]    ðŸš« ML Conviction too low: 0.494
2025-12-04 14:03:56,675 [INFO] ðŸ“¡ LINKUSDT Signal: HOLD (score: 9/15)
2025-12-04 14:03:56,676 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-12-04 14:03:56,677 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 14:03:56,677 [INFO]    âšª No signal - HOLD
2025-12-04 14:03:57,177 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-04 14:03:57,265 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-04 14:03:57,934 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:03:57,935 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:03:57,935 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:03:57,935 [INFO]    âšª No signal - HOLD
2025-12-04 14:03:58,436 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-04 14:03:58,522 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-04 14:03:59,317 [INFO] ðŸŽ¯ ETHUSDT LONG Signal | Score: 10/15
2025-12-04 14:03:59,318 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:03:59,318 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:03:59,318 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:03:59,318 [INFO]    âš¡ RSI acceptable range
2025-12-04 14:03:59,318 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:03:59,318 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:03:59,318 [INFO]    ðŸš« ML Conviction too low: 0.485
2025-12-04 14:03:59,319 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 10/15)
2025-12-04 14:03:59,319 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=10
2025-12-04 14:03:59,319 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI acceptable range, ðŸ—½ NY session (high liquidity)
2025-12-04 14:03:59,320 [INFO]    âšª No signal - HOLD
2025-12-04 14:03:59,820 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-04 14:03:59,904 [INFO]    Current position: LONG 0.69
2025-12-04 14:03:59,904 [INFO]    Entry: $145.48 | Mark: $142.34
2025-12-04 14:03:59,904 [INFO]    PnL: -21.59% ($-2.17)
2025-12-04 14:03:59,904 [INFO]    Age: 12.5h / 72.0h
2025-12-04 14:04:00,405 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-04 14:04:00,494 [INFO]    Current position: LONG 45.3
2025-12-04 14:04:00,494 [INFO]    Entry: $2.21 | Mark: $2.13
2025-12-04 14:04:00,494 [INFO]    PnL: -35.95% ($-3.60)
2025-12-04 14:04:00,494 [INFO]    Age: 16.0h / 72.0h
2025-12-04 14:04:00,995 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-04 14:04:01,078 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-04 14:04:01,845 [INFO] ðŸ“¡ DOTUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:04:01,846 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:04:01,846 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:04:01,846 [INFO]    âšª No signal - HOLD
2025-12-04 14:04:02,347 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-04 14:04:02,435 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-04 14:04:03,141 [INFO] ðŸŽ¯ AVAXUSDT LONG Signal | Score: 11/15
2025-12-04 14:04:03,141 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:04:03,141 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:04:03,141 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:04:03,142 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:04:03,142 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:04:03,142 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:04:03,142 [INFO]    ðŸš« ML Conviction too low: 0.425
2025-12-04 14:04:03,142 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 11/15)
2025-12-04 14:04:03,143 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 14:04:03,143 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 14:04:03,143 [INFO]    âšª No signal - HOLD
2025-12-04 14:04:03,644 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-04 14:04:03,729 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-04 14:04:04,400 [INFO] ðŸ“¡ NEARUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:04:04,400 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:04:04,401 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:04:04,401 [INFO]    âšª No signal - HOLD
2025-12-04 14:04:04,401 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-04 14:07:04,501 [INFO] 
============================================================
2025-12-04 14:07:04,502 [INFO] ðŸ”„ LOOP #10 - 2025-12-04 14:07:04
2025-12-04 14:07:04,502 [INFO] ============================================================
2025-12-04 14:07:05,519 [INFO] ðŸ’“ Bot alive - Loop #10 - Active positions: 3
2025-12-04 14:07:05,606 [INFO] ðŸ’° Current balance: $39.11
2025-12-04 14:07:05,606 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-04 14:07:05,690 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-04 14:07:06,447 [INFO] ðŸŽ¯ ADAUSDT LONG Signal | Score: 11/15
2025-12-04 14:07:06,447 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:07:06,447 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:07:06,447 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:07:06,447 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:07:06,447 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:07:06,447 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:07:06,447 [INFO]    ðŸš« ML Conviction too low: 0.454
2025-12-04 14:07:06,447 [INFO] ðŸ“¡ ADAUSDT Signal: HOLD (score: 11/15)
2025-12-04 14:07:06,448 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 14:07:06,448 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 14:07:06,449 [INFO]    âšª No signal - HOLD
2025-12-04 14:07:06,949 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-04 14:07:07,035 [INFO]    Current position: LONG 0.11
2025-12-04 14:07:07,036 [INFO]    Entry: $924.70 | Mark: $905.94
2025-12-04 14:07:07,036 [INFO]    PnL: -20.29% ($-2.06)
2025-12-04 14:07:07,036 [INFO]    Age: 11.7h / 72.0h
2025-12-04 14:07:07,537 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-04 14:07:07,620 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-04 14:07:08,547 [INFO] ðŸ“¡ DOGEUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:07:08,548 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:07:08,548 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:07:08,548 [INFO]    âšª No signal - HOLD
2025-12-04 14:07:09,049 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-04 14:07:09,132 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-04 14:07:09,815 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 7/15
2025-12-04 14:07:09,816 [INFO]    âš ï¸ HTF aligned (RANGING), LTF diverging
2025-12-04 14:07:09,816 [INFO]    No clear pullback
2025-12-04 14:07:09,816 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:07:09,816 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:07:09,816 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:07:09,816 [INFO]    ðŸš« ML Conviction too low: 0.455
2025-12-04 14:07:09,816 [INFO] ðŸ“¡ UNIUSDT Signal: HOLD (score: 7/15)
2025-12-04 14:07:09,817 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-12-04 14:07:09,817 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (RANGING), LTF diverging, No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 14:07:09,817 [INFO]    âšª No signal - HOLD
2025-12-04 14:07:10,318 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-04 14:07:10,407 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-04 14:07:11,119 [INFO] ðŸŽ¯ LINKUSDT LONG Signal | Score: 9/15
2025-12-04 14:07:11,120 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:07:11,120 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:07:11,120 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:07:11,120 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:07:11,120 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:07:11,120 [INFO]    ðŸš« ML Conviction too low: 0.494
2025-12-04 14:07:11,120 [INFO] ðŸ“¡ LINKUSDT Signal: HOLD (score: 9/15)
2025-12-04 14:07:11,121 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-12-04 14:07:11,121 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 14:07:11,121 [INFO]    âšª No signal - HOLD
2025-12-04 14:07:11,622 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-04 14:07:11,706 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-04 14:07:12,387 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:07:12,388 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:07:12,388 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:07:12,388 [INFO]    âšª No signal - HOLD
2025-12-04 14:07:12,889 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-04 14:07:12,975 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-04 14:07:13,659 [INFO] ðŸŽ¯ ETHUSDT LONG Signal | Score: 10/15
2025-12-04 14:07:13,659 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:07:13,659 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:07:13,659 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:07:13,659 [INFO]    âš¡ RSI acceptable range
2025-12-04 14:07:13,659 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:07:13,659 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:07:13,659 [INFO]    ðŸš« ML Conviction too low: 0.503
2025-12-04 14:07:13,659 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 10/15)
2025-12-04 14:07:13,660 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=10
2025-12-04 14:07:13,660 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI acceptable range, ðŸ—½ NY session (high liquidity)
2025-12-04 14:07:13,660 [INFO]    âšª No signal - HOLD
2025-12-04 14:07:14,161 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-04 14:07:14,246 [INFO]    Current position: LONG 0.69
2025-12-04 14:07:14,246 [INFO]    Entry: $145.48 | Mark: $142.24
2025-12-04 14:07:14,246 [INFO]    PnL: -22.25% ($-2.23)
2025-12-04 14:07:14,246 [INFO]    Age: 12.5h / 72.0h
2025-12-04 14:07:14,747 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-04 14:07:14,829 [INFO]    Current position: LONG 45.3
2025-12-04 14:07:14,829 [INFO]    Entry: $2.21 | Mark: $2.13
2025-12-04 14:07:14,829 [INFO]    PnL: -35.31% ($-3.53)
2025-12-04 14:07:14,829 [INFO]    Age: 16.1h / 72.0h
2025-12-04 14:07:15,330 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-04 14:07:15,422 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-04 14:07:16,084 [INFO] ðŸ“¡ DOTUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:07:16,085 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:07:16,085 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:07:16,086 [INFO]    âšª No signal - HOLD
2025-12-04 14:07:16,586 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-04 14:07:16,670 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-04 14:07:17,346 [INFO] ðŸŽ¯ AVAXUSDT LONG Signal | Score: 11/15
2025-12-04 14:07:17,346 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:07:17,346 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:07:17,346 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:07:17,347 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:07:17,347 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:07:17,347 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:07:17,347 [INFO]    ðŸš« ML Conviction too low: 0.440
2025-12-04 14:07:17,347 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 11/15)
2025-12-04 14:07:17,347 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 14:07:17,348 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 14:07:17,348 [INFO]    âšª No signal - HOLD
2025-12-04 14:07:17,849 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-04 14:07:17,931 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-04 14:07:18,630 [INFO] ðŸ“¡ NEARUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:07:18,631 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:07:18,631 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:07:18,631 [INFO]    âšª No signal - HOLD
2025-12-04 14:07:20,482 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-04 14:10:20,582 [INFO] 
============================================================
2025-12-04 14:10:20,582 [INFO] ðŸ”„ LOOP #11 - 2025-12-04 14:10:20
2025-12-04 14:10:20,582 [INFO] ============================================================
2025-12-04 14:10:20,667 [INFO] ðŸ’° Current balance: $39.11
2025-12-04 14:10:20,668 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-04 14:10:20,753 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-04 14:10:21,400 [INFO] ðŸŽ¯ ADAUSDT LONG Signal | Score: 11/15
2025-12-04 14:10:21,400 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:10:21,401 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:10:21,401 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:10:21,401 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:10:21,401 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:10:21,401 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:10:21,401 [INFO]    ðŸš« ML Conviction too low: 0.467
2025-12-04 14:10:21,401 [INFO] ðŸ“¡ ADAUSDT Signal: HOLD (score: 11/15)
2025-12-04 14:10:21,401 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 14:10:21,402 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 14:10:21,402 [INFO]    âšª No signal - HOLD
2025-12-04 14:10:21,902 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-04 14:10:21,986 [INFO]    Current position: LONG 0.11
2025-12-04 14:10:21,986 [INFO]    Entry: $924.70 | Mark: $907.05
2025-12-04 14:10:21,986 [INFO]    PnL: -19.09% ($-1.94)
2025-12-04 14:10:21,986 [INFO]    Age: 11.7h / 72.0h
2025-12-04 14:10:22,487 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-04 14:10:22,572 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-04 14:10:23,389 [INFO] ðŸ“¡ DOGEUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:10:23,394 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:10:23,394 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:10:23,394 [INFO]    âšª No signal - HOLD
2025-12-04 14:10:23,895 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-04 14:10:23,982 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-04 14:10:24,636 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 7/15
2025-12-04 14:10:24,637 [INFO]    âš ï¸ HTF aligned (RANGING), LTF diverging
2025-12-04 14:10:24,637 [INFO]    No clear pullback
2025-12-04 14:10:24,637 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:10:24,637 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:10:24,637 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:10:24,637 [INFO]    ðŸš« ML Conviction too low: 0.465
2025-12-04 14:10:24,637 [INFO] ðŸ“¡ UNIUSDT Signal: HOLD (score: 7/15)
2025-12-04 14:10:24,638 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-12-04 14:10:24,638 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (RANGING), LTF diverging, No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 14:10:24,638 [INFO]    âšª No signal - HOLD
2025-12-04 14:10:25,139 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-04 14:10:25,224 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-04 14:10:25,923 [INFO] ðŸŽ¯ LINKUSDT LONG Signal | Score: 10/15
2025-12-04 14:10:25,923 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:10:25,923 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:10:25,923 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:10:25,924 [INFO]    âš¡ RSI acceptable range
2025-12-04 14:10:25,924 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:10:25,924 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:10:25,924 [INFO]    ðŸš« ML Conviction too low: 0.482
2025-12-04 14:10:25,924 [INFO] ðŸ“¡ LINKUSDT Signal: HOLD (score: 10/15)
2025-12-04 14:10:25,924 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=10
2025-12-04 14:10:25,925 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI acceptable range, ðŸ—½ NY session (high liquidity)
2025-12-04 14:10:25,925 [INFO]    âšª No signal - HOLD
2025-12-04 14:10:26,425 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-04 14:10:26,512 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-04 14:10:27,358 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:10:27,359 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:10:27,359 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:10:27,359 [INFO]    âšª No signal - HOLD
2025-12-04 14:10:27,860 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-04 14:10:27,946 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-04 14:10:28,643 [INFO] ðŸŽ¯ ETHUSDT LONG Signal | Score: 11/15
2025-12-04 14:10:28,643 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:10:28,643 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:10:28,643 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:10:28,643 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:10:28,643 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:10:28,643 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:10:28,643 [INFO]    ðŸš« ML Conviction too low: 0.478
2025-12-04 14:10:28,643 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 11/15)
2025-12-04 14:10:28,644 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 14:10:28,644 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 14:10:28,644 [INFO]    âšª No signal - HOLD
2025-12-04 14:10:29,145 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-04 14:10:29,233 [INFO]    Current position: LONG 0.69
2025-12-04 14:10:29,233 [INFO]    Entry: $145.48 | Mark: $142.54
2025-12-04 14:10:29,233 [INFO]    PnL: -20.17% ($-2.03)
2025-12-04 14:10:29,233 [INFO]    Age: 12.6h / 72.0h
2025-12-04 14:10:29,733 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-04 14:10:29,819 [INFO]    Current position: LONG 45.3
2025-12-04 14:10:29,819 [INFO]    Entry: $2.21 | Mark: $2.13
2025-12-04 14:10:29,819 [INFO]    PnL: -34.72% ($-3.47)
2025-12-04 14:10:29,819 [INFO]    Age: 16.1h / 72.0h
2025-12-04 14:10:30,320 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-04 14:10:30,405 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-04 14:10:31,213 [INFO] ðŸ“¡ DOTUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:10:31,214 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:10:31,214 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:10:31,214 [INFO]    âšª No signal - HOLD
2025-12-04 14:10:31,715 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-04 14:10:31,939 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-04 14:10:32,603 [INFO] ðŸŽ¯ AVAXUSDT LONG Signal | Score: 11/15
2025-12-04 14:10:32,603 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:10:32,603 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:10:32,603 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:10:32,603 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:10:32,603 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:10:32,603 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:10:32,603 [INFO]    ðŸš« ML Conviction too low: 0.443
2025-12-04 14:10:32,603 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 11/15)
2025-12-04 14:10:32,604 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 14:10:32,604 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 14:10:32,604 [INFO]    âšª No signal - HOLD
2025-12-04 14:10:33,105 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-04 14:10:33,187 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-04 14:10:33,886 [INFO] ðŸ“¡ NEARUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:10:33,887 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:10:33,887 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:10:33,888 [INFO]    âšª No signal - HOLD
2025-12-04 14:10:33,888 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-04 14:13:33,985 [INFO] 
============================================================
2025-12-04 14:13:33,986 [INFO] ðŸ”„ LOOP #12 - 2025-12-04 14:13:33
2025-12-04 14:13:33,986 [INFO] ============================================================
2025-12-04 14:13:34,073 [INFO] ðŸ’° Current balance: $39.11
2025-12-04 14:13:34,073 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-04 14:13:34,154 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-04 14:13:34,816 [INFO] ðŸŽ¯ ADAUSDT LONG Signal | Score: 11/15
2025-12-04 14:13:34,816 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:13:34,816 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:13:34,816 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:13:34,817 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:13:34,817 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:13:34,817 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:13:34,817 [INFO]    ðŸš« ML Conviction too low: 0.465
2025-12-04 14:13:34,817 [INFO] ðŸ“¡ ADAUSDT Signal: HOLD (score: 11/15)
2025-12-04 14:13:34,817 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 14:13:34,818 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 14:13:34,818 [INFO]    âšª No signal - HOLD
2025-12-04 14:13:35,319 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-04 14:13:35,404 [INFO]    Current position: LONG 0.11
2025-12-04 14:13:35,404 [INFO]    Entry: $924.70 | Mark: $908.24
2025-12-04 14:13:35,404 [INFO]    PnL: -17.80% ($-1.81)
2025-12-04 14:13:35,404 [INFO]    Age: 11.8h / 72.0h
2025-12-04 14:13:35,905 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-04 14:13:35,991 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-04 14:13:36,692 [INFO] ðŸ“¡ DOGEUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:13:36,696 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:13:36,696 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:13:36,696 [INFO]    âšª No signal - HOLD
2025-12-04 14:13:37,197 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-04 14:13:37,295 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-04 14:13:37,945 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 7/15
2025-12-04 14:13:37,945 [INFO]    âš ï¸ HTF aligned (RANGING), LTF diverging
2025-12-04 14:13:37,945 [INFO]    No clear pullback
2025-12-04 14:13:37,945 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:13:37,945 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:13:37,945 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:13:37,945 [INFO]    ðŸš« ML Conviction too low: 0.459
2025-12-04 14:13:37,945 [INFO] ðŸ“¡ UNIUSDT Signal: HOLD (score: 7/15)
2025-12-04 14:13:37,946 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-12-04 14:13:37,946 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (RANGING), LTF diverging, No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 14:13:37,946 [INFO]    âšª No signal - HOLD
2025-12-04 14:13:38,447 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-04 14:13:38,531 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-04 14:13:39,237 [INFO] ðŸŽ¯ LINKUSDT LONG Signal | Score: 10/15
2025-12-04 14:13:39,237 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:13:39,238 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:13:39,238 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:13:39,238 [INFO]    âš¡ RSI acceptable range
2025-12-04 14:13:39,238 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:13:39,238 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:13:39,238 [INFO]    ðŸš« ML Conviction too low: 0.482
2025-12-04 14:13:39,238 [INFO] ðŸ“¡ LINKUSDT Signal: HOLD (score: 10/15)
2025-12-04 14:13:39,239 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=10
2025-12-04 14:13:39,239 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI acceptable range, ðŸ—½ NY session (high liquidity)
2025-12-04 14:13:39,239 [INFO]    âšª No signal - HOLD
2025-12-04 14:13:39,740 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-04 14:13:39,822 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-04 14:13:40,483 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:13:40,483 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:13:40,484 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:13:40,484 [INFO]    âšª No signal - HOLD
2025-12-04 14:13:40,984 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-04 14:13:41,070 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-04 14:13:41,776 [INFO] ðŸŽ¯ ETHUSDT LONG Signal | Score: 11/15
2025-12-04 14:13:41,776 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:13:41,777 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:13:41,777 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:13:41,777 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:13:41,777 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:13:41,777 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:13:41,777 [INFO]    ðŸš« ML Conviction too low: 0.475
2025-12-04 14:13:41,777 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 11/15)
2025-12-04 14:13:41,778 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 14:13:41,778 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 14:13:41,778 [INFO]    âšª No signal - HOLD
2025-12-04 14:13:42,279 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-04 14:13:42,500 [INFO]    Current position: LONG 0.69
2025-12-04 14:13:42,501 [INFO]    Entry: $145.48 | Mark: $142.58
2025-12-04 14:13:42,501 [INFO]    PnL: -19.90% ($-2.00)
2025-12-04 14:13:42,501 [INFO]    Age: 12.6h / 72.0h
2025-12-04 14:13:43,001 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-04 14:13:43,085 [INFO]    Current position: LONG 45.3
2025-12-04 14:13:43,085 [INFO]    Entry: $2.21 | Mark: $2.13
2025-12-04 14:13:43,085 [INFO]    PnL: -33.84% ($-3.39)
2025-12-04 14:13:43,085 [INFO]    Age: 16.2h / 72.0h
2025-12-04 14:13:43,585 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-04 14:13:43,669 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-04 14:13:44,344 [INFO] ðŸ“¡ DOTUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:13:44,345 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:13:44,345 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:13:44,346 [INFO]    âšª No signal - HOLD
2025-12-04 14:13:44,846 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-04 14:13:44,934 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-04 14:13:45,626 [INFO] ðŸŽ¯ AVAXUSDT LONG Signal | Score: 14/15
2025-12-04 14:13:45,627 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:13:45,627 [INFO]    âœ… Perfect pullback to EMA21
2025-12-04 14:13:45,627 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:13:45,627 [INFO]    ðŸ“ˆ Strong volume spike (2x)
2025-12-04 14:13:45,627 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:13:45,627 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:13:45,627 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:13:45,627 [INFO]    ðŸš« ML Conviction too low: 0.407
2025-12-04 14:13:45,627 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 14/15)
2025-12-04 14:13:45,628 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=14
2025-12-04 14:13:45,628 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âœ… Perfect pullback to EMA21, ðŸ”‘ At swing low (support), ðŸ“ˆ Strong volume spike (2x), âš¡ RSI neutral (good for entry)
2025-12-04 14:13:45,628 [INFO]    âšª No signal - HOLD
2025-12-04 14:13:46,129 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-04 14:13:46,214 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-04 14:13:47,061 [INFO] ðŸ“¡ NEARUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:13:47,062 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:13:47,062 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:13:47,062 [INFO]    âšª No signal - HOLD
2025-12-04 14:13:47,062 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-04 14:16:47,158 [INFO] 
============================================================
2025-12-04 14:16:47,159 [INFO] ðŸ”„ LOOP #13 - 2025-12-04 14:16:47
2025-12-04 14:16:47,159 [INFO] ============================================================
2025-12-04 14:16:47,245 [INFO] ðŸ’° Current balance: $39.11
2025-12-04 14:16:47,245 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-04 14:16:47,329 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-04 14:16:47,996 [INFO] ðŸŽ¯ ADAUSDT LONG Signal | Score: 11/15
2025-12-04 14:16:47,997 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:16:47,997 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:16:47,997 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:16:47,997 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:16:47,997 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:16:47,997 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:16:47,997 [INFO]    ðŸš« ML Conviction too low: 0.452
2025-12-04 14:16:47,997 [INFO] ðŸ“¡ ADAUSDT Signal: HOLD (score: 11/15)
2025-12-04 14:16:47,998 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 14:16:47,998 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 14:16:47,998 [INFO]    âšª No signal - HOLD
2025-12-04 14:16:48,499 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-04 14:16:48,584 [INFO]    Current position: LONG 0.11
2025-12-04 14:16:48,584 [INFO]    Entry: $924.70 | Mark: $907.09
2025-12-04 14:16:48,584 [INFO]    PnL: -19.04% ($-1.94)
2025-12-04 14:16:48,584 [INFO]    Age: 11.8h / 72.0h
2025-12-04 14:16:49,085 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-04 14:16:49,170 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-04 14:16:49,914 [INFO] ðŸ“¡ DOGEUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:16:49,915 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:16:49,915 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:16:49,915 [INFO]    âšª No signal - HOLD
2025-12-04 14:16:50,416 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-04 14:16:50,506 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-04 14:16:51,235 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 7/15
2025-12-04 14:16:51,235 [INFO]    âš ï¸ HTF aligned (RANGING), LTF diverging
2025-12-04 14:16:51,235 [INFO]    No clear pullback
2025-12-04 14:16:51,235 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:16:51,235 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:16:51,235 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:16:51,235 [INFO]    ðŸš« ML Conviction too low: 0.472
2025-12-04 14:16:51,235 [INFO] ðŸ“¡ UNIUSDT Signal: HOLD (score: 7/15)
2025-12-04 14:16:51,236 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-12-04 14:16:51,236 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (RANGING), LTF diverging, No clear pullback, ðŸ”‘ At swing low (support), ðŸ—½ NY session (high liquidity), âœ… R:R = 2.0:1
2025-12-04 14:16:51,236 [INFO]    âšª No signal - HOLD
2025-12-04 14:16:51,737 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-04 14:16:51,822 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-04 14:16:52,546 [INFO] ðŸŽ¯ LINKUSDT LONG Signal | Score: 10/15
2025-12-04 14:16:52,546 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:16:52,547 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:16:52,547 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:16:52,547 [INFO]    âš¡ RSI acceptable range
2025-12-04 14:16:52,547 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:16:52,547 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:16:52,547 [INFO]    ðŸš« ML Conviction too low: 0.480
2025-12-04 14:16:52,547 [INFO] ðŸ“¡ LINKUSDT Signal: HOLD (score: 10/15)
2025-12-04 14:16:52,548 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=10
2025-12-04 14:16:52,548 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI acceptable range, ðŸ—½ NY session (high liquidity)
2025-12-04 14:16:52,548 [INFO]    âšª No signal - HOLD
2025-12-04 14:16:53,048 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-04 14:16:53,131 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-04 14:16:53,853 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:16:53,854 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:16:53,854 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:16:53,855 [INFO]    âšª No signal - HOLD
2025-12-04 14:16:54,355 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-04 14:16:54,441 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-04 14:16:55,138 [INFO] ðŸŽ¯ ETHUSDT LONG Signal | Score: 11/15
2025-12-04 14:16:55,139 [INFO]    âš ï¸ HTF aligned (UP), LTF diverging
2025-12-04 14:16:55,139 [INFO]    âš ï¸ Near EMA21
2025-12-04 14:16:55,139 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:16:55,139 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:16:55,139 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:16:55,139 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:16:55,139 [INFO]    ðŸš« ML Conviction too low: 0.465
2025-12-04 14:16:55,139 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 11/15)
2025-12-04 14:16:55,140 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=11
2025-12-04 14:16:55,140 [INFO]    ðŸ“ Signal reasons: âš ï¸ HTF aligned (UP), LTF diverging, âš ï¸ Near EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 14:16:55,140 [INFO]    âšª No signal - HOLD
2025-12-04 14:16:55,641 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-04 14:16:55,728 [INFO]    Current position: LONG 0.69
2025-12-04 14:16:55,728 [INFO]    Entry: $145.48 | Mark: $142.52
2025-12-04 14:16:55,728 [INFO]    PnL: -20.34% ($-2.04)
2025-12-04 14:16:55,728 [INFO]    Age: 12.7h / 72.0h
2025-12-04 14:16:56,229 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-04 14:16:56,314 [INFO]    Current position: LONG 45.3
2025-12-04 14:16:56,314 [INFO]    Entry: $2.21 | Mark: $2.13
2025-12-04 14:16:56,315 [INFO]    PnL: -34.61% ($-3.46)
2025-12-04 14:16:56,315 [INFO]    Age: 16.2h / 72.0h
2025-12-04 14:16:56,815 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-04 14:16:56,898 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-04 14:16:57,691 [INFO] ðŸ“¡ DOTUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:16:57,692 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:16:57,692 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:16:57,693 [INFO]    âšª No signal - HOLD
2025-12-04 14:16:58,193 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-04 14:16:58,279 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-04 14:16:59,112 [INFO] ðŸŽ¯ AVAXUSDT LONG Signal | Score: 13/15
2025-12-04 14:16:59,112 [INFO]    âœ… Perfect alignment: All TFs UP
2025-12-04 14:16:59,113 [INFO]    âœ… Perfect pullback to EMA21
2025-12-04 14:16:59,113 [INFO]    ðŸ”‘ At swing low (support)
2025-12-04 14:16:59,113 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-04 14:16:59,113 [INFO]    ðŸ—½ NY session (high liquidity)
2025-12-04 14:16:59,113 [INFO]    âœ… R:R = 2.0:1
2025-12-04 14:16:59,113 [INFO]    ðŸš« ML Conviction too low: 0.512
2025-12-04 14:16:59,113 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 13/15)
2025-12-04 14:16:59,114 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=13
2025-12-04 14:16:59,114 [INFO]    ðŸ“ Signal reasons: âœ… Perfect alignment: All TFs UP, âœ… Perfect pullback to EMA21, ðŸ”‘ At swing low (support), âš¡ RSI neutral (good for entry), ðŸ—½ NY session (high liquidity)
2025-12-04 14:16:59,114 [INFO]    âšª No signal - HOLD
2025-12-04 14:16:59,615 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-04 14:16:59,702 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-04 14:17:00,392 [INFO] ðŸ“¡ NEARUSDT Signal: HOLD (score: 0/15)
2025-12-04 14:17:00,393 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-04 14:17:00,393 [INFO]    ðŸ“ Signal reasons: âŒ No trend alignment - too risky
2025-12-04 14:17:00,393 [INFO]    âšª No signal - HOLD
2025-12-04 14:17:00,393 [INFO] 
ðŸ’¤ Sleeping 180s...
