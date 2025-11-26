2025-11-13 04:48:18,658 [INFO] 
============================================================
2025-11-13 04:48:18,658 [INFO] ðŸ›‘ SHUTTING DOWN BOT
2025-11-13 04:48:18,658 [INFO] ============================================================
2025-11-13 04:48:18,658 [INFO] ðŸ“Š <b>DAILY STATS</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
Trades: 2
Volume: $0.00M
PnL: 0.00%

<b>Overall</b>
Total Trades: 2
Win Rate: 0.0%
W/L: 0/0
2025-11-13 04:48:19,432 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:48:19,435 [INFO] ðŸ‘‹ Bot stopped!
2025-11-13 04:48:19,823 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
âœ… Using fixed position size: $10.0 USDT per trade
âœ… Config validation passed!
2025-11-13 04:48:22,743 [INFO] âœ… Telegram bot initialized
2025-11-13 04:48:29,104 [INFO] ============================================================
2025-11-13 04:48:29,104 [INFO] ðŸš€ ASTERDEX PERP FARM BOT - INITIALIZING
2025-11-13 04:48:29,104 [INFO] ============================================================
2025-11-13 04:48:29,371 [INFO] ðŸ”Œ AsterDEX Client initialized (MAINNET)
2025-11-13 04:48:29,371 [INFO]    URL: https://fapi.asterdex.com/fapi
2025-11-13 04:48:29,371 [INFO] ðŸ“‚ Loaded 1 position timestamps
2025-11-13 04:48:29,372 [INFO] ðŸ“ˆ Trailing Stop enabled: Activation=1.0%, Trail=0.3%
2025-11-13 04:48:29,372 [INFO] ðŸŽ­ Loading Ensemble models...
2025-11-13 04:48:29,384 [INFO] ðŸ§  LSTM Model initialized on cpu
2025-11-13 04:48:29,384 [INFO]    Input: 14, Hidden: 128, Layers: 3, Dropout: 0.3
2025-11-13 04:48:29,385 [INFO] ðŸŽ­ Ensemble initialized with 2 models
2025-11-13 04:48:29,385 [INFO]    Models: ['lstm', 'xgboost']
2025-11-13 04:48:29,385 [INFO]    Weights: [0.3 0.7]
2025-11-13 04:48:29,406 [INFO] âœ… Model loaded from models/lstm_model.pt
2025-11-13 04:48:29,406 [INFO] âœ… LSTM loaded
2025-11-13 04:48:29,500 [INFO] âœ… XGBoost model loaded from models/xgboost_model.json
2025-11-13 04:48:29,501 [INFO] âœ… XGBoost loaded
2025-11-13 04:48:29,501 [INFO] âœ… Ensemble loaded: 2/2 models
2025-11-13 04:48:29,501 [INFO] ðŸŽ­ Using Ensemble predictor: ['lstm', 'xgboost']
2025-11-13 04:48:29,501 [INFO]    Weights: [0.3, 0.7]
2025-11-13 04:48:29,501 [INFO] ðŸŽ¯ Advanced Entry System enabled (min score: 4)
2025-11-13 04:48:29,501 [INFO] âœ… Bot initialized successfully!
2025-11-13 04:48:29,501 [INFO]    Symbols: ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'LTCUSDT', 'AVAXUSDT', 'XRPUSDT']
2025-11-13 04:48:29,501 [INFO]    Leverage: 10x
2025-11-13 04:48:29,501 [INFO]    Position Size: 20.0%
2025-11-13 04:48:29,501 [INFO]    TP/SL: 1.00% / Disabled
2025-11-13 04:48:29,501 [INFO]    Position Timeout: 36.0h
2025-11-13 04:48:29,501 [INFO] ============================================================
2025-11-13 04:48:29,502 [INFO] ðŸ BOT STARTED!
2025-11-13 04:48:30,229 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:48:30,509 [INFO] ðŸ“Š Daily start balance: $17.84
2025-11-13 04:48:30,510 [INFO] ðŸ’° Starting balance: $17.84
2025-11-13 04:48:30,899 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:48:30,902 [INFO] 
============================================================
2025-11-13 04:48:30,902 [INFO] ðŸ”„ LOOP #1 - 2025-11-13 04:48:30
2025-11-13 04:48:30,902 [INFO] ============================================================
2025-11-13 04:48:31,005 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 04:48:31,006 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 04:48:31,104 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 04:48:31,478 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:48:31,479 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:48:31,479 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:48:31,479 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:48:31,479 [INFO]    âšª No signal - HOLD
2025-11-13 04:48:31,980 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 04:48:32,182 [INFO]    Current position: LONG 0.029
2025-11-13 04:48:32,182 [INFO]    Entry: $3474.80 | Mark: $3463.85
2025-11-13 04:48:32,182 [INFO]    PnL: -0.32% ($-0.32)
2025-11-13 04:48:32,182 [INFO]    Age: 0.4h / 36.0h
2025-11-13 04:48:32,683 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 04:48:32,784 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 04:48:33,165 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:48:33,165 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:48:33,166 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:48:33,166 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:48:33,166 [INFO]    âšª No signal - HOLD
2025-11-13 04:48:33,667 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 04:48:33,867 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 04:48:34,228 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:48:34,228 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): â­ Evening Star
2025-11-13 04:48:34,228 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:48:34,229 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): â­ Evening Star
2025-11-13 04:48:34,229 [INFO]    âšª No signal - HOLD
2025-11-13 04:48:34,730 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 04:48:34,832 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 04:48:35,183 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:48:35,183 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:48:35,183 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:48:35,183 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:48:35,184 [INFO]    âšª No signal - HOLD
2025-11-13 04:48:35,685 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 04:48:35,889 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 04:48:36,241 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:48:36,241 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 04:48:36,241 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:48:36,242 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 04:48:36,242 [INFO]    âšª No signal - HOLD
2025-11-13 04:48:36,242 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 04:49:36,271 [INFO] 
============================================================
2025-11-13 04:49:36,271 [INFO] ðŸ”„ LOOP #2 - 2025-11-13 04:49:36
2025-11-13 04:49:36,272 [INFO] ============================================================
2025-11-13 04:49:36,372 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 04:49:36,372 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 04:49:36,477 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 04:49:36,869 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:49:36,869 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:49:36,870 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:49:36,870 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:49:36,870 [INFO]    âšª No signal - HOLD
2025-11-13 04:49:37,371 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 04:49:37,471 [INFO]    Current position: LONG 0.029
2025-11-13 04:49:37,472 [INFO]    Entry: $3474.80 | Mark: $3467.47
2025-11-13 04:49:37,472 [INFO]    PnL: -0.21% ($-0.21)
2025-11-13 04:49:37,472 [INFO]    Age: 0.4h / 36.0h
2025-11-13 04:49:37,973 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 04:49:38,075 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 04:49:38,452 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 04:49:38,453 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 04:49:38,454 [INFO]    ðŸ“ Signal reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 04:49:38,454 [INFO]    âšª No signal - HOLD
2025-11-13 04:49:38,955 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 04:49:39,057 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 04:49:39,438 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:49:39,438 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): â­ Evening Star
2025-11-13 04:49:39,439 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:49:39,439 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): â­ Evening Star
2025-11-13 04:49:39,439 [INFO]    âšª No signal - HOLD
2025-11-13 04:49:39,940 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 04:49:40,040 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 04:49:40,419 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:49:40,419 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:49:40,420 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:49:40,420 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:49:40,420 [INFO]    âšª No signal - HOLD
2025-11-13 04:49:40,921 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 04:49:41,024 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 04:49:41,391 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:49:41,391 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 04:49:41,392 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:49:41,392 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 04:49:41,392 [INFO]    âšª No signal - HOLD
2025-11-13 04:49:41,392 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 04:50:41,425 [INFO] 
============================================================
2025-11-13 04:50:41,426 [INFO] ðŸ”„ LOOP #3 - 2025-11-13 04:50:41
2025-11-13 04:50:41,426 [INFO] ============================================================
2025-11-13 04:50:41,525 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 04:50:41,525 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 04:50:41,627 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 04:50:42,010 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:50:42,010 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): âš¡ MACD Death Cross
2025-11-13 04:50:42,010 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:50:42,011 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): âš¡ MACD Death Cross
2025-11-13 04:50:42,011 [INFO]    âšª No signal - HOLD
2025-11-13 04:50:42,511 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 04:50:42,611 [INFO]    Current position: LONG 0.029
2025-11-13 04:50:42,611 [INFO]    Entry: $3474.80 | Mark: $3462.65
2025-11-13 04:50:42,611 [INFO]    PnL: -0.35% ($-0.35)
2025-11-13 04:50:42,611 [INFO]    Age: 0.4h / 36.0h
2025-11-13 04:50:43,112 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 04:50:43,210 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 04:50:43,561 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:50:43,561 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:50:43,561 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:50:43,561 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:50:43,561 [INFO]    âšª No signal - HOLD
2025-11-13 04:50:44,062 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 04:50:44,163 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 04:50:44,516 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:50:44,516 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): â­ Evening Star
2025-11-13 04:50:44,517 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:50:44,517 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): â­ Evening Star
2025-11-13 04:50:44,517 [INFO]    âšª No signal - HOLD
2025-11-13 04:50:45,018 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 04:50:45,118 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 04:50:45,479 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:50:45,479 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:50:45,480 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:50:45,480 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:50:45,480 [INFO]    âšª No signal - HOLD
2025-11-13 04:50:45,981 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 04:50:46,083 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 04:50:46,459 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:50:46,459 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 04:50:46,460 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:50:46,460 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 04:50:46,460 [INFO]    âšª No signal - HOLD
2025-11-13 04:50:46,460 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 04:51:46,521 [INFO] 
============================================================
2025-11-13 04:51:46,521 [INFO] ðŸ”„ LOOP #4 - 2025-11-13 04:51:46
2025-11-13 04:51:46,521 [INFO] ============================================================
2025-11-13 04:51:46,624 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 04:51:46,625 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 04:51:46,722 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 04:51:47,110 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:51:47,110 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): âš¡ MACD Death Cross
2025-11-13 04:51:47,111 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:51:47,111 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): âš¡ MACD Death Cross
2025-11-13 04:51:47,111 [INFO]    âšª No signal - HOLD
2025-11-13 04:51:47,612 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 04:51:47,714 [INFO]    Current position: LONG 0.029
2025-11-13 04:51:47,714 [INFO]    Entry: $3474.80 | Mark: $3461.20
2025-11-13 04:51:47,714 [INFO]    PnL: -0.39% ($-0.39)
2025-11-13 04:51:47,714 [INFO]    Age: 0.5h / 36.0h
2025-11-13 04:51:48,215 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 04:51:48,325 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 04:51:48,688 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:51:48,688 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:51:48,689 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:51:48,689 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:51:48,689 [INFO]    âšª No signal - HOLD
2025-11-13 04:51:49,189 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 04:51:49,294 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 04:51:49,660 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:51:49,660 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): â­ Evening Star
2025-11-13 04:51:49,660 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:51:49,661 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): â­ Evening Star
2025-11-13 04:51:49,661 [INFO]    âšª No signal - HOLD
2025-11-13 04:51:50,162 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 04:51:50,265 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 04:51:50,619 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:51:50,620 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:51:50,620 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:51:50,620 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:51:50,620 [INFO]    âšª No signal - HOLD
2025-11-13 04:51:51,121 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 04:51:51,220 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 04:51:51,601 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:51:51,601 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:51:51,602 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:51:51,602 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:51:51,602 [INFO]    âšª No signal - HOLD
2025-11-13 04:51:51,603 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 04:52:51,613 [INFO] 
============================================================
2025-11-13 04:52:51,614 [INFO] ðŸ”„ LOOP #5 - 2025-11-13 04:52:51
2025-11-13 04:52:51,614 [INFO] ============================================================
2025-11-13 04:52:52,208 [INFO] ðŸ’“ Bot alive - Loop #5 - Active positions: 1
2025-11-13 04:52:52,311 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 04:52:52,311 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 04:52:52,412 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 04:52:52,771 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:52:52,772 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): âš¡ MACD Death Cross
2025-11-13 04:52:52,772 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:52:52,772 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): âš¡ MACD Death Cross
2025-11-13 04:52:52,772 [INFO]    âšª No signal - HOLD
2025-11-13 04:52:53,273 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 04:52:53,372 [INFO]    Current position: LONG 0.029
2025-11-13 04:52:53,372 [INFO]    Entry: $3474.80 | Mark: $3473.28
2025-11-13 04:52:53,372 [INFO]    PnL: -0.04% ($-0.04)
2025-11-13 04:52:53,372 [INFO]    Age: 0.5h / 36.0h
2025-11-13 04:52:53,873 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 04:52:53,976 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 04:52:54,341 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:52:54,342 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:52:54,342 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:52:54,342 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:52:54,342 [INFO]    âšª No signal - HOLD
2025-11-13 04:52:54,843 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 04:52:54,946 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 04:52:55,426 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:52:55,426 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): â­ Evening Star
2025-11-13 04:52:55,427 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:52:55,427 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): â­ Evening Star
2025-11-13 04:52:55,427 [INFO]    âšª No signal - HOLD
2025-11-13 04:52:55,928 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 04:52:56,028 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 04:52:56,477 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:52:56,477 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:52:56,478 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:52:56,478 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:52:56,478 [INFO]    âšª No signal - HOLD
2025-11-13 04:52:56,979 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 04:52:57,078 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 04:52:57,447 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:52:57,448 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:52:57,448 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:52:57,448 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:52:57,448 [INFO]    âšª No signal - HOLD
2025-11-13 04:52:57,449 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 04:53:57,506 [INFO] 
============================================================
2025-11-13 04:53:57,506 [INFO] ðŸ”„ LOOP #6 - 2025-11-13 04:53:57
2025-11-13 04:53:57,506 [INFO] ============================================================
2025-11-13 04:53:57,611 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 04:53:57,611 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 04:53:57,711 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 04:53:58,153 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:53:58,154 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:53:58,154 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:53:58,156 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:53:58,156 [INFO]    âšª No signal - HOLD
2025-11-13 04:53:58,657 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 04:53:58,757 [INFO]    Current position: LONG 0.029
2025-11-13 04:53:58,757 [INFO]    Entry: $3474.80 | Mark: $3469.15
2025-11-13 04:53:58,757 [INFO]    PnL: -0.16% ($-0.16)
2025-11-13 04:53:58,757 [INFO]    Age: 0.5h / 36.0h
2025-11-13 04:53:59,258 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 04:53:59,358 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 04:53:59,713 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:53:59,713 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:53:59,714 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:53:59,714 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:53:59,714 [INFO]    âšª No signal - HOLD
2025-11-13 04:54:00,215 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 04:54:00,319 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 04:54:00,670 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:54:00,670 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): â­ Evening Star
2025-11-13 04:54:00,671 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:54:00,671 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): â­ Evening Star
2025-11-13 04:54:00,671 [INFO]    âšª No signal - HOLD
2025-11-13 04:54:01,172 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 04:54:01,270 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 04:54:01,617 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:54:01,617 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:54:01,618 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:54:01,618 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:54:01,618 [INFO]    âšª No signal - HOLD
2025-11-13 04:54:02,119 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 04:54:02,221 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 04:54:02,596 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:54:02,596 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:54:02,596 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:54:02,597 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:54:02,597 [INFO]    âšª No signal - HOLD
2025-11-13 04:54:02,597 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 04:55:02,642 [INFO] 
============================================================
2025-11-13 04:55:02,642 [INFO] ðŸ”„ LOOP #7 - 2025-11-13 04:55:02
2025-11-13 04:55:02,642 [INFO] ============================================================
2025-11-13 04:55:02,755 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 04:55:02,756 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 04:55:02,857 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 04:55:03,252 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:55:03,252 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:55:03,252 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:55:03,252 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:55:03,253 [INFO]    âšª No signal - HOLD
2025-11-13 04:55:03,753 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 04:55:03,866 [INFO]    Current position: LONG 0.029
2025-11-13 04:55:03,866 [INFO]    Entry: $3474.80 | Mark: $3471.01
2025-11-13 04:55:03,866 [INFO]    PnL: -0.11% ($-0.11)
2025-11-13 04:55:03,866 [INFO]    Age: 0.5h / 36.0h
2025-11-13 04:55:04,367 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 04:55:04,467 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 04:55:04,829 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:55:04,829 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:55:04,830 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:55:04,830 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:55:04,830 [INFO]    âšª No signal - HOLD
2025-11-13 04:55:05,331 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 04:55:05,434 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 04:55:05,905 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 04:55:05,906 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 04:55:05,906 [INFO]    ðŸ“ Top Reasons:
2025-11-13 04:55:05,906 [INFO]       1. ðŸ“Œ Bullish Pin Bar
2025-11-13 04:55:05,906 [INFO]       2. ðŸ”· Bullish Order Block
2025-11-13 04:55:05,906 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.542 | RSI: 57.9 | OB: 0.87
2025-11-13 04:55:05,906 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 04:55:05,907 [INFO]    ðŸ“ Signal reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 04:55:05,907 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 04:55:05,907 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 04:55:05,907 [INFO]    ðŸ“ Top reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 04:55:05,907 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 04:55:06,004 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 04:55:06,203 [INFO]    ðŸ’µ Current price: $99.55
2025-11-13 04:55:06,314 [INFO]    ðŸ’° Position calculation:
2025-11-13 04:55:06,315 [INFO]       Balance: $17.84
2025-11-13 04:55:06,315 [INFO]       Price: $99.55
2025-11-13 04:55:06,315 [INFO]       Capital (fixed): $10.00
2025-11-13 04:55:06,315 [INFO]       Leverage: 10x
2025-11-13 04:55:06,315 [INFO]       Raw quantity: 1.00452034
2025-11-13 04:55:06,315 [INFO]       Formatted quantity: 1.00500000
2025-11-13 04:55:06,315 [INFO]    ðŸ“¤ Placing BUY order for 1.005 LTCUSDT...
2025-11-13 04:55:06,315 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 04:55:06,315 [INFO]    Raw qty: 1.00500000 -> Formatted: 1.005
2025-11-13 04:55:06,673 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 04:55:07,396 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:55:07,398 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 1.005
2025-11-13 04:55:07,782 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:55:07,784 [ERROR]    âŒ Order placement failed!
2025-11-13 04:55:08,170 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:55:08,673 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 04:55:08,773 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 04:55:09,129 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:55:09,129 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:55:09,130 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:55:09,130 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:55:09,130 [INFO]    âšª No signal - HOLD
2025-11-13 04:55:09,631 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 04:55:09,732 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 04:55:10,186 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:55:10,187 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 04:55:10,187 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:55:10,187 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 04:55:10,187 [INFO]    âšª No signal - HOLD
2025-11-13 04:55:10,188 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 04:56:10,235 [INFO] 
============================================================
2025-11-13 04:56:10,235 [INFO] ðŸ”„ LOOP #8 - 2025-11-13 04:56:10
2025-11-13 04:56:10,236 [INFO] ============================================================
2025-11-13 04:56:10,349 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 04:56:10,349 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 04:56:10,450 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 04:56:10,850 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:56:10,851 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:56:10,851 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:56:10,852 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:56:10,852 [INFO]    âšª No signal - HOLD
2025-11-13 04:56:11,352 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 04:56:11,457 [INFO]    Current position: LONG 0.029
2025-11-13 04:56:11,457 [INFO]    Entry: $3474.80 | Mark: $3470.08
2025-11-13 04:56:11,457 [INFO]    PnL: -0.14% ($-0.14)
2025-11-13 04:56:11,457 [INFO]    Age: 0.5h / 36.0h
2025-11-13 04:56:11,958 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 04:56:12,057 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 04:56:12,410 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:56:12,411 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:56:12,411 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:56:12,411 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:56:12,411 [INFO]    âšª No signal - HOLD
2025-11-13 04:56:12,912 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 04:56:13,011 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 04:56:13,364 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:56:13,364 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): â­ Evening Star
2025-11-13 04:56:13,365 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:56:13,365 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): â­ Evening Star
2025-11-13 04:56:13,365 [INFO]    âšª No signal - HOLD
2025-11-13 04:56:13,866 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 04:56:13,967 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 04:56:14,447 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:56:14,447 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:56:14,448 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:56:14,448 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:56:14,448 [INFO]    âšª No signal - HOLD
2025-11-13 04:56:14,949 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 04:56:15,153 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 04:56:15,519 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:56:15,520 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:56:15,520 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:56:15,520 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:56:15,521 [INFO]    âšª No signal - HOLD
2025-11-13 04:56:15,521 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 04:57:15,581 [INFO] 
============================================================
2025-11-13 04:57:15,581 [INFO] ðŸ”„ LOOP #9 - 2025-11-13 04:57:15
2025-11-13 04:57:15,581 [INFO] ============================================================
2025-11-13 04:57:15,684 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 04:57:15,684 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 04:57:15,784 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 04:57:16,217 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:57:16,217 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:57:16,218 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:57:16,218 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:57:16,218 [INFO]    âšª No signal - HOLD
2025-11-13 04:57:16,719 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 04:57:16,819 [INFO]    Current position: LONG 0.029
2025-11-13 04:57:16,819 [INFO]    Entry: $3474.80 | Mark: $3486.63
2025-11-13 04:57:16,820 [INFO]    PnL: 0.34% ($0.34)
2025-11-13 04:57:16,820 [INFO]    Age: 0.6h / 36.0h
2025-11-13 04:57:17,320 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 04:57:17,421 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 04:57:17,774 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 04:57:17,775 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 04:57:17,775 [INFO]    ðŸ“ Signal reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 04:57:17,775 [INFO]    âšª No signal - HOLD
2025-11-13 04:57:18,276 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 04:57:18,377 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 04:57:18,729 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 04:57:18,729 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 04:57:18,730 [INFO]    ðŸ“ Top Reasons:
2025-11-13 04:57:18,730 [INFO]       1. ðŸ“Œ Bullish Pin Bar
2025-11-13 04:57:18,730 [INFO]       2. ðŸ”· Bullish Order Block
2025-11-13 04:57:18,730 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.565 | RSI: 59.8 | OB: 1.34
2025-11-13 04:57:18,730 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 04:57:18,730 [INFO]    ðŸ“ Signal reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 04:57:18,730 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 04:57:18,731 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 04:57:18,731 [INFO]    ðŸ“ Top reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 04:57:18,731 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 04:57:18,831 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 04:57:19,025 [INFO]    ðŸ’µ Current price: $99.70
2025-11-13 04:57:19,025 [INFO]    ðŸ’° Position calculation:
2025-11-13 04:57:19,025 [INFO]       Balance: $17.84
2025-11-13 04:57:19,025 [INFO]       Price: $99.70
2025-11-13 04:57:19,025 [INFO]       Capital (fixed): $10.00
2025-11-13 04:57:19,025 [INFO]       Leverage: 10x
2025-11-13 04:57:19,025 [INFO]       Raw quantity: 1.00300903
2025-11-13 04:57:19,025 [INFO]       Formatted quantity: 1.00300000
2025-11-13 04:57:19,025 [INFO]    ðŸ“¤ Placing BUY order for 1.003 LTCUSDT...
2025-11-13 04:57:19,025 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 04:57:19,025 [INFO]    Raw qty: 1.00300000 -> Formatted: 1.003
2025-11-13 04:57:19,377 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 04:57:20,118 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:57:20,120 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 1.003
2025-11-13 04:57:20,513 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:57:20,515 [ERROR]    âŒ Order placement failed!
2025-11-13 04:57:20,899 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:57:21,402 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 04:57:21,508 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 04:57:21,874 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:57:21,874 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:57:21,875 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:57:21,875 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:57:21,875 [INFO]    âšª No signal - HOLD
2025-11-13 04:57:22,376 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 04:57:22,479 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 04:57:22,845 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:57:22,845 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 04:57:22,846 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:57:22,846 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 04:57:22,846 [INFO]    âšª No signal - HOLD
2025-11-13 04:57:22,846 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 04:58:22,864 [INFO] 
============================================================
2025-11-13 04:58:22,865 [INFO] ðŸ”„ LOOP #10 - 2025-11-13 04:58:22
2025-11-13 04:58:22,865 [INFO] ============================================================
2025-11-13 04:58:23,463 [INFO] ðŸ’“ Bot alive - Loop #10 - Active positions: 1
2025-11-13 04:58:23,566 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 04:58:23,566 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 04:58:23,665 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 04:58:24,046 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:58:24,046 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:58:24,047 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:58:24,048 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:58:24,048 [INFO]    âšª No signal - HOLD
2025-11-13 04:58:24,548 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 04:58:24,647 [INFO]    Current position: LONG 0.029
2025-11-13 04:58:24,647 [INFO]    Entry: $3474.80 | Mark: $3485.32
2025-11-13 04:58:24,647 [INFO]    PnL: 0.30% ($0.31)
2025-11-13 04:58:24,648 [INFO]    Age: 0.6h / 36.0h
2025-11-13 04:58:25,148 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 04:58:25,245 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 04:58:25,712 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 04:58:25,713 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 04:58:25,714 [INFO]    ðŸ“ Signal reasons: ðŸ•¯ï¸ Bullish Engulfing, ðŸ”· Bullish Order Block
2025-11-13 04:58:25,714 [INFO]    âšª No signal - HOLD
2025-11-13 04:58:26,215 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 04:58:26,315 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 04:58:26,688 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 04:58:26,689 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 04:58:26,689 [INFO]    ðŸ“ Top Reasons:
2025-11-13 04:58:26,689 [INFO]       1. ðŸ“Œ Bullish Pin Bar
2025-11-13 04:58:26,689 [INFO]       2. ðŸ”· Bullish Order Block
2025-11-13 04:58:26,689 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.564 | RSI: 59.6 | OB: 1.62
2025-11-13 04:58:26,690 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 04:58:26,690 [INFO]    ðŸ“ Signal reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 04:58:26,690 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 04:58:26,690 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 04:58:26,691 [INFO]    ðŸ“ Top reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 04:58:26,691 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 04:58:26,790 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 04:58:26,989 [INFO]    ðŸ’µ Current price: $99.70
2025-11-13 04:58:26,989 [INFO]    ðŸ’° Position calculation:
2025-11-13 04:58:26,989 [INFO]       Balance: $17.84
2025-11-13 04:58:26,989 [INFO]       Price: $99.70
2025-11-13 04:58:26,990 [INFO]       Capital (fixed): $10.00
2025-11-13 04:58:26,990 [INFO]       Leverage: 10x
2025-11-13 04:58:26,990 [INFO]       Raw quantity: 1.00300903
2025-11-13 04:58:26,990 [INFO]       Formatted quantity: 1.00300000
2025-11-13 04:58:26,990 [INFO]    ðŸ“¤ Placing BUY order for 1.003 LTCUSDT...
2025-11-13 04:58:26,990 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 04:58:26,990 [INFO]    Raw qty: 1.00300000 -> Formatted: 1.003
2025-11-13 04:58:27,345 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 04:58:28,084 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:58:28,086 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 1.003
2025-11-13 04:58:28,493 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:58:28,495 [ERROR]    âŒ Order placement failed!
2025-11-13 04:58:28,880 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:58:29,383 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 04:58:29,483 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 04:58:29,831 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:58:29,831 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:58:29,832 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:58:29,832 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:58:29,832 [INFO]    âšª No signal - HOLD
2025-11-13 04:58:30,333 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 04:58:30,434 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 04:58:30,803 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 04:58:30,803 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 04:58:30,803 [INFO]    ðŸ“ Top Reasons:
2025-11-13 04:58:30,803 [INFO]       1. ðŸ“Œ Bullish Pin Bar
2025-11-13 04:58:30,803 [INFO]       2. ðŸ”· Bullish Order Block
2025-11-13 04:58:30,803 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.715 | RSI: 72.0 | OB: 0.81
2025-11-13 04:58:30,804 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 04:58:30,804 [INFO]    ðŸ“ Signal reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 04:58:30,804 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 04:58:30,804 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 04:58:30,804 [INFO]    ðŸ“ Top reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 04:58:30,805 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 04:58:30,903 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 04:58:31,107 [INFO]    ðŸ’µ Current price: $2.47
2025-11-13 04:58:31,256 [INFO]    ðŸ’° Position calculation:
2025-11-13 04:58:31,257 [INFO]       Balance: $17.84
2025-11-13 04:58:31,257 [INFO]       Price: $2.47
2025-11-13 04:58:31,257 [INFO]       Capital (fixed): $10.00
2025-11-13 04:58:31,257 [INFO]       Leverage: 10x
2025-11-13 04:58:31,257 [INFO]       Raw quantity: 40.44325811
2025-11-13 04:58:31,257 [INFO]       Formatted quantity: 40.40000000
2025-11-13 04:58:31,257 [INFO]    ðŸ“¤ Placing BUY order for 40.4 XRPUSDT...
2025-11-13 04:58:31,257 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 04:58:31,257 [INFO]    Raw qty: 40.40000000 -> Formatted: 40.4
2025-11-13 04:58:31,608 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 04:58:31,995 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:58:31,997 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.4
2025-11-13 04:58:32,386 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:58:32,388 [ERROR]    âŒ Order placement failed!
2025-11-13 04:58:35,960 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:58:37,097 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 04:59:37,136 [INFO] 
============================================================
2025-11-13 04:59:37,137 [INFO] ðŸ”„ LOOP #11 - 2025-11-13 04:59:37
2025-11-13 04:59:37,137 [INFO] ============================================================
2025-11-13 04:59:37,249 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 04:59:37,249 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 04:59:37,351 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 04:59:37,729 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:59:37,729 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:59:37,730 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:59:37,730 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:59:37,731 [INFO]    âšª No signal - HOLD
2025-11-13 04:59:38,231 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 04:59:38,338 [INFO]    Current position: LONG 0.029
2025-11-13 04:59:38,338 [INFO]    Entry: $3474.80 | Mark: $3482.62
2025-11-13 04:59:38,338 [INFO]    PnL: 0.23% ($0.23)
2025-11-13 04:59:38,338 [INFO]    Age: 0.6h / 36.0h
2025-11-13 04:59:38,839 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 04:59:39,091 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 04:59:39,455 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:59:39,455 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:59:39,455 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:59:39,456 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 04:59:39,456 [INFO]    âšª No signal - HOLD
2025-11-13 04:59:39,957 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 04:59:40,062 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 04:59:40,423 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 04:59:40,424 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 04:59:40,424 [INFO]    ðŸ“ Top Reasons:
2025-11-13 04:59:40,424 [INFO]       1. ðŸ“Œ Bullish Pin Bar
2025-11-13 04:59:40,424 [INFO]       2. ðŸ”· Bullish Order Block
2025-11-13 04:59:40,424 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.574 | RSI: 59.7 | OB: 0.72
2025-11-13 04:59:40,425 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 04:59:40,425 [INFO]    ðŸ“ Signal reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 04:59:40,425 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 04:59:40,425 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 04:59:40,425 [INFO]    ðŸ“ Top reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 04:59:40,425 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 04:59:40,524 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 04:59:40,727 [INFO]    ðŸ’µ Current price: $99.73
2025-11-13 04:59:40,727 [INFO]    ðŸ’° Position calculation:
2025-11-13 04:59:40,727 [INFO]       Balance: $17.84
2025-11-13 04:59:40,728 [INFO]       Price: $99.73
2025-11-13 04:59:40,728 [INFO]       Capital (fixed): $10.00
2025-11-13 04:59:40,728 [INFO]       Leverage: 10x
2025-11-13 04:59:40,728 [INFO]       Raw quantity: 1.00270731
2025-11-13 04:59:40,728 [INFO]       Formatted quantity: 1.00300000
2025-11-13 04:59:40,728 [INFO]    ðŸ“¤ Placing BUY order for 1.003 LTCUSDT...
2025-11-13 04:59:40,728 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 04:59:40,728 [INFO]    Raw qty: 1.00300000 -> Formatted: 1.003
2025-11-13 04:59:41,082 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 04:59:41,824 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:59:41,826 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 1.003
2025-11-13 04:59:42,216 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:59:42,217 [ERROR]    âŒ Order placement failed!
2025-11-13 04:59:42,600 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:59:43,104 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 04:59:43,203 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 04:59:43,559 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 04:59:43,560 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:59:43,560 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 04:59:43,560 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 04:59:43,560 [INFO]    âšª No signal - HOLD
2025-11-13 04:59:44,061 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 04:59:44,164 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 04:59:44,509 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 04:59:44,509 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 04:59:44,509 [INFO]    ðŸ“ Top Reasons:
2025-11-13 04:59:44,509 [INFO]       1. ðŸ“Œ Bullish Pin Bar
2025-11-13 04:59:44,510 [INFO]       2. ðŸ”· Bullish Order Block
2025-11-13 04:59:44,510 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.712 | RSI: 71.4 | OB: 0.96
2025-11-13 04:59:44,510 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 04:59:44,510 [INFO]    ðŸ“ Signal reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 04:59:44,510 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 04:59:44,510 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 04:59:44,510 [INFO]    ðŸ“ Top reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 04:59:44,510 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 04:59:44,608 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 04:59:44,809 [INFO]    ðŸ’µ Current price: $2.47
2025-11-13 04:59:44,810 [INFO]    ðŸ’° Position calculation:
2025-11-13 04:59:44,810 [INFO]       Balance: $17.84
2025-11-13 04:59:44,810 [INFO]       Price: $2.47
2025-11-13 04:59:44,810 [INFO]       Capital (fixed): $10.00
2025-11-13 04:59:44,810 [INFO]       Leverage: 10x
2025-11-13 04:59:44,810 [INFO]       Raw quantity: 40.43181175
2025-11-13 04:59:44,810 [INFO]       Formatted quantity: 40.40000000
2025-11-13 04:59:44,810 [INFO]    ðŸ“¤ Placing BUY order for 40.4 XRPUSDT...
2025-11-13 04:59:44,811 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 04:59:44,811 [INFO]    Raw qty: 40.40000000 -> Formatted: 40.4
2025-11-13 04:59:45,163 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 04:59:45,551 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:59:45,553 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.4
2025-11-13 04:59:45,943 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:59:45,945 [ERROR]    âŒ Order placement failed!
2025-11-13 04:59:49,527 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:59:49,529 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:00:49,583 [INFO] 
============================================================
2025-11-13 05:00:49,583 [INFO] ðŸ”„ LOOP #12 - 2025-11-13 05:00:49
2025-11-13 05:00:49,583 [INFO] ============================================================
2025-11-13 05:00:49,686 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:00:49,686 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:00:49,794 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:00:50,238 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:00:50,239 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:00:50,239 [INFO]    ðŸ“ Signal reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 05:00:50,239 [INFO]    âšª No signal - HOLD
2025-11-13 05:00:50,740 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:00:50,837 [INFO]    Current position: LONG 0.029
2025-11-13 05:00:50,838 [INFO]    Entry: $3474.80 | Mark: $3481.90
2025-11-13 05:00:50,838 [INFO]    PnL: 0.20% ($0.21)
2025-11-13 05:00:50,838 [INFO]    Age: 0.6h / 36.0h
2025-11-13 05:00:51,339 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:00:51,441 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:00:51,823 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:00:51,823 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:00:51,824 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:00:51,824 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:00:51,825 [INFO]    âšª No signal - HOLD
2025-11-13 05:00:52,325 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:00:52,428 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:00:52,807 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:00:52,808 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:00:52,809 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:00:52,809 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:00:52,809 [INFO]    âšª No signal - HOLD
2025-11-13 05:00:53,309 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:00:53,414 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:00:53,790 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:00:53,791 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:00:53,792 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:00:53,792 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:00:53,792 [INFO]    âšª No signal - HOLD
2025-11-13 05:00:54,293 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:00:54,494 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:00:54,882 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:00:54,882 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:00:54,883 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:00:54,884 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:00:54,884 [INFO]    âšª No signal - HOLD
2025-11-13 05:00:54,884 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:01:54,944 [INFO] 
============================================================
2025-11-13 05:01:54,945 [INFO] ðŸ”„ LOOP #13 - 2025-11-13 05:01:54
2025-11-13 05:01:54,945 [INFO] ============================================================
2025-11-13 05:01:55,049 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:01:55,050 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:01:55,152 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:01:55,550 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:01:55,550 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:01:55,550 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:01:55,551 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:01:55,551 [INFO]    âšª No signal - HOLD
2025-11-13 05:01:56,053 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:01:56,258 [INFO]    Current position: LONG 0.029
2025-11-13 05:01:56,258 [INFO]    Entry: $3474.80 | Mark: $3479.89
2025-11-13 05:01:56,258 [INFO]    PnL: 0.15% ($0.15)
2025-11-13 05:01:56,258 [INFO]    Age: 0.6h / 36.0h
2025-11-13 05:01:56,759 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:01:56,861 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:01:57,219 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:01:57,220 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:01:57,220 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:01:57,221 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:01:57,221 [INFO]    âšª No signal - HOLD
2025-11-13 05:01:57,721 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:01:57,821 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:01:58,174 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:01:58,175 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:01:58,175 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:01:58,175 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:01:58,175 [INFO]    âšª No signal - HOLD
2025-11-13 05:01:58,676 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:01:58,777 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:01:59,140 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:01:59,141 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:01:59,141 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:01:59,141 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:01:59,141 [INFO]    âšª No signal - HOLD
2025-11-13 05:01:59,642 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:01:59,742 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:02:00,104 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:02:00,104 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:02:00,105 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:02:00,105 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:02:00,105 [INFO]    âšª No signal - HOLD
2025-11-13 05:02:00,106 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:03:00,150 [INFO] 
============================================================
2025-11-13 05:03:00,150 [INFO] ðŸ”„ LOOP #14 - 2025-11-13 05:03:00
2025-11-13 05:03:00,151 [INFO] ============================================================
2025-11-13 05:03:00,253 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:03:00,253 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:03:00,353 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:03:00,753 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:03:00,753 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:03:00,754 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:03:00,754 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:03:00,754 [INFO]    âšª No signal - HOLD
2025-11-13 05:03:01,255 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:03:01,355 [INFO]    Current position: LONG 0.029
2025-11-13 05:03:01,355 [INFO]    Entry: $3474.80 | Mark: $3480.42
2025-11-13 05:03:01,355 [INFO]    PnL: 0.16% ($0.16)
2025-11-13 05:03:01,356 [INFO]    Age: 0.7h / 36.0h
2025-11-13 05:03:01,856 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:03:01,960 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:03:02,467 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:03:02,468 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:03:02,470 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:03:02,470 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:03:02,471 [INFO]    âšª No signal - HOLD
2025-11-13 05:03:02,971 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:03:03,071 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:03:03,438 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:03:03,438 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:03:03,439 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:03:03,439 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:03:03,439 [INFO]    âšª No signal - HOLD
2025-11-13 05:03:03,940 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:03:04,039 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:03:04,405 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:03:04,405 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:03:04,406 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:03:04,406 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:03:04,406 [INFO]    âšª No signal - HOLD
2025-11-13 05:03:04,907 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:03:05,007 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:03:05,471 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:03:05,471 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:03:05,471 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:03:05,472 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:03:05,472 [INFO]    âšª No signal - HOLD
2025-11-13 05:03:05,472 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:04:05,526 [INFO] 
============================================================
2025-11-13 05:04:05,526 [INFO] ðŸ”„ LOOP #15 - 2025-11-13 05:04:05
2025-11-13 05:04:05,526 [INFO] ============================================================
2025-11-13 05:04:06,143 [INFO] ðŸ’“ Bot alive - Loop #15 - Active positions: 1
2025-11-13 05:04:06,252 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:04:06,252 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:04:06,359 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:04:06,753 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:04:06,754 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:04:06,755 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:04:06,755 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:04:06,755 [INFO]    âšª No signal - HOLD
2025-11-13 05:04:07,256 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:04:07,360 [INFO]    Current position: LONG 0.029
2025-11-13 05:04:07,360 [INFO]    Entry: $3474.80 | Mark: $3477.49
2025-11-13 05:04:07,360 [INFO]    PnL: 0.08% ($0.08)
2025-11-13 05:04:07,360 [INFO]    Age: 0.7h / 36.0h
2025-11-13 05:04:07,861 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:04:07,963 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:04:08,425 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:04:08,425 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:04:08,425 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:04:08,426 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:04:08,426 [INFO]    âšª No signal - HOLD
2025-11-13 05:04:08,926 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:04:09,026 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:04:09,406 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:04:09,406 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:04:09,406 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:04:09,407 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:04:09,407 [INFO]    âšª No signal - HOLD
2025-11-13 05:04:09,907 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:04:10,007 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:04:10,377 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:04:10,377 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:04:10,378 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:04:10,378 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:04:10,378 [INFO]    âšª No signal - HOLD
2025-11-13 05:04:10,879 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:04:10,980 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:04:11,354 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:04:11,354 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:04:11,355 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:04:11,355 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:04:11,355 [INFO]    âšª No signal - HOLD
2025-11-13 05:04:11,355 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:05:11,362 [INFO] 
============================================================
2025-11-13 05:05:11,362 [INFO] ðŸ”„ LOOP #16 - 2025-11-13 05:05:11
2025-11-13 05:05:11,362 [INFO] ============================================================
2025-11-13 05:05:11,467 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:05:11,467 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:05:11,567 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:05:11,980 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:05:11,980 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:05:11,981 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:05:11,981 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:05:11,981 [INFO]    âšª No signal - HOLD
2025-11-13 05:05:12,482 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:05:12,585 [INFO]    Current position: LONG 0.029
2025-11-13 05:05:12,585 [INFO]    Entry: $3474.80 | Mark: $3478.20
2025-11-13 05:05:12,585 [INFO]    PnL: 0.10% ($0.10)
2025-11-13 05:05:12,585 [INFO]    Age: 0.7h / 36.0h
2025-11-13 05:05:13,086 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:05:13,188 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:05:13,554 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:05:13,555 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:05:13,556 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:05:13,556 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:05:13,556 [INFO]    âšª No signal - HOLD
2025-11-13 05:05:14,057 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:05:14,159 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:05:14,525 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:05:14,526 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:05:14,526 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:05:14,527 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:05:14,527 [INFO]    âšª No signal - HOLD
2025-11-13 05:05:15,027 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:05:15,131 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:05:15,486 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:05:15,486 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:05:15,486 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:05:15,487 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:05:15,487 [INFO]    âšª No signal - HOLD
2025-11-13 05:05:15,987 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:05:16,087 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:05:16,442 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:05:16,442 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:05:16,443 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:05:16,443 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:05:16,443 [INFO]    âšª No signal - HOLD
2025-11-13 05:05:16,443 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:06:16,477 [INFO] 
============================================================
2025-11-13 05:06:16,478 [INFO] ðŸ”„ LOOP #17 - 2025-11-13 05:06:16
2025-11-13 05:06:16,478 [INFO] ============================================================
2025-11-13 05:06:16,579 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:06:16,580 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:06:16,678 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:06:17,092 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:06:17,093 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:06:17,094 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:06:17,094 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:06:17,094 [INFO]    âšª No signal - HOLD
2025-11-13 05:06:17,595 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:06:17,696 [INFO]    Current position: LONG 0.029
2025-11-13 05:06:17,696 [INFO]    Entry: $3474.80 | Mark: $3473.50
2025-11-13 05:06:17,697 [INFO]    PnL: -0.04% ($-0.04)
2025-11-13 05:06:17,697 [INFO]    Age: 0.7h / 36.0h
2025-11-13 05:06:18,197 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:06:18,299 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:06:18,651 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:06:18,651 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:06:18,651 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:06:18,651 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:06:18,651 [INFO]    âšª No signal - HOLD
2025-11-13 05:06:19,152 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:06:19,257 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:06:19,617 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:06:19,617 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:06:19,618 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:06:19,618 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:06:19,618 [INFO]    âšª No signal - HOLD
2025-11-13 05:06:20,119 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:06:20,220 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:06:20,576 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:06:20,576 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:06:20,576 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:06:20,577 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:06:20,577 [INFO]    âšª No signal - HOLD
2025-11-13 05:06:21,078 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:06:21,180 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:06:21,539 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:06:21,539 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:06:21,540 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:06:21,540 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:06:21,540 [INFO]    âšª No signal - HOLD
2025-11-13 05:06:21,540 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:07:21,600 [INFO] 
============================================================
2025-11-13 05:07:21,601 [INFO] ðŸ”„ LOOP #18 - 2025-11-13 05:07:21
2025-11-13 05:07:21,601 [INFO] ============================================================
2025-11-13 05:07:21,704 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:07:21,705 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:07:21,805 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:07:22,203 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:07:22,204 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:07:22,204 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:07:22,205 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:07:22,205 [INFO]    âšª No signal - HOLD
2025-11-13 05:07:22,705 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:07:22,807 [INFO]    Current position: LONG 0.029
2025-11-13 05:07:22,808 [INFO]    Entry: $3474.80 | Mark: $3475.15
2025-11-13 05:07:22,808 [INFO]    PnL: 0.01% ($0.01)
2025-11-13 05:07:22,808 [INFO]    Age: 0.7h / 36.0h
2025-11-13 05:07:23,309 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:07:23,409 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:07:23,758 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:07:23,758 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:07:23,759 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:07:23,759 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:07:23,759 [INFO]    âšª No signal - HOLD
2025-11-13 05:07:24,260 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:07:24,361 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:07:24,825 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:07:24,825 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:07:24,826 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:07:24,826 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:07:24,826 [INFO]    âšª No signal - HOLD
2025-11-13 05:07:25,327 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:07:25,425 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:07:25,785 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:07:25,785 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:07:25,785 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:07:25,786 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:07:25,786 [INFO]    âšª No signal - HOLD
2025-11-13 05:07:26,286 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:07:26,386 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:07:26,753 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:07:26,753 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:07:26,754 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:07:26,754 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:07:26,754 [INFO]    âšª No signal - HOLD
2025-11-13 05:07:26,754 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:08:26,813 [INFO] 
============================================================
2025-11-13 05:08:26,814 [INFO] ðŸ”„ LOOP #19 - 2025-11-13 05:08:26
2025-11-13 05:08:26,814 [INFO] ============================================================
2025-11-13 05:08:26,918 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:08:26,918 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:08:27,013 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:08:27,397 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:08:27,397 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:08:27,397 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:08:27,398 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:08:27,398 [INFO]    âšª No signal - HOLD
2025-11-13 05:08:27,899 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:08:28,000 [INFO]    Current position: LONG 0.029
2025-11-13 05:08:28,001 [INFO]    Entry: $3474.80 | Mark: $3473.11
2025-11-13 05:08:28,001 [INFO]    PnL: -0.05% ($-0.05)
2025-11-13 05:08:28,001 [INFO]    Age: 0.7h / 36.0h
2025-11-13 05:08:28,502 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:08:28,603 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:08:28,969 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:08:28,969 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:08:28,970 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:08:28,970 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:08:28,970 [INFO]    âšª No signal - HOLD
2025-11-13 05:08:29,471 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:08:29,572 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:08:29,927 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:08:29,927 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:08:29,928 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:08:29,928 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:08:29,928 [INFO]    âšª No signal - HOLD
2025-11-13 05:08:30,429 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:08:30,529 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:08:30,897 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:08:30,897 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:08:30,898 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:08:30,898 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:08:30,898 [INFO]    âšª No signal - HOLD
2025-11-13 05:08:31,399 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:08:31,499 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:08:31,968 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:08:31,968 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:08:31,969 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:08:31,969 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:08:31,969 [INFO]    âšª No signal - HOLD
2025-11-13 05:08:31,969 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:09:32,029 [INFO] 
============================================================
2025-11-13 05:09:32,029 [INFO] ðŸ”„ LOOP #20 - 2025-11-13 05:09:32
2025-11-13 05:09:32,030 [INFO] ============================================================
2025-11-13 05:09:32,721 [INFO] ðŸ’“ Bot alive - Loop #20 - Active positions: 1
2025-11-13 05:09:32,820 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:09:32,820 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:09:33,026 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:09:33,381 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:09:33,381 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:09:33,382 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:09:33,382 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:09:33,382 [INFO]    âšª No signal - HOLD
2025-11-13 05:09:33,883 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:09:33,981 [INFO]    Current position: LONG 0.029
2025-11-13 05:09:33,981 [INFO]    Entry: $3474.80 | Mark: $3471.45
2025-11-13 05:09:33,982 [INFO]    PnL: -0.10% ($-0.10)
2025-11-13 05:09:33,982 [INFO]    Age: 0.8h / 36.0h
2025-11-13 05:09:34,482 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:09:34,584 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:09:34,934 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:09:34,934 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:09:34,935 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:09:34,935 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:09:34,935 [INFO]    âšª No signal - HOLD
2025-11-13 05:09:35,436 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:09:35,539 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:09:35,936 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:09:35,937 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:09:35,937 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:09:35,937 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:09:35,937 [INFO]    âšª No signal - HOLD
2025-11-13 05:09:36,438 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:09:36,538 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:09:36,916 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:09:36,917 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:09:36,917 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:09:36,917 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:09:36,918 [INFO]    âšª No signal - HOLD
2025-11-13 05:09:37,418 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:09:37,528 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:09:37,914 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:09:37,914 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:09:37,915 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:09:37,915 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:09:37,915 [INFO]    âšª No signal - HOLD
2025-11-13 05:09:38,522 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:10:38,562 [INFO] 
============================================================
2025-11-13 05:10:38,562 [INFO] ðŸ”„ LOOP #21 - 2025-11-13 05:10:38
2025-11-13 05:10:38,563 [INFO] ============================================================
2025-11-13 05:10:38,665 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:10:38,665 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:10:38,774 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:10:39,148 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: SHORT
2025-11-13 05:10:39,148 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:10:39,148 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:10:39,148 [INFO]       1. ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:10:39,148 [INFO]       2. âš¡ MACD Death Cross
2025-11-13 05:10:39,149 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.595 | RSI: 43.1 | OB: 0.29
2025-11-13 05:10:39,150 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:10:39,150 [INFO]    ðŸ“ Signal reasons: ðŸ•¯ï¸ Bearish Engulfing, âš¡ MACD Death Cross
2025-11-13 05:10:39,150 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:10:39,150 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:10:39,150 [INFO]    ðŸ“ Top reasons: ðŸ•¯ï¸ Bearish Engulfing, âš¡ MACD Death Cross
2025-11-13 05:10:39,150 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:10:39,256 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 05:10:39,452 [INFO]    ðŸ’µ Current price: $101824.90
2025-11-13 05:10:39,566 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:10:39,567 [INFO]       Balance: $17.84
2025-11-13 05:10:39,567 [INFO]       Price: $101824.90
2025-11-13 05:10:39,567 [INFO]       Capital (fixed): $10.00
2025-11-13 05:10:39,567 [INFO]       Leverage: 10x
2025-11-13 05:10:39,567 [INFO]       Raw quantity: 0.00098208
2025-11-13 05:10:39,567 [INFO]       Formatted quantity: 0.00100000
2025-11-13 05:10:39,567 [INFO]    ðŸ“¤ Placing SELL order for 0.001 BTCUSDT...
2025-11-13 05:10:39,567 [INFO] ðŸ“ Order: SELL BTCUSDT
2025-11-13 05:10:39,567 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 05:10:39,919 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:10:40,659 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:10:40,662 [ERROR]    Symbol: BTCUSDT, Side: SELL, Qty: 0.001
2025-11-13 05:10:41,058 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:10:41,060 [ERROR]    âŒ Order placement failed!
2025-11-13 05:10:41,449 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:10:41,952 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:10:42,054 [INFO]    Current position: LONG 0.029
2025-11-13 05:10:42,054 [INFO]    Entry: $3474.80 | Mark: $3467.80
2025-11-13 05:10:42,054 [INFO]    PnL: -0.20% ($-0.20)
2025-11-13 05:10:42,054 [INFO]    Age: 0.8h / 36.0h
2025-11-13 05:10:42,555 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:10:42,655 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:10:43,039 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:10:43,040 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:10:43,041 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:10:43,041 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:10:43,041 [INFO]    âšª No signal - HOLD
2025-11-13 05:10:43,542 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:10:43,642 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:10:44,110 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:10:44,111 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:10:44,111 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:10:44,112 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:10:44,112 [INFO]    âšª No signal - HOLD
2025-11-13 05:10:44,613 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:10:44,715 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:10:45,089 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:10:45,090 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:10:45,092 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:10:45,092 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:10:45,093 [INFO]    âšª No signal - HOLD
2025-11-13 05:10:45,593 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:10:45,692 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:10:46,034 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:10:46,035 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:10:46,035 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:10:46,035 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:10:46,035 [INFO]    âšª No signal - HOLD
2025-11-13 05:10:46,036 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:11:46,057 [INFO] 
============================================================
2025-11-13 05:11:46,058 [INFO] ðŸ”„ LOOP #22 - 2025-11-13 05:11:46
2025-11-13 05:11:46,058 [INFO] ============================================================
2025-11-13 05:11:46,159 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:11:46,159 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:11:46,258 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:11:46,658 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: SHORT
2025-11-13 05:11:46,659 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:11:46,659 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:11:46,659 [INFO]       1. ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:11:46,659 [INFO]       2. âš¡ MACD Death Cross
2025-11-13 05:11:46,659 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.595 | RSI: 43.3 | OB: 1.33
2025-11-13 05:11:46,659 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:11:46,660 [INFO]    ðŸ“ Signal reasons: ðŸ•¯ï¸ Bearish Engulfing, âš¡ MACD Death Cross
2025-11-13 05:11:46,660 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:11:46,660 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:11:46,660 [INFO]    ðŸ“ Top reasons: ðŸ•¯ï¸ Bearish Engulfing, âš¡ MACD Death Cross
2025-11-13 05:11:46,660 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:11:46,760 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 05:11:46,961 [INFO]    ðŸ’µ Current price: $101849.50
2025-11-13 05:11:46,962 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:11:46,962 [INFO]       Balance: $17.84
2025-11-13 05:11:46,962 [INFO]       Price: $101849.50
2025-11-13 05:11:46,962 [INFO]       Capital (fixed): $10.00
2025-11-13 05:11:46,962 [INFO]       Leverage: 10x
2025-11-13 05:11:46,962 [INFO]       Raw quantity: 0.00098184
2025-11-13 05:11:46,962 [INFO]       Formatted quantity: 0.00100000
2025-11-13 05:11:46,962 [INFO]    ðŸ“¤ Placing SELL order for 0.001 BTCUSDT...
2025-11-13 05:11:46,962 [INFO] ðŸ“ Order: SELL BTCUSDT
2025-11-13 05:11:46,962 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 05:11:47,316 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:11:48,061 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:11:48,063 [ERROR]    Symbol: BTCUSDT, Side: SELL, Qty: 0.001
2025-11-13 05:11:48,483 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:11:48,485 [ERROR]    âŒ Order placement failed!
2025-11-13 05:11:48,892 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:11:49,396 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:11:49,498 [INFO]    Current position: LONG 0.029
2025-11-13 05:11:49,498 [INFO]    Entry: $3474.80 | Mark: $3468.85
2025-11-13 05:11:49,498 [INFO]    PnL: -0.17% ($-0.17)
2025-11-13 05:11:49,498 [INFO]    Age: 0.8h / 36.0h
2025-11-13 05:11:49,999 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:11:50,104 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:11:50,457 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:11:50,457 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:11:50,458 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:11:50,458 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:11:50,458 [INFO]    âšª No signal - HOLD
2025-11-13 05:11:50,959 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:11:51,074 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:11:51,469 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:11:51,470 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:11:51,471 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:11:51,471 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:11:51,471 [INFO]    âšª No signal - HOLD
2025-11-13 05:11:51,972 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:11:52,077 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:11:52,527 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:11:52,527 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:11:52,527 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:11:52,527 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:11:52,527 [INFO]    âšª No signal - HOLD
2025-11-13 05:11:53,028 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:11:53,127 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:11:53,481 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:11:53,481 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:11:53,481 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:11:53,482 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:11:53,482 [INFO]    âšª No signal - HOLD
2025-11-13 05:11:53,482 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:12:53,542 [INFO] 
============================================================
2025-11-13 05:12:53,542 [INFO] ðŸ”„ LOOP #23 - 2025-11-13 05:12:53
2025-11-13 05:12:53,542 [INFO] ============================================================
2025-11-13 05:12:53,643 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:12:53,643 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:12:53,744 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:12:54,153 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: SHORT
2025-11-13 05:12:54,154 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:12:54,154 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:12:54,154 [INFO]       1. ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:12:54,154 [INFO]       2. âš¡ MACD Death Cross
2025-11-13 05:12:54,154 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.598 | RSI: 43.1 | OB: 0.21
2025-11-13 05:12:54,155 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:12:54,155 [INFO]    ðŸ“ Signal reasons: ðŸ•¯ï¸ Bearish Engulfing, âš¡ MACD Death Cross
2025-11-13 05:12:54,155 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:12:54,155 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:12:54,155 [INFO]    ðŸ“ Top reasons: ðŸ•¯ï¸ Bearish Engulfing, âš¡ MACD Death Cross
2025-11-13 05:12:54,155 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:12:54,254 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 05:12:54,453 [INFO]    ðŸ’µ Current price: $101798.30
2025-11-13 05:12:54,453 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:12:54,453 [INFO]       Balance: $17.84
2025-11-13 05:12:54,453 [INFO]       Price: $101798.30
2025-11-13 05:12:54,453 [INFO]       Capital (fixed): $10.00
2025-11-13 05:12:54,453 [INFO]       Leverage: 10x
2025-11-13 05:12:54,454 [INFO]       Raw quantity: 0.00098233
2025-11-13 05:12:54,454 [INFO]       Formatted quantity: 0.00100000
2025-11-13 05:12:54,454 [INFO]    ðŸ“¤ Placing SELL order for 0.001 BTCUSDT...
2025-11-13 05:12:54,454 [INFO] ðŸ“ Order: SELL BTCUSDT
2025-11-13 05:12:54,454 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 05:12:54,812 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:12:55,610 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:12:55,612 [ERROR]    Symbol: BTCUSDT, Side: SELL, Qty: 0.001
2025-11-13 05:12:56,029 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:12:56,031 [ERROR]    âŒ Order placement failed!
2025-11-13 05:12:56,454 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:12:56,957 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:12:57,058 [INFO]    Current position: LONG 0.029
2025-11-13 05:12:57,058 [INFO]    Entry: $3474.80 | Mark: $3466.38
2025-11-13 05:12:57,058 [INFO]    PnL: -0.24% ($-0.24)
2025-11-13 05:12:57,058 [INFO]    Age: 0.8h / 36.0h
2025-11-13 05:12:57,559 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:12:57,661 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:12:58,015 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:12:58,015 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:12:58,016 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:12:58,016 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:12:58,016 [INFO]    âšª No signal - HOLD
2025-11-13 05:12:58,517 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:12:58,620 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:12:58,981 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:12:58,982 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:12:58,982 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:12:58,982 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:12:58,982 [INFO]    âšª No signal - HOLD
2025-11-13 05:12:59,483 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:12:59,585 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:12:59,931 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:12:59,932 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:12:59,932 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:12:59,932 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:12:59,932 [INFO]    âšª No signal - HOLD
2025-11-13 05:13:00,433 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:13:00,534 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:13:00,986 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:13:00,987 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:13:00,988 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:13:00,988 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:13:00,988 [INFO]    âšª No signal - HOLD
2025-11-13 05:13:00,988 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:14:01,021 [INFO] 
============================================================
2025-11-13 05:14:01,021 [INFO] ðŸ”„ LOOP #24 - 2025-11-13 05:14:01
2025-11-13 05:14:01,021 [INFO] ============================================================
2025-11-13 05:14:01,126 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:14:01,127 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:14:01,226 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:14:01,638 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: SHORT
2025-11-13 05:14:01,638 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:14:01,638 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:14:01,638 [INFO]       1. ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:14:01,638 [INFO]       2. âš¡ MACD Death Cross
2025-11-13 05:14:01,639 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.598 | RSI: 42.8 | OB: 2.12
2025-11-13 05:14:01,639 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:14:01,639 [INFO]    ðŸ“ Signal reasons: ðŸ•¯ï¸ Bearish Engulfing, âš¡ MACD Death Cross
2025-11-13 05:14:01,640 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:14:01,640 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:14:01,640 [INFO]    ðŸ“ Top reasons: ðŸ•¯ï¸ Bearish Engulfing, âš¡ MACD Death Cross
2025-11-13 05:14:01,640 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:14:01,741 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 05:14:01,939 [INFO]    ðŸ’µ Current price: $101817.40
2025-11-13 05:14:01,940 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:14:01,940 [INFO]       Balance: $17.84
2025-11-13 05:14:01,940 [INFO]       Price: $101817.40
2025-11-13 05:14:01,940 [INFO]       Capital (fixed): $10.00
2025-11-13 05:14:01,940 [INFO]       Leverage: 10x
2025-11-13 05:14:01,940 [INFO]       Raw quantity: 0.00098215
2025-11-13 05:14:01,940 [INFO]       Formatted quantity: 0.00100000
2025-11-13 05:14:01,940 [INFO]    ðŸ“¤ Placing SELL order for 0.001 BTCUSDT...
2025-11-13 05:14:01,940 [INFO] ðŸ“ Order: SELL BTCUSDT
2025-11-13 05:14:01,940 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 05:14:02,293 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:14:03,168 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:14:03,170 [ERROR]    Symbol: BTCUSDT, Side: SELL, Qty: 0.001
2025-11-13 05:14:03,599 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:14:03,601 [ERROR]    âŒ Order placement failed!
2025-11-13 05:14:04,045 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:14:04,548 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:14:04,651 [INFO]    Current position: LONG 0.029
2025-11-13 05:14:04,651 [INFO]    Entry: $3474.80 | Mark: $3464.85
2025-11-13 05:14:04,652 [INFO]    PnL: -0.29% ($-0.29)
2025-11-13 05:14:04,652 [INFO]    Age: 0.8h / 36.0h
2025-11-13 05:14:05,152 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:14:05,254 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:14:05,610 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:14:05,611 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:14:05,611 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:14:05,611 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:14:05,611 [INFO]    âšª No signal - HOLD
2025-11-13 05:14:06,112 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:14:06,215 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:14:06,613 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:14:06,614 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:14:06,614 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:14:06,615 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:14:06,615 [INFO]    âšª No signal - HOLD
2025-11-13 05:14:07,116 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:14:07,217 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:14:07,596 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:14:07,597 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:14:07,598 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:14:07,598 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:14:07,598 [INFO]    âšª No signal - HOLD
2025-11-13 05:14:08,099 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:14:08,202 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:14:08,574 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:14:08,574 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:14:08,575 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:14:08,575 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:14:08,575 [INFO]    âšª No signal - HOLD
2025-11-13 05:14:08,575 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:15:08,610 [INFO] 
============================================================
2025-11-13 05:15:08,610 [INFO] ðŸ”„ LOOP #25 - 2025-11-13 05:15:08
2025-11-13 05:15:08,610 [INFO] ============================================================
2025-11-13 05:15:09,219 [INFO] ðŸ’“ Bot alive - Loop #25 - Active positions: 1
2025-11-13 05:15:09,323 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:15:09,324 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:15:09,426 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:15:09,892 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:15:09,892 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:15:09,892 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:15:09,892 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:15:09,892 [INFO]    âšª No signal - HOLD
2025-11-13 05:15:10,393 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:15:10,491 [INFO]    Current position: LONG 0.029
2025-11-13 05:15:10,491 [INFO]    Entry: $3474.80 | Mark: $3464.95
2025-11-13 05:15:10,491 [INFO]    PnL: -0.28% ($-0.29)
2025-11-13 05:15:10,491 [INFO]    Age: 0.9h / 36.0h
2025-11-13 05:15:10,992 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:15:11,091 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:15:11,473 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:15:11,474 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:15:11,475 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:15:11,475 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:15:11,475 [INFO]    âšª No signal - HOLD
2025-11-13 05:15:11,977 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:15:12,075 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:15:12,456 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:15:12,457 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:15:12,457 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:15:12,458 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:15:12,458 [INFO]    âšª No signal - HOLD
2025-11-13 05:15:12,959 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:15:13,061 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:15:13,461 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: SHORT
2025-11-13 05:15:13,462 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:15:13,462 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:15:13,462 [INFO]       1. ðŸ“Š Bearish FVG
2025-11-13 05:15:13,462 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:15:13,462 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.529 | RSI: 61.7 | OB: 1.35
2025-11-13 05:15:13,463 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=5
2025-11-13 05:15:13,463 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:15:13,463 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:15:13,463 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:15:13,463 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:15:13,463 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:15:13,561 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:15:13,759 [INFO]    ðŸ’µ Current price: $17.32
2025-11-13 05:15:13,871 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:15:13,871 [INFO]       Balance: $17.84
2025-11-13 05:15:13,871 [INFO]       Price: $17.32
2025-11-13 05:15:13,871 [INFO]       Capital (fixed): $10.00
2025-11-13 05:15:13,871 [INFO]       Leverage: 10x
2025-11-13 05:15:13,871 [INFO]       Raw quantity: 5.77367206
2025-11-13 05:15:13,872 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:15:13,872 [INFO]    ðŸ“¤ Placing SELL order for 6.0 AVAXUSDT...
2025-11-13 05:15:13,872 [INFO] ðŸ“ Order: SELL AVAXUSDT
2025-11-13 05:15:13,872 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:15:14,222 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:15:14,976 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:15:14,978 [ERROR]    Symbol: AVAXUSDT, Side: SELL, Qty: 6.0
2025-11-13 05:15:15,397 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:15:15,399 [ERROR]    âŒ Order placement failed!
2025-11-13 05:15:15,822 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:15:16,325 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:15:16,426 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:15:16,790 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:15:16,790 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:15:16,791 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:15:16,791 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:15:16,791 [INFO]    âšª No signal - HOLD
2025-11-13 05:15:16,791 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:16:16,801 [INFO] 
============================================================
2025-11-13 05:16:16,802 [INFO] ðŸ”„ LOOP #26 - 2025-11-13 05:16:16
2025-11-13 05:16:16,802 [INFO] ============================================================
2025-11-13 05:16:16,905 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:16:16,906 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:16:17,004 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:16:17,389 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:16:17,390 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 05:16:17,390 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:16:17,390 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 05:16:17,390 [INFO]    âšª No signal - HOLD
2025-11-13 05:16:17,891 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:16:17,993 [INFO]    Current position: LONG 0.029
2025-11-13 05:16:17,993 [INFO]    Entry: $3474.80 | Mark: $3469.02
2025-11-13 05:16:17,993 [INFO]    PnL: -0.17% ($-0.17)
2025-11-13 05:16:17,993 [INFO]    Age: 0.9h / 36.0h
2025-11-13 05:16:18,493 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:16:18,591 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:16:18,941 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:16:18,941 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:16:18,942 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:16:18,942 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:16:18,942 [INFO]    âšª No signal - HOLD
2025-11-13 05:16:19,443 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:16:19,546 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:16:20,097 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:16:20,097 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:16:20,098 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:16:20,098 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:16:20,098 [INFO]    âšª No signal - HOLD
2025-11-13 05:16:20,599 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:16:20,699 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:16:21,154 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: SHORT
2025-11-13 05:16:21,154 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:16:21,154 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:16:21,154 [INFO]       1. ðŸ“Š Bearish FVG
2025-11-13 05:16:21,154 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:16:21,154 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.529 | RSI: 61.7 | OB: 1.32
2025-11-13 05:16:21,155 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=5
2025-11-13 05:16:21,155 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:16:21,155 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:16:21,155 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:16:21,155 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:16:21,155 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:16:21,252 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:16:21,446 [INFO]    ðŸ’µ Current price: $17.32
2025-11-13 05:16:21,446 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:16:21,447 [INFO]       Balance: $17.84
2025-11-13 05:16:21,447 [INFO]       Price: $17.32
2025-11-13 05:16:21,447 [INFO]       Capital (fixed): $10.00
2025-11-13 05:16:21,447 [INFO]       Leverage: 10x
2025-11-13 05:16:21,447 [INFO]       Raw quantity: 5.77367206
2025-11-13 05:16:21,447 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:16:21,447 [INFO]    ðŸ“¤ Placing SELL order for 6.0 AVAXUSDT...
2025-11-13 05:16:21,447 [INFO] ðŸ“ Order: SELL AVAXUSDT
2025-11-13 05:16:21,447 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:16:21,796 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:16:22,575 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:16:22,576 [ERROR]    Symbol: AVAXUSDT, Side: SELL, Qty: 6.0
2025-11-13 05:16:23,020 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:16:23,022 [ERROR]    âŒ Order placement failed!
2025-11-13 05:16:23,454 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:16:23,957 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:16:24,059 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:16:24,425 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:16:24,425 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:16:24,426 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:16:24,426 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:16:24,426 [INFO]    âšª No signal - HOLD
2025-11-13 05:16:24,426 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:17:24,454 [INFO] 
============================================================
2025-11-13 05:17:24,454 [INFO] ðŸ”„ LOOP #27 - 2025-11-13 05:17:24
2025-11-13 05:17:24,454 [INFO] ============================================================
2025-11-13 05:17:24,555 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:17:24,556 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:17:24,654 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:17:25,052 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:17:25,052 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 05:17:25,053 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:17:25,053 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 05:17:25,053 [INFO]    âšª No signal - HOLD
2025-11-13 05:17:25,554 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:17:25,655 [INFO]    Current position: LONG 0.029
2025-11-13 05:17:25,655 [INFO]    Entry: $3474.80 | Mark: $3470.33
2025-11-13 05:17:25,655 [INFO]    PnL: -0.13% ($-0.13)
2025-11-13 05:17:25,655 [INFO]    Age: 0.9h / 36.0h
2025-11-13 05:17:26,156 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:17:26,255 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:17:26,601 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:17:26,601 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 05:17:26,602 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:17:26,602 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 05:17:26,602 [INFO]    âšª No signal - HOLD
2025-11-13 05:17:27,103 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:17:27,201 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:17:27,561 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:17:27,561 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:17:27,562 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:17:27,562 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:17:27,562 [INFO]    âšª No signal - HOLD
2025-11-13 05:17:28,063 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:17:28,165 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:17:28,635 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: SHORT
2025-11-13 05:17:28,635 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:17:28,635 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:17:28,635 [INFO]       1. ðŸ“Š Bearish FVG
2025-11-13 05:17:28,636 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:17:28,636 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.528 | RSI: 61.7 | OB: 1.41
2025-11-13 05:17:28,636 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=5
2025-11-13 05:17:28,637 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:17:28,637 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:17:28,637 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:17:28,637 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:17:28,637 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:17:28,735 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:17:28,936 [INFO]    ðŸ’µ Current price: $17.32
2025-11-13 05:17:28,936 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:17:28,936 [INFO]       Balance: $17.84
2025-11-13 05:17:28,937 [INFO]       Price: $17.32
2025-11-13 05:17:28,937 [INFO]       Capital (fixed): $10.00
2025-11-13 05:17:28,937 [INFO]       Leverage: 10x
2025-11-13 05:17:28,937 [INFO]       Raw quantity: 5.77367206
2025-11-13 05:17:28,937 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:17:28,937 [INFO]    ðŸ“¤ Placing SELL order for 6.0 AVAXUSDT...
2025-11-13 05:17:28,937 [INFO] ðŸ“ Order: SELL AVAXUSDT
2025-11-13 05:17:28,937 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:17:29,288 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:17:30,049 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:17:30,052 [ERROR]    Symbol: AVAXUSDT, Side: SELL, Qty: 6.0
2025-11-13 05:17:30,480 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:17:30,481 [ERROR]    âŒ Order placement failed!
2025-11-13 05:17:30,902 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:17:31,405 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:17:31,507 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:17:31,858 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:17:31,858 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:17:31,859 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:17:31,859 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:17:31,859 [INFO]    âšª No signal - HOLD
2025-11-13 05:17:31,859 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:18:31,920 [INFO] 
============================================================
2025-11-13 05:18:31,920 [INFO] ðŸ”„ LOOP #28 - 2025-11-13 05:18:31
2025-11-13 05:18:31,920 [INFO] ============================================================
2025-11-13 05:18:32,023 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:18:32,023 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:18:32,124 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:18:32,535 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:18:32,535 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:18:32,536 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:18:32,536 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:18:32,536 [INFO]    âšª No signal - HOLD
2025-11-13 05:18:33,037 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:18:33,137 [INFO]    Current position: LONG 0.029
2025-11-13 05:18:33,137 [INFO]    Entry: $3474.80 | Mark: $3475.43
2025-11-13 05:18:33,137 [INFO]    PnL: 0.02% ($0.02)
2025-11-13 05:18:33,137 [INFO]    Age: 0.9h / 36.0h
2025-11-13 05:18:33,638 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:18:33,739 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:18:34,100 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:18:34,100 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:18:34,101 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:18:34,101 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:18:34,101 [INFO]    âšª No signal - HOLD
2025-11-13 05:18:34,602 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:18:34,706 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:18:35,049 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:18:35,049 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:18:35,049 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:18:35,050 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:18:35,050 [INFO]    âšª No signal - HOLD
2025-11-13 05:18:35,550 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:18:35,656 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:18:36,108 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: SHORT
2025-11-13 05:18:36,108 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:18:36,109 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:18:36,109 [INFO]       1. ðŸ“Š Bearish FVG
2025-11-13 05:18:36,109 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:18:36,109 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.529 | RSI: 61.7 | OB: 1.37
2025-11-13 05:18:36,109 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=5
2025-11-13 05:18:36,109 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:18:36,109 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:18:36,110 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:18:36,110 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:18:36,110 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:18:36,209 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:18:36,500 [INFO]    ðŸ’µ Current price: $17.32
2025-11-13 05:18:36,501 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:18:36,501 [INFO]       Balance: $17.84
2025-11-13 05:18:36,501 [INFO]       Price: $17.32
2025-11-13 05:18:36,501 [INFO]       Capital (fixed): $10.00
2025-11-13 05:18:36,501 [INFO]       Leverage: 10x
2025-11-13 05:18:36,501 [INFO]       Raw quantity: 5.77367206
2025-11-13 05:18:36,501 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:18:36,501 [INFO]    ðŸ“¤ Placing SELL order for 6.0 AVAXUSDT...
2025-11-13 05:18:36,501 [INFO] ðŸ“ Order: SELL AVAXUSDT
2025-11-13 05:18:36,501 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:18:36,851 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:18:37,692 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:18:37,694 [ERROR]    Symbol: AVAXUSDT, Side: SELL, Qty: 6.0
2025-11-13 05:18:38,151 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:18:38,153 [ERROR]    âŒ Order placement failed!
2025-11-13 05:18:38,625 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:18:39,128 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:18:39,228 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:18:39,679 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:18:39,679 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:18:39,679 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:18:39,679 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:18:39,679 [INFO]    âšª No signal - HOLD
2025-11-13 05:18:39,680 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:19:39,740 [INFO] 
============================================================
2025-11-13 05:19:39,740 [INFO] ðŸ”„ LOOP #29 - 2025-11-13 05:19:39
2025-11-13 05:19:39,740 [INFO] ============================================================
2025-11-13 05:19:39,844 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:19:39,844 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:19:39,944 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:19:40,334 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:19:40,334 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:19:40,334 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:19:40,334 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:19:40,335 [INFO]    âšª No signal - HOLD
2025-11-13 05:19:40,835 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:19:40,935 [INFO]    Current position: LONG 0.029
2025-11-13 05:19:40,935 [INFO]    Entry: $3474.80 | Mark: $3473.43
2025-11-13 05:19:40,935 [INFO]    PnL: -0.04% ($-0.04)
2025-11-13 05:19:40,935 [INFO]    Age: 0.9h / 36.0h
2025-11-13 05:19:41,436 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:19:41,536 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:19:41,928 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:19:41,928 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:19:41,929 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:19:41,930 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:19:41,930 [INFO]    âšª No signal - HOLD
2025-11-13 05:19:42,431 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:19:42,533 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:19:42,947 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:19:42,947 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:19:42,948 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:19:42,949 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:19:42,949 [INFO]    âšª No signal - HOLD
2025-11-13 05:19:43,450 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:19:43,553 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:19:43,912 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: SHORT
2025-11-13 05:19:43,913 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:19:43,913 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:19:43,913 [INFO]       1. ðŸ“Š Bearish FVG
2025-11-13 05:19:43,913 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:19:43,913 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.529 | RSI: 61.7 | OB: 1.40
2025-11-13 05:19:43,914 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=5
2025-11-13 05:19:43,914 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:19:43,914 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:19:43,914 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:19:43,914 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:19:43,914 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:19:44,010 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:19:44,212 [INFO]    ðŸ’µ Current price: $17.32
2025-11-13 05:19:44,212 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:19:44,212 [INFO]       Balance: $17.84
2025-11-13 05:19:44,212 [INFO]       Price: $17.32
2025-11-13 05:19:44,212 [INFO]       Capital (fixed): $10.00
2025-11-13 05:19:44,212 [INFO]       Leverage: 10x
2025-11-13 05:19:44,212 [INFO]       Raw quantity: 5.77367206
2025-11-13 05:19:44,212 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:19:44,212 [INFO]    ðŸ“¤ Placing SELL order for 6.0 AVAXUSDT...
2025-11-13 05:19:44,212 [INFO] ðŸ“ Order: SELL AVAXUSDT
2025-11-13 05:19:44,212 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:19:44,564 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:19:45,334 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:19:45,336 [ERROR]    Symbol: AVAXUSDT, Side: SELL, Qty: 6.0
2025-11-13 05:19:45,773 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:19:45,775 [ERROR]    âŒ Order placement failed!
2025-11-13 05:19:46,143 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:19:46,646 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:19:46,747 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:19:47,130 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:19:47,130 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 05:19:47,130 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:19:47,130 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 05:19:47,130 [INFO]    âšª No signal - HOLD
2025-11-13 05:19:47,131 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:20:47,165 [INFO] 
============================================================
2025-11-13 05:20:47,166 [INFO] ðŸ”„ LOOP #30 - 2025-11-13 05:20:47
2025-11-13 05:20:47,166 [INFO] ============================================================
2025-11-13 05:20:47,793 [INFO] ðŸ’“ Bot alive - Loop #30 - Active positions: 1
2025-11-13 05:20:47,894 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:20:47,894 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:20:47,993 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:20:48,367 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:20:48,367 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:20:48,368 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:20:48,368 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:20:48,368 [INFO]    âšª No signal - HOLD
2025-11-13 05:20:48,869 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:20:48,970 [INFO]    Current position: LONG 0.029
2025-11-13 05:20:48,970 [INFO]    Entry: $3474.80 | Mark: $3474.60
2025-11-13 05:20:48,970 [INFO]    PnL: -0.01% ($-0.01)
2025-11-13 05:20:48,970 [INFO]    Age: 1.0h / 36.0h
2025-11-13 05:20:49,471 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:20:49,570 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:20:49,944 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:20:49,944 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:20:49,946 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:20:49,946 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:20:49,946 [INFO]    âšª No signal - HOLD
2025-11-13 05:20:50,447 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:20:50,548 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:20:50,900 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:20:50,900 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:20:50,901 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:20:50,901 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:20:50,901 [INFO]    âšª No signal - HOLD
2025-11-13 05:20:51,402 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:20:51,503 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:20:51,866 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: SHORT
2025-11-13 05:20:51,866 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:20:51,866 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:20:51,866 [INFO]       1. ðŸ“Š Bearish FVG
2025-11-13 05:20:51,866 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:20:51,866 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.528 | RSI: 61.7 | OB: 1.45
2025-11-13 05:20:51,867 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=5
2025-11-13 05:20:51,867 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:20:51,868 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:20:51,868 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:20:51,868 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:20:51,868 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:20:51,968 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:20:52,168 [INFO]    ðŸ’µ Current price: $17.32
2025-11-13 05:20:52,169 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:20:52,169 [INFO]       Balance: $17.84
2025-11-13 05:20:52,169 [INFO]       Price: $17.32
2025-11-13 05:20:52,169 [INFO]       Capital (fixed): $10.00
2025-11-13 05:20:52,169 [INFO]       Leverage: 10x
2025-11-13 05:20:52,169 [INFO]       Raw quantity: 5.77367206
2025-11-13 05:20:52,169 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:20:52,169 [INFO]    ðŸ“¤ Placing SELL order for 6.0 AVAXUSDT...
2025-11-13 05:20:52,169 [INFO] ðŸ“ Order: SELL AVAXUSDT
2025-11-13 05:20:52,169 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:20:52,520 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:20:53,270 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:20:53,272 [ERROR]    Symbol: AVAXUSDT, Side: SELL, Qty: 6.0
2025-11-13 05:20:53,708 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:20:53,710 [ERROR]    âŒ Order placement failed!
2025-11-13 05:20:54,125 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:20:54,628 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:20:54,726 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:20:55,075 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:20:55,075 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:20:55,075 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:20:55,075 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:20:55,075 [INFO]    âšª No signal - HOLD
2025-11-13 05:20:55,871 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:21:55,929 [INFO] 
============================================================
2025-11-13 05:21:55,930 [INFO] ðŸ”„ LOOP #31 - 2025-11-13 05:21:55
2025-11-13 05:21:55,931 [INFO] ============================================================
2025-11-13 05:21:56,031 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:21:56,031 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:21:56,131 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:21:56,521 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:21:56,522 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:21:56,522 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:21:56,524 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:21:56,524 [INFO]    âšª No signal - HOLD
2025-11-13 05:21:57,025 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:21:57,129 [INFO]    Current position: LONG 0.029
2025-11-13 05:21:57,129 [INFO]    Entry: $3474.80 | Mark: $3477.60
2025-11-13 05:21:57,129 [INFO]    PnL: 0.08% ($0.08)
2025-11-13 05:21:57,129 [INFO]    Age: 1.0h / 36.0h
2025-11-13 05:21:57,630 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:21:57,730 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:21:58,092 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:21:58,092 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:21:58,092 [INFO]    ðŸ“ Signal reasons: ðŸ•¯ï¸ Bullish Engulfing, ðŸ”· Bullish Order Block
2025-11-13 05:21:58,092 [INFO]    âšª No signal - HOLD
2025-11-13 05:21:58,593 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:21:58,694 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:21:59,083 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:21:59,083 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:21:59,084 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:21:59,084 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:21:59,085 [INFO]    âšª No signal - HOLD
2025-11-13 05:21:59,585 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:21:59,686 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:22:00,069 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: SHORT
2025-11-13 05:22:00,069 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:22:00,069 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:22:00,069 [INFO]       1. ðŸ“Š Bearish FVG
2025-11-13 05:22:00,069 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:22:00,069 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.528 | RSI: 61.7 | OB: 1.45
2025-11-13 05:22:00,070 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=5
2025-11-13 05:22:00,070 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:22:00,070 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:22:00,070 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:22:00,070 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:22:00,070 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:22:00,275 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:22:00,479 [INFO]    ðŸ’µ Current price: $17.32
2025-11-13 05:22:00,479 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:22:00,479 [INFO]       Balance: $17.84
2025-11-13 05:22:00,482 [INFO]       Price: $17.32
2025-11-13 05:22:00,483 [INFO]       Capital (fixed): $10.00
2025-11-13 05:22:00,483 [INFO]       Leverage: 10x
2025-11-13 05:22:00,483 [INFO]       Raw quantity: 5.77367206
2025-11-13 05:22:00,483 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:22:00,483 [INFO]    ðŸ“¤ Placing SELL order for 6.0 AVAXUSDT...
2025-11-13 05:22:00,483 [INFO] ðŸ“ Order: SELL AVAXUSDT
2025-11-13 05:22:00,483 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:22:00,837 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:22:01,678 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:22:01,680 [ERROR]    Symbol: AVAXUSDT, Side: SELL, Qty: 6.0
2025-11-13 05:22:02,140 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:22:02,142 [ERROR]    âŒ Order placement failed!
2025-11-13 05:22:02,591 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:22:03,093 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:22:03,201 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:22:03,562 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:22:03,563 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:22:03,563 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:22:03,564 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:22:03,564 [INFO]    âšª No signal - HOLD
2025-11-13 05:22:03,564 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:23:03,617 [INFO] 
============================================================
2025-11-13 05:23:03,618 [INFO] ðŸ”„ LOOP #32 - 2025-11-13 05:23:03
2025-11-13 05:23:03,618 [INFO] ============================================================
2025-11-13 05:23:03,719 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:23:03,719 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:23:03,819 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:23:04,214 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:23:04,214 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:23:04,215 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:23:04,215 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:23:04,215 [INFO]    âšª No signal - HOLD
2025-11-13 05:23:04,716 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:23:04,876 [INFO]    Current position: LONG 0.029
2025-11-13 05:23:04,876 [INFO]    Entry: $3474.80 | Mark: $3476.85
2025-11-13 05:23:04,876 [INFO]    PnL: 0.06% ($0.06)
2025-11-13 05:23:04,876 [INFO]    Age: 1.0h / 36.0h
2025-11-13 05:23:05,377 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:23:05,477 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:23:05,843 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:23:05,843 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:23:05,844 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:23:05,844 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:23:05,844 [INFO]    âšª No signal - HOLD
2025-11-13 05:23:06,345 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:23:06,444 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:23:06,802 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:23:06,802 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:23:06,802 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:23:06,803 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:23:06,803 [INFO]    âšª No signal - HOLD
2025-11-13 05:23:07,303 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:23:07,400 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:23:07,748 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: SHORT
2025-11-13 05:23:07,748 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:23:07,748 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:23:07,748 [INFO]       1. ðŸ“Š Bearish FVG
2025-11-13 05:23:07,748 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:23:07,748 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.576 | RSI: 61.7 | OB: 1.47
2025-11-13 05:23:07,749 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=5
2025-11-13 05:23:07,749 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:23:07,749 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:23:07,749 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:23:07,749 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:23:07,749 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:23:07,951 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:23:08,153 [INFO]    ðŸ’µ Current price: $17.32
2025-11-13 05:23:08,154 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:23:08,154 [INFO]       Balance: $17.84
2025-11-13 05:23:08,154 [INFO]       Price: $17.32
2025-11-13 05:23:08,154 [INFO]       Capital (fixed): $10.00
2025-11-13 05:23:08,154 [INFO]       Leverage: 10x
2025-11-13 05:23:08,154 [INFO]       Raw quantity: 5.77367206
2025-11-13 05:23:08,154 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:23:08,154 [INFO]    ðŸ“¤ Placing SELL order for 6.0 AVAXUSDT...
2025-11-13 05:23:08,154 [INFO] ðŸ“ Order: SELL AVAXUSDT
2025-11-13 05:23:08,154 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:23:08,608 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:23:09,431 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:23:09,432 [ERROR]    Symbol: AVAXUSDT, Side: SELL, Qty: 6.0
2025-11-13 05:23:09,877 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:23:09,879 [ERROR]    âŒ Order placement failed!
2025-11-13 05:23:10,319 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:23:10,821 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:23:10,920 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:23:11,279 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:23:11,279 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:23:11,279 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:23:11,279 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:23:11,279 [INFO]    âšª No signal - HOLD
2025-11-13 05:23:11,279 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:24:11,340 [INFO] 
============================================================
2025-11-13 05:24:11,340 [INFO] ðŸ”„ LOOP #33 - 2025-11-13 05:24:11
2025-11-13 05:24:11,340 [INFO] ============================================================
2025-11-13 05:24:11,442 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:24:11,442 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:24:11,544 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:24:11,959 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:24:11,960 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:24:11,960 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:24:11,961 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:24:11,961 [INFO]    âšª No signal - HOLD
2025-11-13 05:24:12,461 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:24:12,563 [INFO]    Current position: LONG 0.029
2025-11-13 05:24:12,563 [INFO]    Entry: $3474.80 | Mark: $3477.20
2025-11-13 05:24:12,563 [INFO]    PnL: 0.07% ($0.07)
2025-11-13 05:24:12,564 [INFO]    Age: 1.0h / 36.0h
2025-11-13 05:24:13,064 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:24:13,167 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:24:13,653 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:24:13,654 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:24:13,654 [INFO]    ðŸ“ Signal reasons: ðŸ•¯ï¸ Bullish Engulfing, ðŸ”· Bullish Order Block
2025-11-13 05:24:13,654 [INFO]    âšª No signal - HOLD
2025-11-13 05:24:14,155 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:24:14,258 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:24:14,607 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:24:14,607 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:24:14,607 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:24:14,608 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:24:14,608 [INFO]    âšª No signal - HOLD
2025-11-13 05:24:15,108 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:24:15,207 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:24:15,657 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: SHORT
2025-11-13 05:24:15,657 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:24:15,658 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:24:15,658 [INFO]       1. ðŸ“Š Bearish FVG
2025-11-13 05:24:15,658 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:24:15,658 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.575 | RSI: 62.2 | OB: 1.42
2025-11-13 05:24:15,658 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=5
2025-11-13 05:24:15,659 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:24:15,659 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:24:15,659 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:24:15,659 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:24:15,659 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:24:15,755 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:24:15,953 [INFO]    ðŸ’µ Current price: $17.34
2025-11-13 05:24:15,954 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:24:15,954 [INFO]       Balance: $17.84
2025-11-13 05:24:15,954 [INFO]       Price: $17.34
2025-11-13 05:24:15,954 [INFO]       Capital (fixed): $10.00
2025-11-13 05:24:15,954 [INFO]       Leverage: 10x
2025-11-13 05:24:15,954 [INFO]       Raw quantity: 5.76701269
2025-11-13 05:24:15,954 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:24:15,954 [INFO]    ðŸ“¤ Placing SELL order for 6.0 AVAXUSDT...
2025-11-13 05:24:15,954 [INFO] ðŸ“ Order: SELL AVAXUSDT
2025-11-13 05:24:15,954 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:24:16,304 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:24:17,077 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:24:17,079 [ERROR]    Symbol: AVAXUSDT, Side: SELL, Qty: 6.0
2025-11-13 05:24:17,462 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:24:17,464 [ERROR]    âŒ Order placement failed!
2025-11-13 05:24:17,856 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:24:18,359 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:24:18,464 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:24:18,843 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:24:18,843 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:24:18,844 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:24:18,844 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:24:18,844 [INFO]    âšª No signal - HOLD
2025-11-13 05:24:18,844 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:25:18,898 [INFO] 
============================================================
2025-11-13 05:25:18,898 [INFO] ðŸ”„ LOOP #34 - 2025-11-13 05:25:18
2025-11-13 05:25:18,898 [INFO] ============================================================
2025-11-13 05:25:18,999 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:25:18,999 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:25:19,096 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:25:19,484 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:25:19,484 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:25:19,484 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:25:19,485 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:25:19,485 [INFO]    âšª No signal - HOLD
2025-11-13 05:25:19,985 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:25:20,085 [INFO]    Current position: LONG 0.029
2025-11-13 05:25:20,085 [INFO]    Entry: $3474.80 | Mark: $3474.41
2025-11-13 05:25:20,085 [INFO]    PnL: -0.01% ($-0.01)
2025-11-13 05:25:20,086 [INFO]    Age: 1.0h / 36.0h
2025-11-13 05:25:20,586 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:25:20,685 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:25:21,034 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:25:21,034 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:25:21,035 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:25:21,035 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:25:21,035 [INFO]    âšª No signal - HOLD
2025-11-13 05:25:21,536 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:25:21,635 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:25:21,996 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:25:21,997 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:25:21,997 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:25:21,997 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:25:21,998 [INFO]    âšª No signal - HOLD
2025-11-13 05:25:22,498 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:25:22,599 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:25:22,954 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: SHORT
2025-11-13 05:25:22,955 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:25:22,955 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:25:22,955 [INFO]       1. ðŸ“Š Bearish FVG
2025-11-13 05:25:22,955 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:25:22,955 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.575 | RSI: 62.2 | OB: 1.40
2025-11-13 05:25:22,956 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=5
2025-11-13 05:25:22,956 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:25:22,956 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:25:22,956 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:25:22,956 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:25:22,956 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:25:23,153 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:25:23,389 [INFO]    ðŸ’µ Current price: $17.34
2025-11-13 05:25:23,389 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:25:23,390 [INFO]       Balance: $17.84
2025-11-13 05:25:23,390 [INFO]       Price: $17.34
2025-11-13 05:25:23,390 [INFO]       Capital (fixed): $10.00
2025-11-13 05:25:23,390 [INFO]       Leverage: 10x
2025-11-13 05:25:23,390 [INFO]       Raw quantity: 5.76701269
2025-11-13 05:25:23,390 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:25:23,390 [INFO]    ðŸ“¤ Placing SELL order for 6.0 AVAXUSDT...
2025-11-13 05:25:23,390 [INFO] ðŸ“ Order: SELL AVAXUSDT
2025-11-13 05:25:23,390 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:25:23,741 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:25:24,604 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:25:24,606 [ERROR]    Symbol: AVAXUSDT, Side: SELL, Qty: 6.0
2025-11-13 05:25:25,051 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:25:25,053 [ERROR]    âŒ Order placement failed!
2025-11-13 05:25:25,488 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:25:25,991 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:25:26,097 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:25:26,483 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:25:26,483 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:25:26,484 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:25:26,484 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:25:26,484 [INFO]    âšª No signal - HOLD
2025-11-13 05:25:26,484 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:26:26,530 [INFO] 
============================================================
2025-11-13 05:26:26,530 [INFO] ðŸ”„ LOOP #35 - 2025-11-13 05:26:26
2025-11-13 05:26:26,530 [INFO] ============================================================
2025-11-13 05:26:27,135 [INFO] ðŸ’“ Bot alive - Loop #35 - Active positions: 1
2025-11-13 05:26:27,241 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:26:27,241 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:26:27,343 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:26:27,703 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:26:27,709 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:26:27,709 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, âš¡ MACD Golden Cross
2025-11-13 05:26:27,709 [INFO]    âšª No signal - HOLD
2025-11-13 05:26:28,210 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:26:28,318 [INFO]    Current position: LONG 0.029
2025-11-13 05:26:28,318 [INFO]    Entry: $3474.80 | Mark: $3478.43
2025-11-13 05:26:28,318 [INFO]    PnL: 0.10% ($0.11)
2025-11-13 05:26:28,318 [INFO]    Age: 1.0h / 36.0h
2025-11-13 05:26:28,819 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:26:28,921 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:26:29,410 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:26:29,411 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:26:29,411 [INFO]    ðŸ“ Signal reasons: ðŸ•¯ï¸ Bullish Engulfing, ðŸ”· Bullish Order Block
2025-11-13 05:26:29,411 [INFO]    âšª No signal - HOLD
2025-11-13 05:26:29,912 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:26:30,114 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:26:30,464 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:26:30,465 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:26:30,465 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:26:30,465 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:26:30,465 [INFO]    âšª No signal - HOLD
2025-11-13 05:26:30,966 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:26:31,068 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:26:31,439 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: SHORT
2025-11-13 05:26:31,439 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:26:31,439 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:26:31,439 [INFO]       1. ðŸ“Š Bearish FVG
2025-11-13 05:26:31,439 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:26:31,439 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.575 | RSI: 62.2 | OB: 1.46
2025-11-13 05:26:31,440 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=5
2025-11-13 05:26:31,440 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:26:31,440 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:26:31,440 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:26:31,440 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:26:31,440 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:26:31,540 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:26:31,844 [INFO]    ðŸ’µ Current price: $17.34
2025-11-13 05:26:31,844 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:26:31,844 [INFO]       Balance: $17.84
2025-11-13 05:26:31,844 [INFO]       Price: $17.34
2025-11-13 05:26:31,844 [INFO]       Capital (fixed): $10.00
2025-11-13 05:26:31,845 [INFO]       Leverage: 10x
2025-11-13 05:26:31,845 [INFO]       Raw quantity: 5.76701269
2025-11-13 05:26:31,845 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:26:31,845 [INFO]    ðŸ“¤ Placing SELL order for 6.0 AVAXUSDT...
2025-11-13 05:26:31,845 [INFO] ðŸ“ Order: SELL AVAXUSDT
2025-11-13 05:26:31,845 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:26:32,196 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:26:33,037 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:26:33,039 [ERROR]    Symbol: AVAXUSDT, Side: SELL, Qty: 6.0
2025-11-13 05:26:33,466 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:26:33,469 [ERROR]    âŒ Order placement failed!
2025-11-13 05:26:33,901 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:26:34,404 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:26:34,506 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:26:34,874 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:26:34,875 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:26:34,875 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:26:34,876 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:26:34,876 [INFO]    âšª No signal - HOLD
2025-11-13 05:26:34,876 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:27:34,882 [INFO] 
============================================================
2025-11-13 05:27:34,882 [INFO] ðŸ”„ LOOP #36 - 2025-11-13 05:27:34
2025-11-13 05:27:34,882 [INFO] ============================================================
2025-11-13 05:27:34,986 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:27:34,987 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:27:35,089 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:27:35,485 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:27:35,486 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:27:35,486 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, âš¡ MACD Golden Cross
2025-11-13 05:27:35,486 [INFO]    âšª No signal - HOLD
2025-11-13 05:27:35,987 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:27:36,086 [INFO]    Current position: LONG 0.029
2025-11-13 05:27:36,086 [INFO]    Entry: $3474.80 | Mark: $3479.68
2025-11-13 05:27:36,086 [INFO]    PnL: 0.14% ($0.14)
2025-11-13 05:27:36,086 [INFO]    Age: 1.1h / 36.0h
2025-11-13 05:27:36,587 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:27:36,687 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:27:37,064 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:27:37,065 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:27:37,065 [INFO]    ðŸ“ Signal reasons: ðŸ•¯ï¸ Bullish Engulfing, ðŸ”· Bullish Order Block
2025-11-13 05:27:37,065 [INFO]    âšª No signal - HOLD
2025-11-13 05:27:37,566 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:27:37,667 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:27:38,028 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:27:38,028 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:27:38,029 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:27:38,029 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:27:38,029 [INFO]    âšª No signal - HOLD
2025-11-13 05:27:38,529 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:27:38,631 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:27:39,024 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: SHORT
2025-11-13 05:27:39,024 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:27:39,024 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:27:39,024 [INFO]       1. ðŸ“Š Bearish FVG
2025-11-13 05:27:39,024 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:27:39,025 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.575 | RSI: 62.2 | OB: 1.51
2025-11-13 05:27:39,025 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=5
2025-11-13 05:27:39,026 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:27:39,026 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:27:39,026 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:27:39,026 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:27:39,026 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:27:39,126 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:27:39,423 [INFO]    ðŸ’µ Current price: $17.34
2025-11-13 05:27:39,423 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:27:39,423 [INFO]       Balance: $17.84
2025-11-13 05:27:39,423 [INFO]       Price: $17.34
2025-11-13 05:27:39,423 [INFO]       Capital (fixed): $10.00
2025-11-13 05:27:39,423 [INFO]       Leverage: 10x
2025-11-13 05:27:39,423 [INFO]       Raw quantity: 5.76701269
2025-11-13 05:27:39,423 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:27:39,423 [INFO]    ðŸ“¤ Placing SELL order for 6.0 AVAXUSDT...
2025-11-13 05:27:39,424 [INFO] ðŸ“ Order: SELL AVAXUSDT
2025-11-13 05:27:39,424 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:27:39,876 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:27:40,810 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:27:40,812 [ERROR]    Symbol: AVAXUSDT, Side: SELL, Qty: 6.0
2025-11-13 05:27:41,285 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:27:41,286 [ERROR]    âŒ Order placement failed!
2025-11-13 05:27:41,761 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:27:42,263 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:27:42,371 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:27:42,769 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:27:42,769 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:27:42,770 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:27:42,770 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:27:42,770 [INFO]    âšª No signal - HOLD
2025-11-13 05:27:42,770 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:28:42,818 [INFO] 
============================================================
2025-11-13 05:28:42,819 [INFO] ðŸ”„ LOOP #37 - 2025-11-13 05:28:42
2025-11-13 05:28:42,819 [INFO] ============================================================
2025-11-13 05:28:42,922 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:28:42,922 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:28:43,024 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:28:43,410 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:28:43,411 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:28:43,411 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, âš¡ MACD Golden Cross
2025-11-13 05:28:43,411 [INFO]    âšª No signal - HOLD
2025-11-13 05:28:43,912 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:28:44,042 [INFO]    Current position: LONG 0.029
2025-11-13 05:28:44,043 [INFO]    Entry: $3474.80 | Mark: $3480.07
2025-11-13 05:28:44,043 [INFO]    PnL: 0.15% ($0.15)
2025-11-13 05:28:44,043 [INFO]    Age: 1.1h / 36.0h
2025-11-13 05:28:44,544 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:28:44,643 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:28:45,000 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:28:45,001 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:28:45,002 [INFO]    ðŸ“ Signal reasons: ðŸ•¯ï¸ Bullish Engulfing, ðŸ”· Bullish Order Block
2025-11-13 05:28:45,002 [INFO]    âšª No signal - HOLD
2025-11-13 05:28:45,503 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:28:45,649 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:28:46,007 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:28:46,007 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:28:46,007 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:28:46,007 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:28:46,007 [INFO]    âšª No signal - HOLD
2025-11-13 05:28:46,508 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:28:46,714 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:28:47,097 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: SHORT
2025-11-13 05:28:47,097 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:28:47,097 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:28:47,097 [INFO]       1. ðŸ“Š Bearish FVG
2025-11-13 05:28:47,097 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:28:47,098 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.575 | RSI: 62.5 | OB: 1.48
2025-11-13 05:28:47,098 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=5
2025-11-13 05:28:47,098 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:28:47,098 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:28:47,099 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:28:47,099 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:28:47,099 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:28:47,198 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:28:47,393 [INFO]    ðŸ’µ Current price: $17.35
2025-11-13 05:28:47,394 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:28:47,394 [INFO]       Balance: $17.84
2025-11-13 05:28:47,394 [INFO]       Price: $17.35
2025-11-13 05:28:47,394 [INFO]       Capital (fixed): $10.00
2025-11-13 05:28:47,394 [INFO]       Leverage: 10x
2025-11-13 05:28:47,394 [INFO]       Raw quantity: 5.76368876
2025-11-13 05:28:47,394 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:28:47,394 [INFO]    ðŸ“¤ Placing SELL order for 6.0 AVAXUSDT...
2025-11-13 05:28:47,394 [INFO] ðŸ“ Order: SELL AVAXUSDT
2025-11-13 05:28:47,394 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:28:47,843 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:28:48,591 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:28:48,593 [ERROR]    Symbol: AVAXUSDT, Side: SELL, Qty: 6.0
2025-11-13 05:28:49,029 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:28:49,031 [ERROR]    âŒ Order placement failed!
2025-11-13 05:28:49,451 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:28:49,953 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:28:50,052 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:28:50,414 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:28:50,415 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:28:50,415 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:28:50,415 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:28:50,415 [INFO]    âšª No signal - HOLD
2025-11-13 05:28:50,415 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:29:50,473 [INFO] 
============================================================
2025-11-13 05:29:50,473 [INFO] ðŸ”„ LOOP #38 - 2025-11-13 05:29:50
2025-11-13 05:29:50,473 [INFO] ============================================================
2025-11-13 05:29:50,581 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:29:50,581 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:29:50,682 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:29:51,082 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:29:51,083 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:29:51,083 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, âš¡ MACD Golden Cross
2025-11-13 05:29:51,083 [INFO]    âšª No signal - HOLD
2025-11-13 05:29:51,584 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:29:51,686 [INFO]    Current position: LONG 0.029
2025-11-13 05:29:51,686 [INFO]    Entry: $3474.80 | Mark: $3482.80
2025-11-13 05:29:51,686 [INFO]    PnL: 0.23% ($0.23)
2025-11-13 05:29:51,686 [INFO]    Age: 1.1h / 36.0h
2025-11-13 05:29:52,187 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:29:52,289 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:29:52,663 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:29:52,663 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:29:52,663 [INFO]    ðŸ“ Signal reasons: ðŸ•¯ï¸ Bullish Engulfing, ðŸ”· Bullish Order Block
2025-11-13 05:29:52,663 [INFO]    âšª No signal - HOLD
2025-11-13 05:29:53,164 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:29:53,266 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:29:53,615 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:29:53,616 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:29:53,616 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:29:53,616 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:29:53,616 [INFO]    âšª No signal - HOLD
2025-11-13 05:29:54,117 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:29:54,220 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:29:54,579 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: SHORT
2025-11-13 05:29:54,580 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:29:54,580 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:29:54,580 [INFO]       1. ðŸ“Š Bearish FVG
2025-11-13 05:29:54,580 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:29:54,580 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.575 | RSI: 62.5 | OB: 1.48
2025-11-13 05:29:54,580 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=5
2025-11-13 05:29:54,581 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:29:54,581 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:29:54,581 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:29:54,581 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bearish FVG, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:29:54,581 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:29:54,681 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:29:54,979 [INFO]    ðŸ’µ Current price: $17.35
2025-11-13 05:29:54,980 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:29:54,980 [INFO]       Balance: $17.84
2025-11-13 05:29:54,980 [INFO]       Price: $17.35
2025-11-13 05:29:54,980 [INFO]       Capital (fixed): $10.00
2025-11-13 05:29:54,980 [INFO]       Leverage: 10x
2025-11-13 05:29:54,980 [INFO]       Raw quantity: 5.76368876
2025-11-13 05:29:54,980 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:29:54,980 [INFO]    ðŸ“¤ Placing SELL order for 6.0 AVAXUSDT...
2025-11-13 05:29:54,980 [INFO] ðŸ“ Order: SELL AVAXUSDT
2025-11-13 05:29:54,980 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:29:55,334 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:29:56,267 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:29:56,269 [ERROR]    Symbol: AVAXUSDT, Side: SELL, Qty: 6.0
2025-11-13 05:29:56,770 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:29:56,772 [ERROR]    âŒ Order placement failed!
2025-11-13 05:29:57,266 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:29:57,769 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:29:57,869 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:29:58,254 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:29:58,255 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:29:58,255 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:29:58,256 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:29:58,256 [INFO]    âšª No signal - HOLD
2025-11-13 05:29:58,256 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:30:58,293 [INFO] 
============================================================
2025-11-13 05:30:58,293 [INFO] ðŸ”„ LOOP #39 - 2025-11-13 05:30:58
2025-11-13 05:30:58,294 [INFO] ============================================================
2025-11-13 05:30:58,396 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:30:58,396 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:30:58,494 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:30:58,907 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:30:58,908 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:30:58,909 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:30:58,909 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:30:58,909 [INFO]    âšª No signal - HOLD
2025-11-13 05:30:59,410 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:30:59,513 [INFO]    Current position: LONG 0.029
2025-11-13 05:30:59,513 [INFO]    Entry: $3474.80 | Mark: $3486.46
2025-11-13 05:30:59,513 [INFO]    PnL: 0.34% ($0.34)
2025-11-13 05:30:59,513 [INFO]    Age: 1.1h / 36.0h
2025-11-13 05:31:00,014 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:31:00,118 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:31:00,510 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:31:00,511 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:31:00,511 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:31:00,512 [INFO]    âšª No signal - HOLD
2025-11-13 05:31:01,012 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:31:01,212 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:31:01,665 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:31:01,666 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:31:01,666 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:31:01,667 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:31:01,667 [INFO]    âšª No signal - HOLD
2025-11-13 05:31:02,168 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:31:02,269 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:31:02,723 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:31:02,723 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:31:02,723 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:31:02,724 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:31:02,724 [INFO]    âšª No signal - HOLD
2025-11-13 05:31:03,224 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:31:03,325 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:31:03,673 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:31:03,673 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:31:03,673 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:31:03,674 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:31:03,674 [INFO]    âšª No signal - HOLD
2025-11-13 05:31:03,674 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:32:03,734 [INFO] 
============================================================
2025-11-13 05:32:03,735 [INFO] ðŸ”„ LOOP #40 - 2025-11-13 05:32:03
2025-11-13 05:32:03,735 [INFO] ============================================================
2025-11-13 05:32:04,340 [INFO] ðŸ’“ Bot alive - Loop #40 - Active positions: 1
2025-11-13 05:32:04,444 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:32:04,444 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:32:04,545 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:32:04,918 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:32:04,919 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 05:32:04,919 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:32:04,919 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 05:32:04,919 [INFO]    âšª No signal - HOLD
2025-11-13 05:32:05,420 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:32:05,522 [INFO]    Current position: LONG 0.029
2025-11-13 05:32:05,522 [INFO]    Entry: $3474.80 | Mark: $3481.74
2025-11-13 05:32:05,522 [INFO]    PnL: 0.20% ($0.20)
2025-11-13 05:32:05,522 [INFO]    Age: 1.1h / 36.0h
2025-11-13 05:32:06,023 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:32:06,127 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:32:06,526 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:32:06,530 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:32:06,530 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:32:06,530 [INFO]    âšª No signal - HOLD
2025-11-13 05:32:07,031 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:32:07,131 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:32:07,499 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:32:07,501 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:32:07,502 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:32:07,502 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(2): ðŸ•¯ï¸ Bearish Engulfing
2025-11-13 05:32:07,502 [INFO]    âšª No signal - HOLD
2025-11-13 05:32:08,003 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:32:08,102 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:32:08,480 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:32:08,480 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:32:08,481 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:32:08,481 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:32:08,481 [INFO]    âšª No signal - HOLD
2025-11-13 05:32:08,982 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:32:09,087 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:32:09,451 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:32:09,451 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:32:09,452 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:32:09,452 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:32:09,452 [INFO]    âšª No signal - HOLD
2025-11-13 05:32:10,068 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:33:10,074 [INFO] 
============================================================
2025-11-13 05:33:10,074 [INFO] ðŸ”„ LOOP #41 - 2025-11-13 05:33:10
2025-11-13 05:33:10,074 [INFO] ============================================================
2025-11-13 05:33:10,179 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:33:10,179 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:33:10,279 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:33:10,622 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:33:10,622 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:33:10,622 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:33:10,623 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:33:10,623 [INFO]    âšª No signal - HOLD
2025-11-13 05:33:11,123 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:33:11,225 [INFO]    Current position: LONG 0.029
2025-11-13 05:33:11,225 [INFO]    Entry: $3474.80 | Mark: $3486.35
2025-11-13 05:33:11,225 [INFO]    PnL: 0.33% ($0.34)
2025-11-13 05:33:11,225 [INFO]    Age: 1.2h / 36.0h
2025-11-13 05:33:11,725 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:33:11,825 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:33:12,188 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:33:12,189 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:33:12,189 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:33:12,190 [INFO]    âšª No signal - HOLD
2025-11-13 05:33:12,691 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:33:12,791 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:33:13,173 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:33:13,173 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:33:13,174 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:33:13,174 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:33:13,174 [INFO]    âšª No signal - HOLD
2025-11-13 05:33:13,675 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:33:13,775 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:33:14,120 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:33:14,120 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:33:14,120 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:33:14,121 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:33:14,121 [INFO]    âšª No signal - HOLD
2025-11-13 05:33:14,621 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:33:14,723 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:33:15,099 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:33:15,099 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:33:15,099 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:33:15,100 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:33:15,100 [INFO]    âšª No signal - HOLD
2025-11-13 05:33:15,100 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:34:15,139 [INFO] 
============================================================
2025-11-13 05:34:15,140 [INFO] ðŸ”„ LOOP #42 - 2025-11-13 05:34:15
2025-11-13 05:34:15,140 [INFO] ============================================================
2025-11-13 05:34:15,240 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:34:15,240 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:34:15,340 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:34:15,738 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:34:15,738 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:34:15,738 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:34:15,738 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:34:15,738 [INFO]    âšª No signal - HOLD
2025-11-13 05:34:16,239 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:34:16,347 [INFO]    Current position: LONG 0.029
2025-11-13 05:34:16,347 [INFO]    Entry: $3474.80 | Mark: $3489.00
2025-11-13 05:34:16,348 [INFO]    PnL: 0.41% ($0.41)
2025-11-13 05:34:16,348 [INFO]    Age: 1.2h / 36.0h
2025-11-13 05:34:16,848 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:34:16,949 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:34:17,325 [INFO]    âš ï¸ HTF trend is bearish, filtering LONG signal
2025-11-13 05:34:17,326 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 05:34:17,326 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:34:17,326 [INFO]    âšª No signal - HOLD
2025-11-13 05:34:17,827 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:34:17,930 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:34:18,285 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 05:34:18,286 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:34:18,286 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:34:18,286 [INFO]       1. ðŸ“Œ Bullish Pin Bar
2025-11-13 05:34:18,286 [INFO]       2. ðŸ”· Bullish Order Block
2025-11-13 05:34:18,286 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.533 | RSI: 55.5 | OB: 0.85
2025-11-13 05:34:18,287 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:34:18,287 [INFO]    ðŸ“ Signal reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 05:34:18,287 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:34:18,287 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:34:18,287 [INFO]    ðŸ“ Top reasons: ðŸ“Œ Bullish Pin Bar, ðŸ”· Bullish Order Block
2025-11-13 05:34:18,287 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:34:18,387 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 05:34:18,590 [INFO]    ðŸ’µ Current price: $99.62
2025-11-13 05:34:18,590 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:34:18,591 [INFO]       Balance: $17.84
2025-11-13 05:34:18,591 [INFO]       Price: $99.62
2025-11-13 05:34:18,591 [INFO]       Capital (fixed): $10.00
2025-11-13 05:34:18,591 [INFO]       Leverage: 10x
2025-11-13 05:34:18,591 [INFO]       Raw quantity: 1.00381450
2025-11-13 05:34:18,591 [INFO]       Formatted quantity: 1.00400000
2025-11-13 05:34:18,591 [INFO]    ðŸ“¤ Placing BUY order for 1.004 LTCUSDT...
2025-11-13 05:34:18,591 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 05:34:18,591 [INFO]    Raw qty: 1.00400000 -> Formatted: 1.004
2025-11-13 05:34:18,943 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:34:19,688 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:34:19,689 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 1.004
2025-11-13 05:34:20,109 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:34:20,111 [ERROR]    âŒ Order placement failed!
2025-11-13 05:34:20,540 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:34:21,043 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:34:21,144 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:34:21,550 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:34:21,551 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:34:21,551 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:34:21,552 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:34:21,552 [INFO]    âšª No signal - HOLD
2025-11-13 05:34:22,052 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:34:22,154 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:34:22,635 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:34:22,635 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:34:22,635 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:34:22,636 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:34:22,636 [INFO]    âšª No signal - HOLD
2025-11-13 05:34:22,636 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:35:22,693 [INFO] 
============================================================
2025-11-13 05:35:22,694 [INFO] ðŸ”„ LOOP #43 - 2025-11-13 05:35:22
2025-11-13 05:35:22,694 [INFO] ============================================================
2025-11-13 05:35:22,797 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:35:22,797 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:35:22,897 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:35:23,294 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:35:23,294 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:35:23,295 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:35:23,295 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:35:23,295 [INFO]    âšª No signal - HOLD
2025-11-13 05:35:23,796 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:35:23,896 [INFO]    Current position: LONG 0.029
2025-11-13 05:35:23,896 [INFO]    Entry: $3474.80 | Mark: $3493.30
2025-11-13 05:35:23,896 [INFO]    PnL: 0.53% ($0.54)
2025-11-13 05:35:23,896 [INFO]    Age: 1.2h / 36.0h
2025-11-13 05:35:24,397 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:35:24,496 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:35:24,878 [INFO] ðŸŽ¯ SOLUSDT Advanced Signal: LONG
2025-11-13 05:35:24,879 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:35:24,879 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:35:24,879 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:35:24,879 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:35:24,879 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.553 | RSI: 63.7 | OB: 1.46
2025-11-13 05:35:24,880 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:35:24,880 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:35:24,880 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:35:24,880 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:35:24,880 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:35:24,880 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:35:24,979 [INFO] âœ… Set leverage 10x for SOLUSDT
2025-11-13 05:35:25,180 [INFO]    ðŸ’µ Current price: $154.76
2025-11-13 05:35:25,388 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:35:25,389 [INFO]       Balance: $17.84
2025-11-13 05:35:25,389 [INFO]       Price: $154.76
2025-11-13 05:35:25,389 [INFO]       Capital (fixed): $10.00
2025-11-13 05:35:25,389 [INFO]       Leverage: 10x
2025-11-13 05:35:25,389 [INFO]       Raw quantity: 0.64616180
2025-11-13 05:35:25,389 [INFO]       Formatted quantity: 0.65000000
2025-11-13 05:35:25,389 [INFO]    ðŸ“¤ Placing BUY order for 0.65 SOLUSDT...
2025-11-13 05:35:25,389 [INFO] ðŸ“ Order: BUY SOLUSDT
2025-11-13 05:35:25,390 [INFO]    Raw qty: 0.65000000 -> Formatted: 0.65
2025-11-13 05:35:25,742 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:35:27,024 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:35:27,026 [ERROR]    Symbol: SOLUSDT, Side: BUY, Qty: 0.65
2025-11-13 05:35:27,512 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:35:27,514 [ERROR]    âŒ Order placement failed!
2025-11-13 05:35:28,002 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:35:28,505 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:35:28,608 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:35:29,058 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 05:35:29,058 [INFO]    ðŸ“Š Confluence Score: 8/4
2025-11-13 05:35:29,059 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:35:29,059 [INFO]       1. ðŸ“Œ Bullish Pin Bar
2025-11-13 05:35:29,059 [INFO]       2. â­ Morning Star
2025-11-13 05:35:29,059 [INFO]       3. ðŸ”· Bullish Order Block
2025-11-13 05:35:29,059 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.556 | RSI: 55.6 | OB: 0.43
2025-11-13 05:35:29,059 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=8
2025-11-13 05:35:29,060 [INFO]    ðŸ“ Signal reasons: ðŸ“Œ Bullish Pin Bar, â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:35:29,060 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:35:29,060 [INFO]    ðŸ“Š Confluence score: 8/4
2025-11-13 05:35:29,060 [INFO]    ðŸ“ Top reasons: ðŸ“Œ Bullish Pin Bar, â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:35:29,060 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:35:29,159 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 05:35:29,357 [INFO]    ðŸ’µ Current price: $99.64
2025-11-13 05:35:29,357 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:35:29,357 [INFO]       Balance: $17.84
2025-11-13 05:35:29,357 [INFO]       Price: $99.64
2025-11-13 05:35:29,358 [INFO]       Capital (fixed): $10.00
2025-11-13 05:35:29,358 [INFO]       Leverage: 10x
2025-11-13 05:35:29,358 [INFO]       Raw quantity: 1.00361301
2025-11-13 05:35:29,358 [INFO]       Formatted quantity: 1.00400000
2025-11-13 05:35:29,358 [INFO]    ðŸ“¤ Placing BUY order for 1.004 LTCUSDT...
2025-11-13 05:35:29,358 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 05:35:29,358 [INFO]    Raw qty: 1.00400000 -> Formatted: 1.004
2025-11-13 05:35:29,710 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:35:30,204 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:35:30,205 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 1.004
2025-11-13 05:35:30,688 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:35:30,690 [ERROR]    âŒ Order placement failed!
2025-11-13 05:35:34,467 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:35:34,969 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:35:35,070 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:35:35,452 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:35:35,452 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:35:35,453 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:35:35,453 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:35:35,453 [INFO]    âšª No signal - HOLD
2025-11-13 05:35:35,954 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:35:36,054 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:35:36,511 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:35:36,511 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:35:36,512 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:35:36,512 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:35:36,512 [INFO]    âšª No signal - HOLD
2025-11-13 05:35:36,512 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:36:36,525 [INFO] 
============================================================
2025-11-13 05:36:36,526 [INFO] ðŸ”„ LOOP #44 - 2025-11-13 05:36:36
2025-11-13 05:36:36,526 [INFO] ============================================================
2025-11-13 05:36:36,628 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:36:36,628 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:36:36,728 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:36:37,113 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:36:37,114 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:36:37,114 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:36:37,114 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:36:37,114 [INFO]    âšª No signal - HOLD
2025-11-13 05:36:37,615 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:36:37,712 [INFO]    Current position: LONG 0.029
2025-11-13 05:36:37,712 [INFO]    Entry: $3474.80 | Mark: $3498.86
2025-11-13 05:36:37,712 [INFO]    PnL: 0.69% ($0.70)
2025-11-13 05:36:37,712 [INFO]    Age: 1.2h / 36.0h
2025-11-13 05:36:38,213 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:36:38,313 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:36:38,662 [INFO] ðŸŽ¯ SOLUSDT Advanced Signal: LONG
2025-11-13 05:36:38,662 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:36:38,663 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:36:38,663 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:36:38,663 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:36:38,663 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.543 | RSI: 65.5 | OB: 1.26
2025-11-13 05:36:38,663 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:36:38,663 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:36:38,663 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:36:38,663 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:36:38,664 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:36:38,664 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:36:38,764 [INFO] âœ… Set leverage 10x for SOLUSDT
2025-11-13 05:36:38,967 [INFO]    ðŸ’µ Current price: $155.10
2025-11-13 05:36:38,967 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:36:38,967 [INFO]       Balance: $17.84
2025-11-13 05:36:38,967 [INFO]       Price: $155.10
2025-11-13 05:36:38,967 [INFO]       Capital (fixed): $10.00
2025-11-13 05:36:38,967 [INFO]       Leverage: 10x
2025-11-13 05:36:38,967 [INFO]       Raw quantity: 0.64474533
2025-11-13 05:36:38,967 [INFO]       Formatted quantity: 0.64000000
2025-11-13 05:36:38,968 [INFO]    ðŸ“¤ Placing BUY order for 0.64 SOLUSDT...
2025-11-13 05:36:38,968 [INFO] ðŸ“ Order: BUY SOLUSDT
2025-11-13 05:36:38,968 [INFO]    Raw qty: 0.64000000 -> Formatted: 0.64
2025-11-13 05:36:39,320 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:36:40,257 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:36:40,259 [ERROR]    Symbol: SOLUSDT, Side: BUY, Qty: 0.64
2025-11-13 05:36:40,758 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:36:40,759 [ERROR]    âŒ Order placement failed!
2025-11-13 05:36:41,257 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:36:41,760 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:36:41,864 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:36:42,231 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 05:36:42,231 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 05:36:42,231 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:36:42,231 [INFO]       1. â­ Morning Star
2025-11-13 05:36:42,231 [INFO]       2. ðŸ”· Bullish Order Block
2025-11-13 05:36:42,231 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.540 | RSI: 57.0 | OB: 0.92
2025-11-13 05:36:42,232 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 05:36:42,232 [INFO]    ðŸ“ Signal reasons: â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:36:42,232 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:36:42,232 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 05:36:42,232 [INFO]    ðŸ“ Top reasons: â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:36:42,232 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:36:42,331 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 05:36:42,530 [INFO]    ðŸ’µ Current price: $99.98
2025-11-13 05:36:42,530 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:36:42,530 [INFO]       Balance: $17.84
2025-11-13 05:36:42,530 [INFO]       Price: $99.98
2025-11-13 05:36:42,530 [INFO]       Capital (fixed): $10.00
2025-11-13 05:36:42,530 [INFO]       Leverage: 10x
2025-11-13 05:36:42,530 [INFO]       Raw quantity: 1.00020004
2025-11-13 05:36:42,530 [INFO]       Formatted quantity: 1.00000000
2025-11-13 05:36:42,530 [INFO]    ðŸ“¤ Placing BUY order for 1.0 LTCUSDT...
2025-11-13 05:36:42,531 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 05:36:42,531 [INFO]    Raw qty: 1.00000000 -> Formatted: 1.0
2025-11-13 05:36:42,883 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:36:44,386 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:36:44,388 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 1.0
2025-11-13 05:36:44,881 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:36:44,883 [ERROR]    âŒ Order placement failed!
2025-11-13 05:36:45,367 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:36:45,870 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:36:45,975 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:36:46,430 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:36:46,430 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:36:46,430 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:36:46,431 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:36:46,431 [INFO]    âšª No signal - HOLD
2025-11-13 05:36:46,931 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:36:47,030 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:36:47,387 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:36:47,388 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:36:47,388 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:36:47,388 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:36:47,388 [INFO]    âšª No signal - HOLD
2025-11-13 05:36:47,388 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:37:47,431 [INFO] 
============================================================
2025-11-13 05:37:47,431 [INFO] ðŸ”„ LOOP #45 - 2025-11-13 05:37:47
2025-11-13 05:37:47,431 [INFO] ============================================================
2025-11-13 05:37:48,028 [INFO] ðŸ’“ Bot alive - Loop #45 - Active positions: 1
2025-11-13 05:37:48,130 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:37:48,130 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:37:48,233 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:37:48,598 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:37:48,598 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:37:48,599 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:37:48,599 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:37:48,599 [INFO]    âšª No signal - HOLD
2025-11-13 05:37:49,100 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:37:49,202 [INFO]    Current position: LONG 0.029
2025-11-13 05:37:49,202 [INFO]    Entry: $3474.80 | Mark: $3501.70
2025-11-13 05:37:49,202 [INFO]    PnL: 0.77% ($0.78)
2025-11-13 05:37:49,202 [INFO]    Age: 1.2h / 36.0h
2025-11-13 05:37:49,704 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:37:49,806 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:37:50,182 [INFO] ðŸŽ¯ SOLUSDT Advanced Signal: LONG
2025-11-13 05:37:50,182 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:37:50,182 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:37:50,182 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:37:50,182 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:37:50,182 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.566 | RSI: 66.1 | OB: 1.08
2025-11-13 05:37:50,183 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:37:50,183 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:37:50,183 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:37:50,183 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:37:50,183 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:37:50,183 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:37:50,283 [INFO] âœ… Set leverage 10x for SOLUSDT
2025-11-13 05:37:50,679 [INFO]    ðŸ’µ Current price: $155.19
2025-11-13 05:37:50,680 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:37:50,680 [INFO]       Balance: $17.84
2025-11-13 05:37:50,680 [INFO]       Price: $155.19
2025-11-13 05:37:50,680 [INFO]       Capital (fixed): $10.00
2025-11-13 05:37:50,680 [INFO]       Leverage: 10x
2025-11-13 05:37:50,680 [INFO]       Raw quantity: 0.64439218
2025-11-13 05:37:50,680 [INFO]       Formatted quantity: 0.64000000
2025-11-13 05:37:50,680 [INFO]    ðŸ“¤ Placing BUY order for 0.64 SOLUSDT...
2025-11-13 05:37:50,680 [INFO] ðŸ“ Order: BUY SOLUSDT
2025-11-13 05:37:50,680 [INFO]    Raw qty: 0.64000000 -> Formatted: 0.64
2025-11-13 05:37:51,034 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:37:51,944 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:37:51,946 [ERROR]    Symbol: SOLUSDT, Side: BUY, Qty: 0.64
2025-11-13 05:37:52,443 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:37:52,449 [ERROR]    âŒ Order placement failed!
2025-11-13 05:37:52,964 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:37:53,467 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:37:53,567 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:37:53,936 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 05:37:53,937 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 05:37:53,937 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:37:53,937 [INFO]       1. â­ Morning Star
2025-11-13 05:37:53,937 [INFO]       2. ðŸ”· Bullish Order Block
2025-11-13 05:37:53,937 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.566 | RSI: 58.5 | OB: 1.09
2025-11-13 05:37:53,938 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 05:37:53,938 [INFO]    ðŸ“ Signal reasons: â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:37:53,938 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:37:53,938 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 05:37:53,938 [INFO]    ðŸ“ Top reasons: â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:37:53,938 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:37:54,037 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 05:37:54,237 [INFO]    ðŸ’µ Current price: $100.04
2025-11-13 05:37:54,237 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:37:54,237 [INFO]       Balance: $17.84
2025-11-13 05:37:54,237 [INFO]       Price: $100.04
2025-11-13 05:37:54,237 [INFO]       Capital (fixed): $10.00
2025-11-13 05:37:54,238 [INFO]       Leverage: 10x
2025-11-13 05:37:54,238 [INFO]       Raw quantity: 0.99960016
2025-11-13 05:37:54,238 [INFO]       Formatted quantity: 1.00000000
2025-11-13 05:37:54,238 [INFO]    ðŸ“¤ Placing BUY order for 1.0 LTCUSDT...
2025-11-13 05:37:54,238 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 05:37:54,238 [INFO]    Raw qty: 1.00000000 -> Formatted: 1.0
2025-11-13 05:37:54,587 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:37:55,218 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:37:55,220 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 1.0
2025-11-13 05:37:55,730 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:37:55,732 [ERROR]    âŒ Order placement failed!
2025-11-13 05:37:59,554 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:38:00,056 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:38:00,163 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:38:00,683 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:38:00,683 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:38:00,683 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:38:00,684 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:38:00,684 [INFO]    âšª No signal - HOLD
2025-11-13 05:38:01,184 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:38:01,287 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:38:01,640 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:38:01,640 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:38:01,641 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:38:01,641 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:38:01,641 [INFO]    âšª No signal - HOLD
2025-11-13 05:38:01,641 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:39:01,697 [INFO] 
============================================================
2025-11-13 05:39:01,698 [INFO] ðŸ”„ LOOP #46 - 2025-11-13 05:39:01
2025-11-13 05:39:01,698 [INFO] ============================================================
2025-11-13 05:39:01,802 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:39:01,802 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:39:01,901 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:39:02,308 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:39:02,309 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:39:02,310 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:39:02,310 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:39:02,310 [INFO]    âšª No signal - HOLD
2025-11-13 05:39:02,811 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:39:02,912 [INFO]    Current position: LONG 0.029
2025-11-13 05:39:02,913 [INFO]    Entry: $3474.80 | Mark: $3507.42
2025-11-13 05:39:02,913 [INFO]    PnL: 0.94% ($0.95)
2025-11-13 05:39:02,913 [INFO]    Age: 1.3h / 36.0h
2025-11-13 05:39:03,414 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:39:03,514 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:39:03,896 [INFO] ðŸŽ¯ SOLUSDT Advanced Signal: LONG
2025-11-13 05:39:03,896 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:39:03,896 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:39:03,896 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:39:03,896 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:39:03,896 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.568 | RSI: 66.6 | OB: 1.21
2025-11-13 05:39:03,897 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:39:03,897 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:39:03,897 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:39:03,898 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:39:03,898 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:39:03,898 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:39:03,995 [INFO] âœ… Set leverage 10x for SOLUSDT
2025-11-13 05:39:04,197 [INFO]    ðŸ’µ Current price: $155.37
2025-11-13 05:39:04,197 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:39:04,197 [INFO]       Balance: $17.84
2025-11-13 05:39:04,197 [INFO]       Price: $155.37
2025-11-13 05:39:04,197 [INFO]       Capital (fixed): $10.00
2025-11-13 05:39:04,197 [INFO]       Leverage: 10x
2025-11-13 05:39:04,197 [INFO]       Raw quantity: 0.64362490
2025-11-13 05:39:04,197 [INFO]       Formatted quantity: 0.64000000
2025-11-13 05:39:04,198 [INFO]    ðŸ“¤ Placing BUY order for 0.64 SOLUSDT...
2025-11-13 05:39:04,198 [INFO] ðŸ“ Order: BUY SOLUSDT
2025-11-13 05:39:04,198 [INFO]    Raw qty: 0.64000000 -> Formatted: 0.64
2025-11-13 05:39:04,549 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:39:05,394 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:39:05,396 [ERROR]    Symbol: SOLUSDT, Side: BUY, Qty: 0.64
2025-11-13 05:39:05,900 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:39:05,902 [ERROR]    âŒ Order placement failed!
2025-11-13 05:39:06,401 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:39:06,903 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:39:07,011 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:39:07,367 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 05:39:07,367 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 05:39:07,367 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:39:07,367 [INFO]       1. â­ Morning Star
2025-11-13 05:39:07,367 [INFO]       2. ðŸ”· Bullish Order Block
2025-11-13 05:39:07,368 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.573 | RSI: 59.5 | OB: 0.89
2025-11-13 05:39:07,368 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 05:39:07,369 [INFO]    ðŸ“ Signal reasons: â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:39:07,369 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:39:07,369 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 05:39:07,369 [INFO]    ðŸ“ Top reasons: â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:39:07,369 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:39:07,469 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 05:39:07,766 [INFO]    ðŸ’µ Current price: $100.16
2025-11-13 05:39:07,766 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:39:07,766 [INFO]       Balance: $17.84
2025-11-13 05:39:07,766 [INFO]       Price: $100.16
2025-11-13 05:39:07,766 [INFO]       Capital (fixed): $10.00
2025-11-13 05:39:07,766 [INFO]       Leverage: 10x
2025-11-13 05:39:07,766 [INFO]       Raw quantity: 0.99840256
2025-11-13 05:39:07,766 [INFO]       Formatted quantity: 0.99800000
2025-11-13 05:39:07,767 [INFO]    ðŸ“¤ Placing BUY order for 0.998 LTCUSDT...
2025-11-13 05:39:07,767 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 05:39:07,767 [INFO]    Raw qty: 0.99800000 -> Formatted: 0.998
2025-11-13 05:39:08,119 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:39:08,625 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:39:08,628 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.998
2025-11-13 05:39:09,123 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:39:09,126 [ERROR]    âŒ Order placement failed!
2025-11-13 05:39:12,935 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:39:13,438 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:39:13,538 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:39:13,895 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:39:13,895 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:39:13,896 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:39:13,896 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:39:13,896 [INFO]    âšª No signal - HOLD
2025-11-13 05:39:14,397 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:39:14,493 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:39:14,853 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:39:14,854 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:39:14,854 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:39:14,854 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:39:14,854 [INFO]    âšª No signal - HOLD
2025-11-13 05:39:14,855 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:40:14,914 [INFO] 
============================================================
2025-11-13 05:40:14,914 [INFO] ðŸ”„ LOOP #47 - 2025-11-13 05:40:14
2025-11-13 05:40:14,914 [INFO] ============================================================
2025-11-13 05:40:15,021 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:40:15,021 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:40:15,123 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:40:15,531 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:40:15,532 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:40:15,532 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:40:15,533 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:40:15,533 [INFO]    âšª No signal - HOLD
2025-11-13 05:40:16,034 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:40:16,137 [INFO]    Current position: LONG 0.029
2025-11-13 05:40:16,137 [INFO]    Entry: $3474.80 | Mark: $3502.66
2025-11-13 05:40:16,137 [INFO]    PnL: 0.80% ($0.81)
2025-11-13 05:40:16,137 [INFO]    Age: 1.3h / 36.0h
2025-11-13 05:40:16,638 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:40:16,738 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:40:17,093 [INFO] ðŸŽ¯ SOLUSDT Advanced Signal: LONG
2025-11-13 05:40:17,093 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:40:17,094 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:40:17,094 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:40:17,094 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:40:17,094 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.567 | RSI: 65.5 | OB: 1.63
2025-11-13 05:40:17,094 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:40:17,095 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:40:17,095 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:40:17,095 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:40:17,095 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:40:17,095 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:40:17,196 [INFO] âœ… Set leverage 10x for SOLUSDT
2025-11-13 05:40:17,397 [INFO]    ðŸ’µ Current price: $155.15
2025-11-13 05:40:17,397 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:40:17,397 [INFO]       Balance: $17.84
2025-11-13 05:40:17,397 [INFO]       Price: $155.15
2025-11-13 05:40:17,398 [INFO]       Capital (fixed): $10.00
2025-11-13 05:40:17,398 [INFO]       Leverage: 10x
2025-11-13 05:40:17,398 [INFO]       Raw quantity: 0.64453754
2025-11-13 05:40:17,398 [INFO]       Formatted quantity: 0.64000000
2025-11-13 05:40:17,398 [INFO]    ðŸ“¤ Placing BUY order for 0.64 SOLUSDT...
2025-11-13 05:40:17,398 [INFO] ðŸ“ Order: BUY SOLUSDT
2025-11-13 05:40:17,398 [INFO]    Raw qty: 0.64000000 -> Formatted: 0.64
2025-11-13 05:40:17,752 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:40:18,585 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:40:18,587 [ERROR]    Symbol: SOLUSDT, Side: BUY, Qty: 0.64
2025-11-13 05:40:19,037 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:40:19,039 [ERROR]    âŒ Order placement failed!
2025-11-13 05:40:19,483 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:40:19,985 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:40:20,085 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:40:20,454 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 05:40:20,455 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 05:40:20,455 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:40:20,455 [INFO]       1. â­ Morning Star
2025-11-13 05:40:20,455 [INFO]       2. ðŸ”· Bullish Order Block
2025-11-13 05:40:20,455 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.580 | RSI: 59.7 | OB: 0.84
2025-11-13 05:40:20,455 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 05:40:20,456 [INFO]    ðŸ“ Signal reasons: â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:40:20,456 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:40:20,456 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 05:40:20,456 [INFO]    ðŸ“ Top reasons: â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:40:20,456 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:40:20,555 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 05:40:20,749 [INFO]    ðŸ’µ Current price: $100.23
2025-11-13 05:40:20,750 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:40:20,750 [INFO]       Balance: $17.84
2025-11-13 05:40:20,750 [INFO]       Price: $100.23
2025-11-13 05:40:20,750 [INFO]       Capital (fixed): $10.00
2025-11-13 05:40:20,750 [INFO]       Leverage: 10x
2025-11-13 05:40:20,750 [INFO]       Raw quantity: 0.99770528
2025-11-13 05:40:20,750 [INFO]       Formatted quantity: 0.99800000
2025-11-13 05:40:20,750 [INFO]    ðŸ“¤ Placing BUY order for 0.998 LTCUSDT...
2025-11-13 05:40:20,750 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 05:40:20,750 [INFO]    Raw qty: 0.99800000 -> Formatted: 0.998
2025-11-13 05:40:21,103 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:40:21,490 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:40:21,492 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.998
2025-11-13 05:40:21,925 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:40:21,927 [ERROR]    âŒ Order placement failed!
2025-11-13 05:40:25,598 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:40:26,101 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:40:26,201 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:40:26,613 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:40:26,614 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:40:26,614 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:40:26,614 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:40:26,614 [INFO]    âšª No signal - HOLD
2025-11-13 05:40:27,115 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:40:27,217 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:40:27,584 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:40:27,584 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:40:27,584 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:40:27,584 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:40:27,584 [INFO]    âšª No signal - HOLD
2025-11-13 05:40:27,585 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:41:27,631 [INFO] 
============================================================
2025-11-13 05:41:27,632 [INFO] ðŸ”„ LOOP #48 - 2025-11-13 05:41:27
2025-11-13 05:41:27,632 [INFO] ============================================================
2025-11-13 05:41:27,734 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:41:27,734 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:41:27,837 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:41:28,237 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:41:28,237 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:41:28,237 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:41:28,238 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:41:28,238 [INFO]    âšª No signal - HOLD
2025-11-13 05:41:28,738 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:41:28,835 [INFO]    Current position: LONG 0.029
2025-11-13 05:41:28,835 [INFO]    Entry: $3474.80 | Mark: $3505.00
2025-11-13 05:41:28,835 [INFO]    PnL: 0.87% ($0.88)
2025-11-13 05:41:28,835 [INFO]    Age: 1.3h / 36.0h
2025-11-13 05:41:29,336 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:41:29,438 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:41:29,832 [INFO] ðŸŽ¯ SOLUSDT Advanced Signal: LONG
2025-11-13 05:41:29,832 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:41:29,832 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:41:29,832 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:41:29,832 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:41:29,833 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.567 | RSI: 65.6 | OB: 1.66
2025-11-13 05:41:29,833 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:41:29,834 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:41:29,834 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:41:29,834 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:41:29,834 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:41:29,834 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:41:29,932 [INFO] âœ… Set leverage 10x for SOLUSDT
2025-11-13 05:41:30,228 [INFO]    ðŸ’µ Current price: $155.12
2025-11-13 05:41:30,228 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:41:30,228 [INFO]       Balance: $17.84
2025-11-13 05:41:30,228 [INFO]       Price: $155.12
2025-11-13 05:41:30,228 [INFO]       Capital (fixed): $10.00
2025-11-13 05:41:30,228 [INFO]       Leverage: 10x
2025-11-13 05:41:30,228 [INFO]       Raw quantity: 0.64466220
2025-11-13 05:41:30,228 [INFO]       Formatted quantity: 0.64000000
2025-11-13 05:41:30,229 [INFO]    ðŸ“¤ Placing BUY order for 0.64 SOLUSDT...
2025-11-13 05:41:30,229 [INFO] ðŸ“ Order: BUY SOLUSDT
2025-11-13 05:41:30,229 [INFO]    Raw qty: 0.64000000 -> Formatted: 0.64
2025-11-13 05:41:30,579 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:41:31,314 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:41:31,316 [ERROR]    Symbol: SOLUSDT, Side: BUY, Qty: 0.64
2025-11-13 05:41:31,730 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:41:31,732 [ERROR]    âŒ Order placement failed!
2025-11-13 05:41:32,129 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:41:32,632 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:41:32,734 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:41:33,100 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 05:41:33,101 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 05:41:33,101 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:41:33,101 [INFO]       1. â­ Morning Star
2025-11-13 05:41:33,101 [INFO]       2. ðŸ”· Bullish Order Block
2025-11-13 05:41:33,101 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.589 | RSI: 59.7 | OB: 4.99
2025-11-13 05:41:33,102 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 05:41:33,102 [INFO]    ðŸ“ Signal reasons: â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:41:33,102 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:41:33,102 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 05:41:33,102 [INFO]    ðŸ“ Top reasons: â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:41:33,102 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:41:33,201 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 05:41:33,413 [INFO]    ðŸ’µ Current price: $100.23
2025-11-13 05:41:33,413 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:41:33,413 [INFO]       Balance: $17.84
2025-11-13 05:41:33,413 [INFO]       Price: $100.23
2025-11-13 05:41:33,413 [INFO]       Capital (fixed): $10.00
2025-11-13 05:41:33,413 [INFO]       Leverage: 10x
2025-11-13 05:41:33,413 [INFO]       Raw quantity: 0.99770528
2025-11-13 05:41:33,413 [INFO]       Formatted quantity: 0.99800000
2025-11-13 05:41:33,414 [INFO]    ðŸ“¤ Placing BUY order for 0.998 LTCUSDT...
2025-11-13 05:41:33,414 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 05:41:33,414 [INFO]    Raw qty: 0.99800000 -> Formatted: 0.998
2025-11-13 05:41:33,764 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:41:34,129 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:41:34,131 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.998
2025-11-13 05:41:34,532 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:41:34,535 [ERROR]    âŒ Order placement failed!
2025-11-13 05:41:38,159 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:41:38,662 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:41:38,889 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:41:39,303 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:41:39,308 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:41:39,309 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:41:39,309 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:41:39,309 [INFO]    âšª No signal - HOLD
2025-11-13 05:41:39,810 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:41:39,912 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:41:40,274 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:41:40,275 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:41:40,275 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:41:40,276 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:41:40,276 [INFO]    âšª No signal - HOLD
2025-11-13 05:41:40,276 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:42:40,322 [INFO] 
============================================================
2025-11-13 05:42:40,322 [INFO] ðŸ”„ LOOP #49 - 2025-11-13 05:42:40
2025-11-13 05:42:40,322 [INFO] ============================================================
2025-11-13 05:42:40,428 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:42:40,428 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:42:40,548 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:42:40,954 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:42:40,954 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:42:40,955 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:42:40,955 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:42:40,955 [INFO]    âšª No signal - HOLD
2025-11-13 05:42:41,456 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:42:41,558 [INFO]    Current position: LONG 0.029
2025-11-13 05:42:41,558 [INFO]    Entry: $3474.80 | Mark: $3505.85
2025-11-13 05:42:41,559 [INFO]    PnL: 0.89% ($0.90)
2025-11-13 05:42:41,559 [INFO]    Age: 1.3h / 36.0h
2025-11-13 05:42:42,059 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:42:42,164 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:42:42,532 [INFO] ðŸŽ¯ SOLUSDT Advanced Signal: LONG
2025-11-13 05:42:42,532 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:42:42,532 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:42:42,532 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:42:42,532 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:42:42,533 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.559 | RSI: 65.6 | OB: 1.37
2025-11-13 05:42:42,533 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:42:42,533 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:42:42,533 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:42:42,533 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:42:42,534 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:42:42,534 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:42:42,632 [INFO] âœ… Set leverage 10x for SOLUSDT
2025-11-13 05:42:42,830 [INFO]    ðŸ’µ Current price: $155.17
2025-11-13 05:42:42,830 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:42:42,831 [INFO]       Balance: $17.84
2025-11-13 05:42:42,831 [INFO]       Price: $155.17
2025-11-13 05:42:42,831 [INFO]       Capital (fixed): $10.00
2025-11-13 05:42:42,831 [INFO]       Leverage: 10x
2025-11-13 05:42:42,831 [INFO]       Raw quantity: 0.64445447
2025-11-13 05:42:42,831 [INFO]       Formatted quantity: 0.64000000
2025-11-13 05:42:42,831 [INFO]    ðŸ“¤ Placing BUY order for 0.64 SOLUSDT...
2025-11-13 05:42:42,831 [INFO] ðŸ“ Order: BUY SOLUSDT
2025-11-13 05:42:42,831 [INFO]    Raw qty: 0.64000000 -> Formatted: 0.64
2025-11-13 05:42:43,186 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:42:43,933 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:42:43,935 [ERROR]    Symbol: SOLUSDT, Side: BUY, Qty: 0.64
2025-11-13 05:42:44,340 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:42:44,342 [ERROR]    âŒ Order placement failed!
2025-11-13 05:42:44,744 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:42:45,249 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:42:45,353 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:42:45,709 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 05:42:45,709 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 05:42:45,709 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:42:45,709 [INFO]       1. â­ Morning Star
2025-11-13 05:42:45,709 [INFO]       2. ðŸ”· Bullish Order Block
2025-11-13 05:42:45,709 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.575 | RSI: 58.6 | OB: 2.57
2025-11-13 05:42:45,710 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 05:42:45,710 [INFO]    ðŸ“ Signal reasons: â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:42:45,710 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:42:45,710 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 05:42:45,710 [INFO]    ðŸ“ Top reasons: â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:42:45,710 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:42:45,810 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 05:42:46,008 [INFO]    ðŸ’µ Current price: $100.08
2025-11-13 05:42:46,008 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:42:46,008 [INFO]       Balance: $17.84
2025-11-13 05:42:46,008 [INFO]       Price: $100.08
2025-11-13 05:42:46,008 [INFO]       Capital (fixed): $10.00
2025-11-13 05:42:46,009 [INFO]       Leverage: 10x
2025-11-13 05:42:46,009 [INFO]       Raw quantity: 0.99920064
2025-11-13 05:42:46,009 [INFO]       Formatted quantity: 0.99900000
2025-11-13 05:42:46,009 [INFO]    ðŸ“¤ Placing BUY order for 0.999 LTCUSDT...
2025-11-13 05:42:46,009 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 05:42:46,009 [INFO]    Raw qty: 0.99900000 -> Formatted: 0.999
2025-11-13 05:42:46,364 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:42:46,742 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:42:46,744 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.999
2025-11-13 05:42:47,149 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:42:47,151 [ERROR]    âŒ Order placement failed!
2025-11-13 05:42:50,748 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:42:51,250 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:42:51,353 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:42:51,702 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:42:51,702 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:42:51,703 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:42:51,703 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:42:51,703 [INFO]    âšª No signal - HOLD
2025-11-13 05:42:52,204 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:42:52,304 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:42:52,778 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:42:52,779 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:42:52,780 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:42:52,780 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:42:52,780 [INFO]    âšª No signal - HOLD
2025-11-13 05:42:52,780 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:43:52,837 [INFO] 
============================================================
2025-11-13 05:43:52,838 [INFO] ðŸ”„ LOOP #50 - 2025-11-13 05:43:52
2025-11-13 05:43:52,838 [INFO] ============================================================
2025-11-13 05:43:53,434 [INFO] ðŸ’“ Bot alive - Loop #50 - Active positions: 1
2025-11-13 05:43:53,535 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:43:53,535 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:43:53,637 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:43:54,098 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:43:54,098 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:43:54,099 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:43:54,099 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:43:54,099 [INFO]    âšª No signal - HOLD
2025-11-13 05:43:54,600 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:43:54,700 [INFO]    Current position: LONG 0.029
2025-11-13 05:43:54,700 [INFO]    Entry: $3474.80 | Mark: $3508.20
2025-11-13 05:43:54,701 [INFO]    PnL: 0.96% ($0.97)
2025-11-13 05:43:54,701 [INFO]    Age: 1.3h / 36.0h
2025-11-13 05:43:55,202 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:43:55,299 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:43:55,683 [INFO] ðŸŽ¯ SOLUSDT Advanced Signal: LONG
2025-11-13 05:43:55,683 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:43:55,683 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:43:55,683 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:43:55,683 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:43:55,684 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.559 | RSI: 66.1 | OB: 1.17
2025-11-13 05:43:55,684 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:43:55,685 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:43:55,685 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:43:55,685 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:43:55,685 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:43:55,685 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:43:55,785 [INFO] âœ… Set leverage 10x for SOLUSDT
2025-11-13 05:43:56,091 [INFO]    ðŸ’µ Current price: $155.32
2025-11-13 05:43:56,092 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:43:56,092 [INFO]       Balance: $17.84
2025-11-13 05:43:56,092 [INFO]       Price: $155.32
2025-11-13 05:43:56,092 [INFO]       Capital (fixed): $10.00
2025-11-13 05:43:56,092 [INFO]       Leverage: 10x
2025-11-13 05:43:56,092 [INFO]       Raw quantity: 0.64381136
2025-11-13 05:43:56,092 [INFO]       Formatted quantity: 0.64000000
2025-11-13 05:43:56,092 [INFO]    ðŸ“¤ Placing BUY order for 0.64 SOLUSDT...
2025-11-13 05:43:56,092 [INFO] ðŸ“ Order: BUY SOLUSDT
2025-11-13 05:43:56,092 [INFO]    Raw qty: 0.64000000 -> Formatted: 0.64
2025-11-13 05:43:56,550 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:43:57,412 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:43:57,414 [ERROR]    Symbol: SOLUSDT, Side: BUY, Qty: 0.64
2025-11-13 05:43:57,978 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:43:57,979 [ERROR]    âŒ Order placement failed!
2025-11-13 05:43:58,446 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:43:58,948 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:43:59,050 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:43:59,400 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 05:43:59,400 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 05:43:59,400 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:43:59,400 [INFO]       1. â­ Morning Star
2025-11-13 05:43:59,400 [INFO]       2. ðŸ”· Bullish Order Block
2025-11-13 05:43:59,400 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.578 | RSI: 59.2 | OB: 1.09
2025-11-13 05:43:59,401 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 05:43:59,401 [INFO]    ðŸ“ Signal reasons: â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:43:59,401 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:43:59,401 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 05:43:59,401 [INFO]    ðŸ“ Top reasons: â­ Morning Star, ðŸ”· Bullish Order Block
2025-11-13 05:43:59,401 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:43:59,500 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 05:43:59,699 [INFO]    ðŸ’µ Current price: $100.23
2025-11-13 05:43:59,699 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:43:59,699 [INFO]       Balance: $17.84
2025-11-13 05:43:59,699 [INFO]       Price: $100.23
2025-11-13 05:43:59,699 [INFO]       Capital (fixed): $10.00
2025-11-13 05:43:59,699 [INFO]       Leverage: 10x
2025-11-13 05:43:59,699 [INFO]       Raw quantity: 0.99770528
2025-11-13 05:43:59,699 [INFO]       Formatted quantity: 0.99800000
2025-11-13 05:43:59,699 [INFO]    ðŸ“¤ Placing BUY order for 0.998 LTCUSDT...
2025-11-13 05:43:59,699 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 05:43:59,699 [INFO]    Raw qty: 0.99800000 -> Formatted: 0.998
2025-11-13 05:44:00,152 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:44:00,603 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:44:00,604 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.998
2025-11-13 05:44:01,092 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:44:01,093 [ERROR]    âŒ Order placement failed!
2025-11-13 05:44:04,778 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:44:05,282 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:44:05,385 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:44:05,898 [INFO] ðŸ“¡ AVAXUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:44:05,899 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:44:05,899 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:44:05,899 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:44:05,899 [INFO]    âšª No signal - HOLD
2025-11-13 05:44:06,400 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:44:06,501 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:44:06,863 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:44:06,863 [INFO]    Partial signals: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:44:06,864 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:44:06,864 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”· Bullish Order Block
2025-11-13 05:44:06,864 [INFO]    âšª No signal - HOLD
2025-11-13 05:44:07,883 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:45:07,942 [INFO] 
============================================================
2025-11-13 05:45:07,943 [INFO] ðŸ”„ LOOP #51 - 2025-11-13 05:45:07
2025-11-13 05:45:07,943 [INFO] ============================================================
2025-11-13 05:45:08,048 [INFO] ðŸ’° Current balance: $17.84
2025-11-13 05:45:08,048 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:45:08,151 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:45:08,496 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:45:08,496 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:45:08,497 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:45:08,497 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(3): ðŸ”€ Bearish RSI Divergence
2025-11-13 05:45:08,497 [INFO]    âšª No signal - HOLD
2025-11-13 05:45:08,998 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:45:09,096 [INFO]    Current position: LONG 0.029
2025-11-13 05:45:09,096 [INFO]    Entry: $3474.80 | Mark: $3510.20
2025-11-13 05:45:09,096 [INFO]    PnL: 1.02% ($1.03)
2025-11-13 05:45:09,096 [INFO]    Age: 1.4h / 36.0h
2025-11-13 05:45:09,096 [INFO] ðŸŽ¯ Trailing stop activated for ETHUSDT at 1.02% profit
2025-11-13 05:45:09,096 [INFO]    ðŸ”´ Closing position: TP (1.02%)
2025-11-13 05:45:09,313 [INFO] ðŸ“ Order: SELL ETHUSDT
2025-11-13 05:45:09,313 [INFO]    Raw qty: 0.02900000 -> Formatted: 0.029
2025-11-13 05:45:09,664 [INFO] âœ… Order created: SELL 0.029 ETHUSDT
2025-11-13 05:45:09,664 [INFO] ðŸ’° TRADE: CLOSE LONG ETHUSDT | TP (1.02%) | PnL: 1.02%
2025-11-13 05:45:10,397 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:45:10,399 [INFO] â±ï¸ Cleared position tracking for ETHUSDT
2025-11-13 05:45:10,400 [INFO] ðŸ“ Trade recorded: CLOSE_LONG 0.029 ETHUSDT @ $3510.20
2025-11-13 05:45:10,400 [INFO]    Daily trades: 1 | Volume: $1.0k
2025-11-13 05:45:10,900 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:45:11,100 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:45:11,494 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 05:45:11,495 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(3): ðŸ”· Bearish Order Block
2025-11-13 05:45:11,495 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 05:45:11,495 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(3): ðŸ”· Bearish Order Block
2025-11-13 05:45:11,496 [INFO]    âšª No signal - HOLD
2025-11-13 05:45:11,997 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:45:12,099 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:45:12,477 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:45:12,478 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:45:12,478 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:45:12,478 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:45:12,478 [INFO]    âšª No signal - HOLD
2025-11-13 05:45:12,979 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:45:13,079 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 05:45:13,528 [INFO] ðŸŽ¯ AVAXUSDT Advanced Signal: LONG
2025-11-13 05:45:13,528 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:45:13,528 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:45:13,528 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:45:13,529 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:45:13,529 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.528 | RSI: 66.7 | OB: 1.45
2025-11-13 05:45:13,529 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:45:13,529 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:45:13,529 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:45:13,529 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:45:13,529 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:45:13,529 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:45:13,628 [INFO] âœ… Set leverage 10x for AVAXUSDT
2025-11-13 05:45:13,929 [INFO]    ðŸ’µ Current price: $17.50
2025-11-13 05:45:13,929 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:45:13,929 [INFO]       Balance: $17.84
2025-11-13 05:45:13,929 [INFO]       Price: $17.50
2025-11-13 05:45:13,929 [INFO]       Capital (fixed): $10.00
2025-11-13 05:45:13,929 [INFO]       Leverage: 10x
2025-11-13 05:45:13,929 [INFO]       Raw quantity: 5.71428571
2025-11-13 05:45:13,929 [INFO]       Formatted quantity: 6.00000000
2025-11-13 05:45:13,929 [INFO]    ðŸ“¤ Placing BUY order for 6.0 AVAXUSDT...
2025-11-13 05:45:13,930 [INFO] ðŸ“ Order: BUY AVAXUSDT
2025-11-13 05:45:13,930 [INFO]    Raw qty: 6.00000000 -> Formatted: 6.0
2025-11-13 05:45:14,283 [INFO] âœ… Order created: BUY 6.0 AVAXUSDT
2025-11-13 05:45:14,284 [INFO] ðŸ’° TRADE: OPEN LONG AVAXUSDT | Qty: 6.0 | Price: $17.50 | Score: 5 | ðŸ”· Bullish Order Block
2025-11-13 05:45:14,712 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:45:14,714 [INFO] â±ï¸ Tracking position open time for AVAXUSDT: 2025-11-13T05:45:14.714172
2025-11-13 05:45:14,714 [INFO] ðŸ“ Trade recorded: LONG 6.0 AVAXUSDT @ $17.50
2025-11-13 05:45:14,714 [INFO]    Daily trades: 2 | Volume: $2.1k
2025-11-13 05:45:14,714 [INFO]    âœ… Order placed successfully!
2025-11-13 05:45:15,215 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:45:15,317 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:45:15,692 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 05:45:15,692 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:45:15,692 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:45:15,692 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:45:15,693 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:45:15,693 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.559 | RSI: 69.4 | OB: 1.09
2025-11-13 05:45:15,693 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:45:15,694 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:45:15,694 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:45:15,694 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:45:15,694 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:45:15,694 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:45:15,793 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 05:45:16,189 [INFO]    ðŸ’µ Current price: $2.48
2025-11-13 05:45:16,189 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:45:16,189 [INFO]       Balance: $17.84
2025-11-13 05:45:16,189 [INFO]       Price: $2.48
2025-11-13 05:45:16,189 [INFO]       Capital (fixed): $10.00
2025-11-13 05:45:16,189 [INFO]       Leverage: 10x
2025-11-13 05:45:16,189 [INFO]       Raw quantity: 40.34047360
2025-11-13 05:45:16,189 [INFO]       Formatted quantity: 40.30000000
2025-11-13 05:45:16,189 [INFO]    ðŸ“¤ Placing BUY order for 40.3 XRPUSDT...
2025-11-13 05:45:16,189 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 05:45:16,189 [INFO]    Raw qty: 40.30000000 -> Formatted: 40.3
2025-11-13 05:45:16,539 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:45:16,957 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:45:16,959 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.3
2025-11-13 05:45:17,345 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:45:17,348 [ERROR]    âŒ Order placement failed!
2025-11-13 05:45:17,756 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:45:17,759 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:46:17,814 [INFO] 
============================================================
2025-11-13 05:46:17,814 [INFO] ðŸ”„ LOOP #52 - 2025-11-13 05:46:17
2025-11-13 05:46:17,814 [INFO] ============================================================
2025-11-13 05:46:17,916 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 05:46:17,916 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:46:18,016 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:46:18,411 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:46:18,411 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:46:18,411 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:46:18,411 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:46:18,412 [INFO]    âšª No signal - HOLD
2025-11-13 05:46:18,912 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:46:19,014 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 05:46:19,381 [INFO] ðŸŽ¯ ETHUSDT Advanced Signal: SHORT
2025-11-13 05:46:19,381 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:46:19,381 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:46:19,381 [INFO]       1. ðŸ“ˆ RSI Overbought
2025-11-13 05:46:19,381 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:46:19,382 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.577 | RSI: 71.9 | OB: 2.12
2025-11-13 05:46:19,382 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:46:19,382 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:46:19,382 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:46:19,382 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:46:19,382 [INFO]    ðŸ“ Top reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:46:19,382 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:46:19,481 [INFO] âœ… Set leverage 10x for ETHUSDT
2025-11-13 05:46:19,685 [INFO]    ðŸ’µ Current price: $3513.85
2025-11-13 05:46:19,686 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:46:19,686 [INFO]       Balance: $18.75
2025-11-13 05:46:19,686 [INFO]       Price: $3513.85
2025-11-13 05:46:19,686 [INFO]       Capital (fixed): $10.00
2025-11-13 05:46:19,686 [INFO]       Leverage: 10x
2025-11-13 05:46:19,686 [INFO]       Raw quantity: 0.02845881
2025-11-13 05:46:19,686 [INFO]       Formatted quantity: 0.02800000
2025-11-13 05:46:19,686 [INFO]    ðŸ“¤ Placing SELL order for 0.028 ETHUSDT...
2025-11-13 05:46:19,686 [INFO] ðŸ“ Order: SELL ETHUSDT
2025-11-13 05:46:19,686 [INFO]    Raw qty: 0.02800000 -> Formatted: 0.028
2025-11-13 05:46:20,042 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:46:20,811 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:46:20,814 [ERROR]    Symbol: ETHUSDT, Side: SELL, Qty: 0.028
2025-11-13 05:46:21,243 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:46:21,245 [ERROR]    âŒ Order placement failed!
2025-11-13 05:46:21,775 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:46:22,277 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:46:22,379 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:46:22,732 [INFO] ðŸŽ¯ SOLUSDT Advanced Signal: SHORT
2025-11-13 05:46:22,732 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:46:22,732 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:46:22,732 [INFO]       1. ðŸ”· Bearish Order Block
2025-11-13 05:46:22,732 [INFO]       2. ðŸ“ˆ RSI Overbought
2025-11-13 05:46:22,732 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.578 | RSI: 70.8 | OB: 1.09
2025-11-13 05:46:22,733 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:46:22,733 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bearish Order Block, ðŸ“ˆ RSI Overbought
2025-11-13 05:46:22,733 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:46:22,733 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:46:22,733 [INFO]    ðŸ“ Top reasons: ðŸ”· Bearish Order Block, ðŸ“ˆ RSI Overbought
2025-11-13 05:46:22,733 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:46:22,836 [INFO] âœ… Set leverage 10x for SOLUSDT
2025-11-13 05:46:23,035 [INFO]    ðŸ’µ Current price: $155.54
2025-11-13 05:46:23,036 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:46:23,036 [INFO]       Balance: $18.75
2025-11-13 05:46:23,036 [INFO]       Price: $155.54
2025-11-13 05:46:23,036 [INFO]       Capital (fixed): $10.00
2025-11-13 05:46:23,036 [INFO]       Leverage: 10x
2025-11-13 05:46:23,036 [INFO]       Raw quantity: 0.64290077
2025-11-13 05:46:23,036 [INFO]       Formatted quantity: 0.64000000
2025-11-13 05:46:23,036 [INFO]    ðŸ“¤ Placing SELL order for 0.64 SOLUSDT...
2025-11-13 05:46:23,036 [INFO] ðŸ“ Order: SELL SOLUSDT
2025-11-13 05:46:23,036 [INFO]    Raw qty: 0.64000000 -> Formatted: 0.64
2025-11-13 05:46:23,387 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:46:23,808 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:46:23,810 [ERROR]    Symbol: SOLUSDT, Side: SELL, Qty: 0.64
2025-11-13 05:46:24,190 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:46:24,192 [ERROR]    âŒ Order placement failed!
2025-11-13 05:46:27,748 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:46:28,251 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:46:28,351 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:46:28,847 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:46:28,848 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:46:28,848 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:46:28,848 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:46:28,848 [INFO]    âšª No signal - HOLD
2025-11-13 05:46:29,349 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:46:29,452 [INFO]    Current position: LONG 6.0
2025-11-13 05:46:29,452 [INFO]    Entry: $17.52 | Mark: $17.54
2025-11-13 05:46:29,452 [INFO]    PnL: 0.11% ($0.11)
2025-11-13 05:46:29,452 [INFO]    Age: 0.0h / 36.0h
2025-11-13 05:46:29,953 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:46:30,054 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:46:30,402 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 05:46:30,402 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:46:30,402 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:46:30,402 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:46:30,402 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:46:30,403 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.514 | RSI: 69.9 | OB: 2.18
2025-11-13 05:46:30,403 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:46:30,403 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:46:30,403 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:46:30,403 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:46:30,403 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:46:30,403 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:46:30,500 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 05:46:30,693 [INFO]    ðŸ’µ Current price: $2.48
2025-11-13 05:46:30,693 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:46:30,693 [INFO]       Balance: $18.75
2025-11-13 05:46:30,693 [INFO]       Price: $2.48
2025-11-13 05:46:30,693 [INFO]       Capital (fixed): $10.00
2025-11-13 05:46:30,693 [INFO]       Leverage: 10x
2025-11-13 05:46:30,693 [INFO]       Raw quantity: 40.26251158
2025-11-13 05:46:30,693 [INFO]       Formatted quantity: 40.30000000
2025-11-13 05:46:30,693 [INFO]    ðŸ“¤ Placing BUY order for 40.3 XRPUSDT...
2025-11-13 05:46:30,694 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 05:46:30,694 [INFO]    Raw qty: 40.30000000 -> Formatted: 40.3
2025-11-13 05:46:31,047 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:46:31,488 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:46:31,491 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.3
2025-11-13 05:46:31,914 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:46:31,918 [ERROR]    âŒ Order placement failed!
2025-11-13 05:46:32,297 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:46:32,299 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:47:32,343 [INFO] 
============================================================
2025-11-13 05:47:32,343 [INFO] ðŸ”„ LOOP #53 - 2025-11-13 05:47:32
2025-11-13 05:47:32,343 [INFO] ============================================================
2025-11-13 05:47:32,444 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 05:47:32,444 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:47:32,545 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:47:32,966 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:47:32,966 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:47:32,967 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:47:32,968 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:47:32,968 [INFO]    âšª No signal - HOLD
2025-11-13 05:47:33,469 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:47:33,570 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 05:47:33,969 [INFO] ðŸŽ¯ ETHUSDT Advanced Signal: SHORT
2025-11-13 05:47:33,969 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:47:33,969 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:47:33,969 [INFO]       1. ðŸ“ˆ RSI Overbought
2025-11-13 05:47:33,969 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:47:33,969 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.585 | RSI: 72.4 | OB: 7.69
2025-11-13 05:47:33,970 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:47:33,970 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:47:33,970 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:47:33,970 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:47:33,970 [INFO]    ðŸ“ Top reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:47:33,970 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:47:34,072 [INFO] âœ… Set leverage 10x for ETHUSDT
2025-11-13 05:47:34,271 [INFO]    ðŸ’µ Current price: $3517.45
2025-11-13 05:47:34,271 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:47:34,272 [INFO]       Balance: $18.75
2025-11-13 05:47:34,272 [INFO]       Price: $3517.45
2025-11-13 05:47:34,272 [INFO]       Capital (fixed): $10.00
2025-11-13 05:47:34,272 [INFO]       Leverage: 10x
2025-11-13 05:47:34,272 [INFO]       Raw quantity: 0.02842969
2025-11-13 05:47:34,272 [INFO]       Formatted quantity: 0.02800000
2025-11-13 05:47:34,272 [INFO]    ðŸ“¤ Placing SELL order for 0.028 ETHUSDT...
2025-11-13 05:47:34,272 [INFO] ðŸ“ Order: SELL ETHUSDT
2025-11-13 05:47:34,272 [INFO]    Raw qty: 0.02800000 -> Formatted: 0.028
2025-11-13 05:47:34,627 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:47:35,326 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:47:35,329 [ERROR]    Symbol: ETHUSDT, Side: SELL, Qty: 0.028
2025-11-13 05:47:35,718 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:47:35,720 [ERROR]    âŒ Order placement failed!
2025-11-13 05:47:36,152 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:47:36,654 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:47:36,757 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:47:37,217 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:47:37,218 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:47:37,219 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:47:37,219 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:47:37,219 [INFO]    âšª No signal - HOLD
2025-11-13 05:47:37,720 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:47:37,822 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:47:38,183 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:47:38,184 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:47:38,184 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:47:38,184 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:47:38,184 [INFO]    âšª No signal - HOLD
2025-11-13 05:47:38,685 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:47:38,785 [INFO]    Current position: LONG 6.0
2025-11-13 05:47:38,785 [INFO]    Entry: $17.52 | Mark: $17.53
2025-11-13 05:47:38,785 [INFO]    PnL: 0.05% ($0.05)
2025-11-13 05:47:38,785 [INFO]    Age: 0.0h / 36.0h
2025-11-13 05:47:39,286 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:47:39,387 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:47:39,866 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 05:47:39,867 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:47:39,867 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:47:39,867 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:47:39,867 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:47:39,867 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.581 | RSI: 70.6 | OB: 1.17
2025-11-13 05:47:39,868 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:47:39,868 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:47:39,868 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:47:39,868 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:47:39,868 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:47:39,868 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:47:40,062 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 05:47:40,272 [INFO]    ðŸ’µ Current price: $2.49
2025-11-13 05:47:40,273 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:47:40,273 [INFO]       Balance: $18.75
2025-11-13 05:47:40,273 [INFO]       Price: $2.49
2025-11-13 05:47:40,273 [INFO]       Capital (fixed): $10.00
2025-11-13 05:47:40,273 [INFO]       Leverage: 10x
2025-11-13 05:47:40,273 [INFO]       Raw quantity: 40.23659116
2025-11-13 05:47:40,273 [INFO]       Formatted quantity: 40.20000000
2025-11-13 05:47:40,273 [INFO]    ðŸ“¤ Placing BUY order for 40.2 XRPUSDT...
2025-11-13 05:47:40,273 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 05:47:40,273 [INFO]    Raw qty: 40.20000000 -> Formatted: 40.2
2025-11-13 05:47:40,725 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:47:41,121 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:47:41,122 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.2
2025-11-13 05:47:41,500 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:47:41,509 [ERROR]    âŒ Order placement failed!
2025-11-13 05:47:41,887 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:47:41,889 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:48:41,945 [INFO] 
============================================================
2025-11-13 05:48:41,947 [INFO] ðŸ”„ LOOP #54 - 2025-11-13 05:48:41
2025-11-13 05:48:41,947 [INFO] ============================================================
2025-11-13 05:48:42,051 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 05:48:42,052 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:48:42,156 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:48:42,665 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:48:42,677 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:48:42,678 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:48:42,678 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:48:42,678 [INFO]    âšª No signal - HOLD
2025-11-13 05:48:43,179 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:48:43,277 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 05:48:43,740 [INFO] ðŸŽ¯ ETHUSDT Advanced Signal: SHORT
2025-11-13 05:48:43,741 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:48:43,741 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:48:43,741 [INFO]       1. ðŸ“ˆ RSI Overbought
2025-11-13 05:48:43,741 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:48:43,741 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.560 | RSI: 72.5 | OB: 8.70
2025-11-13 05:48:43,746 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:48:43,746 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:48:43,746 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:48:43,747 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:48:43,747 [INFO]    ðŸ“ Top reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:48:43,747 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:48:43,849 [INFO] âœ… Set leverage 10x for ETHUSDT
2025-11-13 05:48:44,053 [INFO]    ðŸ’µ Current price: $3519.90
2025-11-13 05:48:44,054 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:48:44,054 [INFO]       Balance: $18.75
2025-11-13 05:48:44,054 [INFO]       Price: $3519.90
2025-11-13 05:48:44,054 [INFO]       Capital (fixed): $10.00
2025-11-13 05:48:44,054 [INFO]       Leverage: 10x
2025-11-13 05:48:44,054 [INFO]       Raw quantity: 0.02840990
2025-11-13 05:48:44,054 [INFO]       Formatted quantity: 0.02800000
2025-11-13 05:48:44,054 [INFO]    ðŸ“¤ Placing SELL order for 0.028 ETHUSDT...
2025-11-13 05:48:44,054 [INFO] ðŸ“ Order: SELL ETHUSDT
2025-11-13 05:48:44,055 [INFO]    Raw qty: 0.02800000 -> Formatted: 0.028
2025-11-13 05:48:44,404 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:48:45,587 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:48:45,589 [ERROR]    Symbol: ETHUSDT, Side: SELL, Qty: 0.028
2025-11-13 05:48:45,990 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:48:45,992 [ERROR]    âŒ Order placement failed!
2025-11-13 05:48:46,433 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:48:46,938 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:48:47,041 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:48:47,597 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:48:47,606 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:48:47,607 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:48:47,607 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:48:47,607 [INFO]    âšª No signal - HOLD
2025-11-13 05:48:48,108 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:48:48,208 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:48:48,772 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:48:48,772 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:48:48,773 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:48:48,773 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:48:48,773 [INFO]    âšª No signal - HOLD
2025-11-13 05:48:49,274 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:48:49,376 [INFO]    Current position: LONG 6.0
2025-11-13 05:48:49,376 [INFO]    Entry: $17.52 | Mark: $17.54
2025-11-13 05:48:49,376 [INFO]    PnL: 0.13% ($0.14)
2025-11-13 05:48:49,376 [INFO]    Age: 0.1h / 36.0h
2025-11-13 05:48:49,877 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:48:49,985 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:48:50,399 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 05:48:50,400 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:48:50,400 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:48:50,401 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:48:50,401 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:48:50,401 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.597 | RSI: 71.2 | OB: 1.26
2025-11-13 05:48:50,402 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:48:50,402 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:48:50,402 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:48:50,403 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:48:50,403 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:48:50,403 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:48:50,505 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 05:48:50,801 [INFO]    ðŸ’µ Current price: $2.49
2025-11-13 05:48:50,801 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:48:50,801 [INFO]       Balance: $18.75
2025-11-13 05:48:50,802 [INFO]       Price: $2.49
2025-11-13 05:48:50,802 [INFO]       Capital (fixed): $10.00
2025-11-13 05:48:50,802 [INFO]       Leverage: 10x
2025-11-13 05:48:50,802 [INFO]       Raw quantity: 40.17516371
2025-11-13 05:48:50,802 [INFO]       Formatted quantity: 40.20000000
2025-11-13 05:48:50,802 [INFO]    ðŸ“¤ Placing BUY order for 40.2 XRPUSDT...
2025-11-13 05:48:50,802 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 05:48:50,802 [INFO]    Raw qty: 40.20000000 -> Formatted: 40.2
2025-11-13 05:48:51,152 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:48:51,541 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:48:51,546 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.2
2025-11-13 05:48:51,984 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:48:51,992 [ERROR]    âŒ Order placement failed!
2025-11-13 05:48:52,382 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:48:52,384 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:49:52,436 [INFO] 
============================================================
2025-11-13 05:49:52,437 [INFO] ðŸ”„ LOOP #55 - 2025-11-13 05:49:52
2025-11-13 05:49:52,437 [INFO] ============================================================
2025-11-13 05:49:53,212 [INFO] ðŸ’“ Bot alive - Loop #55 - Active positions: 1
2025-11-13 05:49:53,312 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 05:49:53,312 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:49:53,412 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:49:53,770 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:49:53,770 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:49:53,771 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:49:53,771 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:49:53,771 [INFO]    âšª No signal - HOLD
2025-11-13 05:49:54,272 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:49:54,371 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 05:49:54,826 [INFO] ðŸŽ¯ ETHUSDT Advanced Signal: SHORT
2025-11-13 05:49:54,827 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:49:54,827 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:49:54,827 [INFO]       1. ðŸ“ˆ RSI Overbought
2025-11-13 05:49:54,827 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:49:54,827 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.581 | RSI: 73.4 | OB: 4.79
2025-11-13 05:49:54,827 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:49:54,828 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:49:54,828 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:49:54,828 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:49:54,828 [INFO]    ðŸ“ Top reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:49:54,828 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:49:54,923 [INFO] âœ… Set leverage 10x for ETHUSDT
2025-11-13 05:49:55,125 [INFO]    ðŸ’µ Current price: $3522.00
2025-11-13 05:49:55,125 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:49:55,125 [INFO]       Balance: $18.75
2025-11-13 05:49:55,125 [INFO]       Price: $3522.00
2025-11-13 05:49:55,125 [INFO]       Capital (fixed): $10.00
2025-11-13 05:49:55,125 [INFO]       Leverage: 10x
2025-11-13 05:49:55,125 [INFO]       Raw quantity: 0.02839296
2025-11-13 05:49:55,125 [INFO]       Formatted quantity: 0.02800000
2025-11-13 05:49:55,125 [INFO]    ðŸ“¤ Placing SELL order for 0.028 ETHUSDT...
2025-11-13 05:49:55,126 [INFO] ðŸ“ Order: SELL ETHUSDT
2025-11-13 05:49:55,126 [INFO]    Raw qty: 0.02800000 -> Formatted: 0.028
2025-11-13 05:49:55,479 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:49:56,206 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:49:56,208 [ERROR]    Symbol: ETHUSDT, Side: SELL, Qty: 0.028
2025-11-13 05:49:56,643 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:49:56,644 [ERROR]    âŒ Order placement failed!
2025-11-13 05:49:57,079 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:49:57,582 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:49:57,780 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:49:58,127 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:49:58,128 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:49:58,128 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:49:58,128 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:49:58,128 [INFO]    âšª No signal - HOLD
2025-11-13 05:49:58,629 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:49:58,828 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:49:59,180 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:49:59,180 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:49:59,181 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:49:59,181 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:49:59,181 [INFO]    âšª No signal - HOLD
2025-11-13 05:49:59,682 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:49:59,784 [INFO]    Current position: LONG 6.0
2025-11-13 05:49:59,784 [INFO]    Entry: $17.52 | Mark: $17.54
2025-11-13 05:49:59,784 [INFO]    PnL: 0.12% ($0.12)
2025-11-13 05:49:59,784 [INFO]    Age: 0.1h / 36.0h
2025-11-13 05:50:00,285 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:50:00,389 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:50:00,981 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 05:50:00,981 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:50:00,981 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:50:00,981 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:50:00,982 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:50:00,982 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.589 | RSI: 71.4 | OB: 1.43
2025-11-13 05:50:00,982 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:50:00,982 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:50:00,982 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:50:00,982 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:50:00,982 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:50:00,982 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:50:01,079 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 05:50:01,280 [INFO]    ðŸ’µ Current price: $2.49
2025-11-13 05:50:01,280 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:50:01,280 [INFO]       Balance: $18.75
2025-11-13 05:50:01,280 [INFO]       Price: $2.49
2025-11-13 05:50:01,280 [INFO]       Capital (fixed): $10.00
2025-11-13 05:50:01,280 [INFO]       Leverage: 10x
2025-11-13 05:50:01,281 [INFO]       Raw quantity: 40.15257980
2025-11-13 05:50:01,281 [INFO]       Formatted quantity: 40.20000000
2025-11-13 05:50:01,281 [INFO]    ðŸ“¤ Placing BUY order for 40.2 XRPUSDT...
2025-11-13 05:50:01,281 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 05:50:01,281 [INFO]    Raw qty: 40.20000000 -> Formatted: 40.2
2025-11-13 05:50:01,633 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:50:02,065 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:50:02,067 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.2
2025-11-13 05:50:02,508 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:50:02,510 [ERROR]    âŒ Order placement failed!
2025-11-13 05:50:02,917 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:50:02,920 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:51:02,977 [INFO] 
============================================================
2025-11-13 05:51:02,977 [INFO] ðŸ”„ LOOP #56 - 2025-11-13 05:51:02
2025-11-13 05:51:02,978 [INFO] ============================================================
2025-11-13 05:51:03,080 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 05:51:03,080 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:51:03,182 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:51:03,599 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:51:03,599 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:51:03,600 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:51:03,600 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:51:03,600 [INFO]    âšª No signal - HOLD
2025-11-13 05:51:04,101 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:51:04,202 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 05:51:04,562 [INFO] ðŸŽ¯ ETHUSDT Advanced Signal: SHORT
2025-11-13 05:51:04,562 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:51:04,562 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:51:04,562 [INFO]       1. ðŸ“ˆ RSI Overbought
2025-11-13 05:51:04,562 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:51:04,562 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.570 | RSI: 74.0 | OB: 2.90
2025-11-13 05:51:04,563 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:51:04,563 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:51:04,563 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:51:04,563 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:51:04,563 [INFO]    ðŸ“ Top reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:51:04,563 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:51:04,663 [INFO] âœ… Set leverage 10x for ETHUSDT
2025-11-13 05:51:04,859 [INFO]    ðŸ’µ Current price: $3532.20
2025-11-13 05:51:04,859 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:51:04,860 [INFO]       Balance: $18.75
2025-11-13 05:51:04,860 [INFO]       Price: $3532.20
2025-11-13 05:51:04,860 [INFO]       Capital (fixed): $10.00
2025-11-13 05:51:04,860 [INFO]       Leverage: 10x
2025-11-13 05:51:04,860 [INFO]       Raw quantity: 0.02831097
2025-11-13 05:51:04,860 [INFO]       Formatted quantity: 0.02800000
2025-11-13 05:51:04,860 [INFO]    ðŸ“¤ Placing SELL order for 0.028 ETHUSDT...
2025-11-13 05:51:04,860 [INFO] ðŸ“ Order: SELL ETHUSDT
2025-11-13 05:51:04,860 [INFO]    Raw qty: 0.02800000 -> Formatted: 0.028
2025-11-13 05:51:05,214 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:51:05,997 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:51:05,999 [ERROR]    Symbol: ETHUSDT, Side: SELL, Qty: 0.028
2025-11-13 05:51:06,434 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:51:06,435 [ERROR]    âŒ Order placement failed!
2025-11-13 05:51:07,348 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:51:07,850 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:51:07,948 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:51:08,311 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:51:08,311 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:51:08,311 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:51:08,312 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:51:08,312 [INFO]    âšª No signal - HOLD
2025-11-13 05:51:08,812 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:51:08,912 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:51:09,271 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:51:09,271 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:51:09,272 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:51:09,272 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:51:09,272 [INFO]    âšª No signal - HOLD
2025-11-13 05:51:09,773 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:51:09,872 [INFO]    Current position: LONG 6.0
2025-11-13 05:51:09,872 [INFO]    Entry: $17.52 | Mark: $17.57
2025-11-13 05:51:09,872 [INFO]    PnL: 0.26% ($0.28)
2025-11-13 05:51:09,872 [INFO]    Age: 0.1h / 36.0h
2025-11-13 05:51:10,373 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:51:10,472 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:51:10,934 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 05:51:10,934 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:51:10,934 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:51:10,935 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:51:10,935 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:51:10,935 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.560 | RSI: 71.8 | OB: 2.05
2025-11-13 05:51:10,935 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:51:10,935 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:51:10,935 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:51:10,935 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:51:10,935 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:51:10,935 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:51:11,035 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 05:51:11,336 [INFO]    ðŸ’µ Current price: $2.49
2025-11-13 05:51:11,336 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:51:11,336 [INFO]       Balance: $18.75
2025-11-13 05:51:11,336 [INFO]       Price: $2.49
2025-11-13 05:51:11,336 [INFO]       Capital (fixed): $10.00
2025-11-13 05:51:11,336 [INFO]       Leverage: 10x
2025-11-13 05:51:11,336 [INFO]       Raw quantity: 40.11231448
2025-11-13 05:51:11,336 [INFO]       Formatted quantity: 40.10000000
2025-11-13 05:51:11,337 [INFO]    ðŸ“¤ Placing BUY order for 40.1 XRPUSDT...
2025-11-13 05:51:11,337 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 05:51:11,337 [INFO]    Raw qty: 40.10000000 -> Formatted: 40.1
2025-11-13 05:51:11,784 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:51:12,247 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:51:12,250 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.1
2025-11-13 05:51:12,683 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:51:12,685 [ERROR]    âŒ Order placement failed!
2025-11-13 05:51:13,082 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:51:13,084 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:52:13,109 [INFO] 
============================================================
2025-11-13 05:52:13,110 [INFO] ðŸ”„ LOOP #57 - 2025-11-13 05:52:13
2025-11-13 05:52:13,110 [INFO] ============================================================
2025-11-13 05:52:13,212 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 05:52:13,213 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:52:13,312 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:52:13,694 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:52:13,694 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:52:13,694 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:52:13,695 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:52:13,695 [INFO]    âšª No signal - HOLD
2025-11-13 05:52:14,195 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:52:14,295 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 05:52:14,644 [INFO] ðŸŽ¯ ETHUSDT Advanced Signal: SHORT
2025-11-13 05:52:14,644 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:52:14,645 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:52:14,645 [INFO]       1. ðŸ“ˆ RSI Overbought
2025-11-13 05:52:14,645 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:52:14,645 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.552 | RSI: 73.2 | OB: 1.69
2025-11-13 05:52:14,645 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:52:14,645 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:52:14,645 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:52:14,645 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:52:14,646 [INFO]    ðŸ“ Top reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:52:14,646 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:52:14,743 [INFO] âœ… Set leverage 10x for ETHUSDT
2025-11-13 05:52:14,937 [INFO]    ðŸ’µ Current price: $3523.65
2025-11-13 05:52:14,938 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:52:14,938 [INFO]       Balance: $18.75
2025-11-13 05:52:14,938 [INFO]       Price: $3523.65
2025-11-13 05:52:14,938 [INFO]       Capital (fixed): $10.00
2025-11-13 05:52:14,938 [INFO]       Leverage: 10x
2025-11-13 05:52:14,938 [INFO]       Raw quantity: 0.02837966
2025-11-13 05:52:14,938 [INFO]       Formatted quantity: 0.02800000
2025-11-13 05:52:14,938 [INFO]    ðŸ“¤ Placing SELL order for 0.028 ETHUSDT...
2025-11-13 05:52:14,938 [INFO] ðŸ“ Order: SELL ETHUSDT
2025-11-13 05:52:14,938 [INFO]    Raw qty: 0.02800000 -> Formatted: 0.028
2025-11-13 05:52:15,387 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:52:16,128 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:52:16,130 [ERROR]    Symbol: ETHUSDT, Side: SELL, Qty: 0.028
2025-11-13 05:52:16,622 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:52:16,624 [ERROR]    âŒ Order placement failed!
2025-11-13 05:52:17,075 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:52:17,577 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:52:17,680 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:52:18,040 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:52:18,040 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:52:18,041 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:52:18,041 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:52:18,041 [INFO]    âšª No signal - HOLD
2025-11-13 05:52:18,542 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:52:18,641 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:52:18,995 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:52:18,995 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:52:18,996 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:52:18,996 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:52:18,996 [INFO]    âšª No signal - HOLD
2025-11-13 05:52:19,497 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:52:19,694 [INFO]    Current position: LONG 6.0
2025-11-13 05:52:19,694 [INFO]    Entry: $17.52 | Mark: $17.56
2025-11-13 05:52:19,694 [INFO]    PnL: 0.23% ($0.24)
2025-11-13 05:52:19,694 [INFO]    Age: 0.1h / 36.0h
2025-11-13 05:52:20,195 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:52:20,316 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:52:20,661 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 05:52:20,662 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:52:20,662 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:52:20,662 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:52:20,662 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:52:20,662 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.557 | RSI: 71.5 | OB: 0.56
2025-11-13 05:52:20,662 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:52:20,663 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:52:20,663 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:52:20,663 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:52:20,663 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:52:20,663 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:52:20,864 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 05:52:21,062 [INFO]    ðŸ’µ Current price: $2.49
2025-11-13 05:52:21,062 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:52:21,063 [INFO]       Balance: $18.75
2025-11-13 05:52:21,063 [INFO]       Price: $2.49
2025-11-13 05:52:21,063 [INFO]       Capital (fixed): $10.00
2025-11-13 05:52:21,063 [INFO]       Leverage: 10x
2025-11-13 05:52:21,063 [INFO]       Raw quantity: 40.14290876
2025-11-13 05:52:21,063 [INFO]       Formatted quantity: 40.10000000
2025-11-13 05:52:21,063 [INFO]    ðŸ“¤ Placing BUY order for 40.1 XRPUSDT...
2025-11-13 05:52:21,063 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 05:52:21,063 [INFO]    Raw qty: 40.10000000 -> Formatted: 40.1
2025-11-13 05:52:21,415 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:52:21,844 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:52:21,846 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.1
2025-11-13 05:52:22,272 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:52:22,273 [ERROR]    âŒ Order placement failed!
2025-11-13 05:52:22,729 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:52:22,730 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:53:22,791 [INFO] 
============================================================
2025-11-13 05:53:22,791 [INFO] ðŸ”„ LOOP #58 - 2025-11-13 05:53:22
2025-11-13 05:53:22,791 [INFO] ============================================================
2025-11-13 05:53:22,892 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 05:53:22,892 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:53:22,992 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:53:23,401 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:53:23,401 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:53:23,402 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:53:23,402 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:53:23,402 [INFO]    âšª No signal - HOLD
2025-11-13 05:53:23,903 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:53:24,003 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 05:53:24,359 [INFO] ðŸŽ¯ ETHUSDT Advanced Signal: SHORT
2025-11-13 05:53:24,359 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:53:24,359 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:53:24,359 [INFO]       1. ðŸ“ˆ RSI Overbought
2025-11-13 05:53:24,359 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:53:24,360 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.552 | RSI: 73.9 | OB: 2.15
2025-11-13 05:53:24,360 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:53:24,360 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:53:24,360 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:53:24,360 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:53:24,360 [INFO]    ðŸ“ Top reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:53:24,360 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:53:24,459 [INFO] âœ… Set leverage 10x for ETHUSDT
2025-11-13 05:53:24,654 [INFO]    ðŸ’µ Current price: $3527.35
2025-11-13 05:53:24,654 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:53:24,655 [INFO]       Balance: $18.75
2025-11-13 05:53:24,655 [INFO]       Price: $3527.35
2025-11-13 05:53:24,655 [INFO]       Capital (fixed): $10.00
2025-11-13 05:53:24,655 [INFO]       Leverage: 10x
2025-11-13 05:53:24,655 [INFO]       Raw quantity: 0.02834989
2025-11-13 05:53:24,655 [INFO]       Formatted quantity: 0.02800000
2025-11-13 05:53:24,655 [INFO]    ðŸ“¤ Placing SELL order for 0.028 ETHUSDT...
2025-11-13 05:53:24,655 [INFO] ðŸ“ Order: SELL ETHUSDT
2025-11-13 05:53:24,655 [INFO]    Raw qty: 0.02800000 -> Formatted: 0.028
2025-11-13 05:53:25,016 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:53:25,783 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:53:25,785 [ERROR]    Symbol: ETHUSDT, Side: SELL, Qty: 0.028
2025-11-13 05:53:26,182 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:53:26,184 [ERROR]    âŒ Order placement failed!
2025-11-13 05:53:26,598 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:53:27,100 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:53:27,199 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:53:27,577 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:53:27,577 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:53:27,578 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:53:27,578 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:53:27,578 [INFO]    âšª No signal - HOLD
2025-11-13 05:53:28,079 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:53:28,180 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:53:28,539 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:53:28,539 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:53:28,540 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:53:28,540 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:53:28,540 [INFO]    âšª No signal - HOLD
2025-11-13 05:53:29,041 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:53:29,240 [INFO]    Current position: LONG 6.0
2025-11-13 05:53:29,241 [INFO]    Entry: $17.52 | Mark: $17.55
2025-11-13 05:53:29,241 [INFO]    PnL: 0.19% ($0.20)
2025-11-13 05:53:29,241 [INFO]    Age: 0.1h / 36.0h
2025-11-13 05:53:29,742 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:53:29,921 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:53:30,284 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 05:53:30,285 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:53:30,285 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:53:30,285 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:53:30,285 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:53:30,285 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.535 | RSI: 71.7 | OB: 0.61
2025-11-13 05:53:30,285 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:53:30,286 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:53:30,286 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:53:30,286 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:53:30,286 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:53:30,286 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:53:30,386 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 05:53:30,582 [INFO]    ðŸ’µ Current price: $2.49
2025-11-13 05:53:30,583 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:53:30,583 [INFO]       Balance: $18.75
2025-11-13 05:53:30,583 [INFO]       Price: $2.49
2025-11-13 05:53:30,583 [INFO]       Capital (fixed): $10.00
2025-11-13 05:53:30,583 [INFO]       Leverage: 10x
2025-11-13 05:53:30,583 [INFO]       Raw quantity: 40.14452027
2025-11-13 05:53:30,583 [INFO]       Formatted quantity: 40.10000000
2025-11-13 05:53:30,583 [INFO]    ðŸ“¤ Placing BUY order for 40.1 XRPUSDT...
2025-11-13 05:53:30,583 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 05:53:30,583 [INFO]    Raw qty: 40.10000000 -> Formatted: 40.1
2025-11-13 05:53:30,935 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:53:31,344 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:53:31,346 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.1
2025-11-13 05:53:31,797 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:53:31,799 [ERROR]    âŒ Order placement failed!
2025-11-13 05:53:32,225 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:53:32,227 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:54:32,287 [INFO] 
============================================================
2025-11-13 05:54:32,288 [INFO] ðŸ”„ LOOP #59 - 2025-11-13 05:54:32
2025-11-13 05:54:32,288 [INFO] ============================================================
2025-11-13 05:54:32,392 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 05:54:32,393 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:54:32,494 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:54:32,889 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:54:32,890 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:54:32,890 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:54:32,890 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:54:32,890 [INFO]    âšª No signal - HOLD
2025-11-13 05:54:33,391 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:54:33,492 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 05:54:33,853 [INFO] ðŸŽ¯ ETHUSDT Advanced Signal: SHORT
2025-11-13 05:54:33,853 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:54:33,853 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:54:33,853 [INFO]       1. ðŸ“ˆ RSI Overbought
2025-11-13 05:54:33,853 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:54:33,853 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.572 | RSI: 73.8 | OB: 2.98
2025-11-13 05:54:33,854 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:54:33,854 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:54:33,854 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:54:33,854 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:54:33,854 [INFO]    ðŸ“ Top reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:54:33,854 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:54:33,951 [INFO] âœ… Set leverage 10x for ETHUSDT
2025-11-13 05:54:34,149 [INFO]    ðŸ’µ Current price: $3530.30
2025-11-13 05:54:34,150 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:54:34,150 [INFO]       Balance: $18.75
2025-11-13 05:54:34,150 [INFO]       Price: $3530.30
2025-11-13 05:54:34,150 [INFO]       Capital (fixed): $10.00
2025-11-13 05:54:34,150 [INFO]       Leverage: 10x
2025-11-13 05:54:34,150 [INFO]       Raw quantity: 0.02832620
2025-11-13 05:54:34,150 [INFO]       Formatted quantity: 0.02800000
2025-11-13 05:54:34,150 [INFO]    ðŸ“¤ Placing SELL order for 0.028 ETHUSDT...
2025-11-13 05:54:34,150 [INFO] ðŸ“ Order: SELL ETHUSDT
2025-11-13 05:54:34,150 [INFO]    Raw qty: 0.02800000 -> Formatted: 0.028
2025-11-13 05:54:34,501 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:54:35,260 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:54:35,261 [ERROR]    Symbol: ETHUSDT, Side: SELL, Qty: 0.028
2025-11-13 05:54:35,644 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:54:35,646 [ERROR]    âŒ Order placement failed!
2025-11-13 05:54:36,028 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:54:36,530 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:54:36,631 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:54:37,086 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:54:37,086 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:54:37,087 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:54:37,087 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:54:37,087 [INFO]    âšª No signal - HOLD
2025-11-13 05:54:37,588 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:54:37,688 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:54:38,179 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:54:38,179 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:54:38,180 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:54:38,180 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:54:38,181 [INFO]    âšª No signal - HOLD
2025-11-13 05:54:38,681 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:54:38,783 [INFO]    Current position: LONG 6.0
2025-11-13 05:54:38,783 [INFO]    Entry: $17.52 | Mark: $17.57
2025-11-13 05:54:38,783 [INFO]    PnL: 0.27% ($0.28)
2025-11-13 05:54:38,783 [INFO]    Age: 0.2h / 36.0h
2025-11-13 05:54:39,284 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:54:39,386 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:54:39,754 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 05:54:39,755 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:54:39,755 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:54:39,755 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:54:39,755 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:54:39,755 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.524 | RSI: 72.0 | OB: 0.89
2025-11-13 05:54:39,756 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:54:39,756 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:54:39,756 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:54:39,756 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:54:39,756 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:54:39,756 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:54:39,856 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 05:54:40,054 [INFO]    ðŸ’µ Current price: $2.50
2025-11-13 05:54:40,054 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:54:40,054 [INFO]       Balance: $18.75
2025-11-13 05:54:40,054 [INFO]       Price: $2.50
2025-11-13 05:54:40,054 [INFO]       Capital (fixed): $10.00
2025-11-13 05:54:40,054 [INFO]       Leverage: 10x
2025-11-13 05:54:40,055 [INFO]       Raw quantity: 40.05607851
2025-11-13 05:54:40,055 [INFO]       Formatted quantity: 40.10000000
2025-11-13 05:54:40,055 [INFO]    ðŸ“¤ Placing BUY order for 40.1 XRPUSDT...
2025-11-13 05:54:40,055 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 05:54:40,055 [INFO]    Raw qty: 40.10000000 -> Formatted: 40.1
2025-11-13 05:54:40,408 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:54:40,802 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:54:40,805 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.1
2025-11-13 05:54:41,192 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:54:41,194 [ERROR]    âŒ Order placement failed!
2025-11-13 05:54:41,582 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:54:41,584 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:55:41,645 [INFO] 
============================================================
2025-11-13 05:55:41,645 [INFO] ðŸ”„ LOOP #60 - 2025-11-13 05:55:41
2025-11-13 05:55:41,645 [INFO] ============================================================
2025-11-13 05:55:42,239 [INFO] ðŸ’“ Bot alive - Loop #60 - Active positions: 1
2025-11-13 05:55:42,344 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 05:55:42,344 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:55:42,443 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:55:42,802 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 05:55:42,803 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:55:42,803 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:55:42,803 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 05:55:42,803 [INFO]       2. ðŸ“ˆ Volume Spike
2025-11-13 05:55:42,803 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.589 | RSI: 63.5 | OB: 5.27
2025-11-13 05:55:42,803 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=4
2025-11-13 05:55:42,803 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 05:55:42,803 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:55:42,804 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:55:42,804 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 05:55:42,804 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:55:42,903 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 05:55:43,103 [INFO]    ðŸ’µ Current price: $103132.90
2025-11-13 05:55:43,104 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:55:43,104 [INFO]       Balance: $18.75
2025-11-13 05:55:43,104 [INFO]       Price: $103132.90
2025-11-13 05:55:43,104 [INFO]       Capital (fixed): $10.00
2025-11-13 05:55:43,104 [INFO]       Leverage: 10x
2025-11-13 05:55:43,104 [INFO]       Raw quantity: 0.00096962
2025-11-13 05:55:43,104 [INFO]       Formatted quantity: 0.00100000
2025-11-13 05:55:43,104 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 05:55:43,104 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 05:55:43,104 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 05:55:43,456 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:55:44,204 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:55:44,206 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 05:55:44,601 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:55:44,603 [ERROR]    âŒ Order placement failed!
2025-11-13 05:55:45,004 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:55:45,507 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:55:45,606 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 05:55:45,993 [INFO] ðŸŽ¯ ETHUSDT Advanced Signal: SHORT
2025-11-13 05:55:45,993 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:55:45,993 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:55:45,993 [INFO]       1. ðŸ“ˆ RSI Overbought
2025-11-13 05:55:45,993 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:55:45,993 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.582 | RSI: 74.3 | OB: 2.84
2025-11-13 05:55:45,994 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:55:45,994 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:55:45,995 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:55:45,995 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:55:45,995 [INFO]    ðŸ“ Top reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:55:45,995 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:55:46,092 [INFO] âœ… Set leverage 10x for ETHUSDT
2025-11-13 05:55:46,288 [INFO]    ðŸ’µ Current price: $3532.30
2025-11-13 05:55:46,288 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:55:46,288 [INFO]       Balance: $18.75
2025-11-13 05:55:46,288 [INFO]       Price: $3532.30
2025-11-13 05:55:46,288 [INFO]       Capital (fixed): $10.00
2025-11-13 05:55:46,288 [INFO]       Leverage: 10x
2025-11-13 05:55:46,288 [INFO]       Raw quantity: 0.02831017
2025-11-13 05:55:46,288 [INFO]       Formatted quantity: 0.02800000
2025-11-13 05:55:46,289 [INFO]    ðŸ“¤ Placing SELL order for 0.028 ETHUSDT...
2025-11-13 05:55:46,289 [INFO] ðŸ“ Order: SELL ETHUSDT
2025-11-13 05:55:46,289 [INFO]    Raw qty: 0.02800000 -> Formatted: 0.028
2025-11-13 05:55:46,642 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:55:47,050 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:55:47,052 [ERROR]    Symbol: ETHUSDT, Side: SELL, Qty: 0.028
2025-11-13 05:55:47,439 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:55:47,441 [ERROR]    âŒ Order placement failed!
2025-11-13 05:55:51,039 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:55:51,541 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:55:51,640 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:55:51,990 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:55:51,991 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:55:51,991 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:55:51,991 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:55:51,991 [INFO]    âšª No signal - HOLD
2025-11-13 05:55:52,492 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:55:52,593 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:55:52,955 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:55:52,955 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:55:52,955 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:55:52,956 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:55:52,956 [INFO]    âšª No signal - HOLD
2025-11-13 05:55:53,457 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:55:53,561 [INFO]    Current position: LONG 6.0
2025-11-13 05:55:53,562 [INFO]    Entry: $17.52 | Mark: $17.61
2025-11-13 05:55:53,562 [INFO]    PnL: 0.50% ($0.53)
2025-11-13 05:55:53,562 [INFO]    Age: 0.2h / 36.0h
2025-11-13 05:55:54,063 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:55:54,161 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:55:54,519 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 05:55:54,519 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:55:54,519 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:55:54,519 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:55:54,519 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:55:54,520 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.529 | RSI: 72.2 | OB: 1.06
2025-11-13 05:55:54,520 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:55:54,520 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:55:54,520 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:55:54,520 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:55:54,520 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:55:54,520 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:55:54,719 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 05:55:54,916 [INFO]    ðŸ’µ Current price: $2.49
2025-11-13 05:55:54,917 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:55:54,917 [INFO]       Balance: $18.75
2025-11-13 05:55:54,917 [INFO]       Price: $2.49
2025-11-13 05:55:54,917 [INFO]       Capital (fixed): $10.00
2025-11-13 05:55:54,917 [INFO]       Leverage: 10x
2025-11-13 05:55:54,917 [INFO]       Raw quantity: 40.09140841
2025-11-13 05:55:54,917 [INFO]       Formatted quantity: 40.10000000
2025-11-13 05:55:54,917 [INFO]    ðŸ“¤ Placing BUY order for 40.1 XRPUSDT...
2025-11-13 05:55:54,918 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 05:55:54,918 [INFO]    Raw qty: 40.10000000 -> Formatted: 40.1
2025-11-13 05:55:55,269 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:55:55,654 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:55:55,656 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.1
2025-11-13 05:55:56,050 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:55:56,052 [ERROR]    âŒ Order placement failed!
2025-11-13 05:55:56,441 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:55:57,035 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:56:57,090 [INFO] 
============================================================
2025-11-13 05:56:57,090 [INFO] ðŸ”„ LOOP #61 - 2025-11-13 05:56:57
2025-11-13 05:56:57,090 [INFO] ============================================================
2025-11-13 05:56:57,194 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 05:56:57,194 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:56:57,296 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:56:57,677 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 05:56:57,678 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:56:57,678 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:56:57,678 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 05:56:57,678 [INFO]       2. ðŸ“ˆ Volume Spike
2025-11-13 05:56:57,678 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.585 | RSI: 64.0 | OB: 1.01
2025-11-13 05:56:57,679 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=4
2025-11-13 05:56:57,679 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 05:56:57,679 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:56:57,680 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:56:57,680 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 05:56:57,680 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:56:57,779 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 05:56:57,986 [INFO]    ðŸ’µ Current price: $103191.40
2025-11-13 05:56:57,986 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:56:57,986 [INFO]       Balance: $18.75
2025-11-13 05:56:57,986 [INFO]       Price: $103191.40
2025-11-13 05:56:57,986 [INFO]       Capital (fixed): $10.00
2025-11-13 05:56:57,987 [INFO]       Leverage: 10x
2025-11-13 05:56:57,987 [INFO]       Raw quantity: 0.00096907
2025-11-13 05:56:57,987 [INFO]       Formatted quantity: 0.00100000
2025-11-13 05:56:57,987 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 05:56:57,987 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 05:56:57,987 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 05:56:58,339 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:56:59,190 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:56:59,192 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 05:56:59,628 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:56:59,630 [ERROR]    âŒ Order placement failed!
2025-11-13 05:57:00,057 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:57:00,560 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:57:00,660 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 05:57:01,118 [INFO] ðŸŽ¯ ETHUSDT Advanced Signal: SHORT
2025-11-13 05:57:01,118 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:57:01,118 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:57:01,119 [INFO]       1. ðŸ“ˆ RSI Overbought
2025-11-13 05:57:01,119 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:57:01,119 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.580 | RSI: 74.7 | OB: 2.06
2025-11-13 05:57:01,119 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=4
2025-11-13 05:57:01,119 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:57:01,119 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:57:01,119 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:57:01,119 [INFO]    ðŸ“ Top reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 05:57:01,119 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:57:01,217 [INFO] âœ… Set leverage 10x for ETHUSDT
2025-11-13 05:57:01,512 [INFO]    ðŸ’µ Current price: $3535.65
2025-11-13 05:57:01,512 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:57:01,513 [INFO]       Balance: $18.75
2025-11-13 05:57:01,513 [INFO]       Price: $3535.65
2025-11-13 05:57:01,513 [INFO]       Capital (fixed): $10.00
2025-11-13 05:57:01,513 [INFO]       Leverage: 10x
2025-11-13 05:57:01,513 [INFO]       Raw quantity: 0.02828334
2025-11-13 05:57:01,513 [INFO]       Formatted quantity: 0.02800000
2025-11-13 05:57:01,513 [INFO]    ðŸ“¤ Placing SELL order for 0.028 ETHUSDT...
2025-11-13 05:57:01,513 [INFO] ðŸ“ Order: SELL ETHUSDT
2025-11-13 05:57:01,513 [INFO]    Raw qty: 0.02800000 -> Formatted: 0.028
2025-11-13 05:57:01,867 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:57:02,351 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:57:02,353 [ERROR]    Symbol: ETHUSDT, Side: SELL, Qty: 0.028
2025-11-13 05:57:02,790 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:57:02,792 [ERROR]    âŒ Order placement failed!
2025-11-13 05:57:06,424 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:57:06,927 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:57:07,029 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:57:07,379 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:57:07,380 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:57:07,380 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:57:07,380 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:57:07,380 [INFO]    âšª No signal - HOLD
2025-11-13 05:57:07,881 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:57:07,981 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:57:08,327 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:57:08,327 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:57:08,327 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:57:08,327 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:57:08,328 [INFO]    âšª No signal - HOLD
2025-11-13 05:57:08,828 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:57:08,930 [INFO]    Current position: LONG 6.0
2025-11-13 05:57:08,931 [INFO]    Entry: $17.52 | Mark: $17.64
2025-11-13 05:57:08,931 [INFO]    PnL: 0.66% ($0.70)
2025-11-13 05:57:08,932 [INFO]    Age: 0.2h / 36.0h
2025-11-13 05:57:09,432 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:57:09,536 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:57:09,889 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 05:57:09,890 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:57:09,890 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:57:09,890 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:57:09,890 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:57:09,890 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.523 | RSI: 72.4 | OB: 1.21
2025-11-13 05:57:09,890 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:57:09,890 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:57:09,890 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:57:09,891 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:57:09,891 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:57:09,891 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:57:09,991 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 05:57:10,283 [INFO]    ðŸ’µ Current price: $2.50
2025-11-13 05:57:10,283 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:57:10,284 [INFO]       Balance: $18.75
2025-11-13 05:57:10,284 [INFO]       Price: $2.50
2025-11-13 05:57:10,284 [INFO]       Capital (fixed): $10.00
2025-11-13 05:57:10,284 [INFO]       Leverage: 10x
2025-11-13 05:57:10,284 [INFO]       Raw quantity: 40.04645389
2025-11-13 05:57:10,284 [INFO]       Formatted quantity: 40.00000000
2025-11-13 05:57:10,284 [INFO]    ðŸ“¤ Placing BUY order for 40.0 XRPUSDT...
2025-11-13 05:57:10,284 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 05:57:10,284 [INFO]    Raw qty: 40.00000000 -> Formatted: 40.0
2025-11-13 05:57:10,640 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:57:11,075 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:57:11,079 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.0
2025-11-13 05:57:11,508 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:57:11,510 [ERROR]    âŒ Order placement failed!
2025-11-13 05:57:11,951 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:57:11,953 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:58:11,978 [INFO] 
============================================================
2025-11-13 05:58:11,979 [INFO] ðŸ”„ LOOP #62 - 2025-11-13 05:58:11
2025-11-13 05:58:11,979 [INFO] ============================================================
2025-11-13 05:58:12,083 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 05:58:12,084 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:58:12,190 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:58:12,605 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 05:58:12,605 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:58:12,606 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:58:12,606 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 05:58:12,606 [INFO]       2. ðŸ“ˆ Volume Spike
2025-11-13 05:58:12,606 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.575 | RSI: 63.8 | OB: 1.19
2025-11-13 05:58:12,607 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=4
2025-11-13 05:58:12,607 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 05:58:12,607 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:58:12,607 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:58:12,607 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 05:58:12,607 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:58:12,704 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 05:58:12,910 [INFO]    ðŸ’µ Current price: $103168.80
2025-11-13 05:58:12,910 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:58:12,910 [INFO]       Balance: $18.75
2025-11-13 05:58:12,910 [INFO]       Price: $103168.80
2025-11-13 05:58:12,910 [INFO]       Capital (fixed): $10.00
2025-11-13 05:58:12,911 [INFO]       Leverage: 10x
2025-11-13 05:58:12,911 [INFO]       Raw quantity: 0.00096929
2025-11-13 05:58:12,911 [INFO]       Formatted quantity: 0.00100000
2025-11-13 05:58:12,911 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 05:58:12,911 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 05:58:12,911 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 05:58:13,267 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:58:13,984 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:58:13,987 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 05:58:14,386 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:58:14,388 [ERROR]    âŒ Order placement failed!
2025-11-13 05:58:14,774 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:58:15,277 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:58:15,377 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 05:58:15,746 [INFO] ðŸŽ¯ ETHUSDT Advanced Signal: SHORT
2025-11-13 05:58:15,747 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 05:58:15,747 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:58:15,747 [INFO]       1. ðŸ“ˆ RSI Overbought
2025-11-13 05:58:15,747 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:58:15,747 [INFO]       3. ðŸ“ˆ Volume Spike
2025-11-13 05:58:15,747 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.585 | RSI: 74.0 | OB: 3.32
2025-11-13 05:58:15,748 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=6
2025-11-13 05:58:15,748 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence, ðŸ“ˆ Volume Spike
2025-11-13 05:58:15,748 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:58:15,748 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 05:58:15,748 [INFO]    ðŸ“ Top reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence, ðŸ“ˆ Volume Spike
2025-11-13 05:58:15,749 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:58:15,848 [INFO] âœ… Set leverage 10x for ETHUSDT
2025-11-13 05:58:16,056 [INFO]    ðŸ’µ Current price: $3530.40
2025-11-13 05:58:16,057 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:58:16,057 [INFO]       Balance: $18.75
2025-11-13 05:58:16,057 [INFO]       Price: $3530.40
2025-11-13 05:58:16,057 [INFO]       Capital (fixed): $10.00
2025-11-13 05:58:16,057 [INFO]       Leverage: 10x
2025-11-13 05:58:16,057 [INFO]       Raw quantity: 0.02832540
2025-11-13 05:58:16,058 [INFO]       Formatted quantity: 0.02800000
2025-11-13 05:58:16,058 [INFO]    ðŸ“¤ Placing SELL order for 0.028 ETHUSDT...
2025-11-13 05:58:16,058 [INFO] ðŸ“ Order: SELL ETHUSDT
2025-11-13 05:58:16,058 [INFO]    Raw qty: 0.02800000 -> Formatted: 0.028
2025-11-13 05:58:16,411 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:58:16,807 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:58:16,808 [ERROR]    Symbol: ETHUSDT, Side: SELL, Qty: 0.028
2025-11-13 05:58:17,207 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:58:17,209 [ERROR]    âŒ Order placement failed!
2025-11-13 05:58:21,202 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:58:21,704 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:58:21,802 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:58:22,150 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:58:22,150 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:58:22,150 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:58:22,151 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 05:58:22,151 [INFO]    âšª No signal - HOLD
2025-11-13 05:58:22,651 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:58:22,750 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:58:23,107 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:58:23,108 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:58:23,108 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:58:23,108 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:58:23,108 [INFO]    âšª No signal - HOLD
2025-11-13 05:58:23,609 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:58:23,705 [INFO]    Current position: LONG 6.0
2025-11-13 05:58:23,705 [INFO]    Entry: $17.52 | Mark: $17.61
2025-11-13 05:58:23,706 [INFO]    PnL: 0.52% ($0.55)
2025-11-13 05:58:23,706 [INFO]    Age: 0.2h / 36.0h
2025-11-13 05:58:24,206 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:58:24,306 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:58:24,662 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 05:58:24,663 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:58:24,663 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:58:24,663 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:58:24,663 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:58:24,663 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.520 | RSI: 72.4 | OB: 1.42
2025-11-13 05:58:24,663 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:58:24,664 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:58:24,664 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:58:24,664 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:58:24,664 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:58:24,664 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:58:24,763 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 05:58:24,962 [INFO]    ðŸ’µ Current price: $2.50
2025-11-13 05:58:24,962 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:58:24,962 [INFO]       Balance: $18.75
2025-11-13 05:58:24,962 [INFO]       Price: $2.50
2025-11-13 05:58:24,963 [INFO]       Capital (fixed): $10.00
2025-11-13 05:58:24,963 [INFO]       Leverage: 10x
2025-11-13 05:58:24,963 [INFO]       Raw quantity: 40.05447408
2025-11-13 05:58:24,963 [INFO]       Formatted quantity: 40.10000000
2025-11-13 05:58:24,963 [INFO]    ðŸ“¤ Placing BUY order for 40.1 XRPUSDT...
2025-11-13 05:58:24,963 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 05:58:24,963 [INFO]    Raw qty: 40.10000000 -> Formatted: 40.1
2025-11-13 05:58:25,315 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:58:25,706 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:58:25,708 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.1
2025-11-13 05:58:26,109 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:58:26,111 [ERROR]    âŒ Order placement failed!
2025-11-13 05:58:26,491 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:58:26,493 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 05:59:26,554 [INFO] 
============================================================
2025-11-13 05:59:26,554 [INFO] ðŸ”„ LOOP #63 - 2025-11-13 05:59:26
2025-11-13 05:59:26,554 [INFO] ============================================================
2025-11-13 05:59:26,654 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 05:59:26,655 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 05:59:26,754 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 05:59:27,202 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 05:59:27,203 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:59:27,203 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:59:27,203 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 05:59:27,203 [INFO]       2. ðŸ“ˆ Volume Spike
2025-11-13 05:59:27,203 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.582 | RSI: 63.7 | OB: 3.26
2025-11-13 05:59:27,204 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=4
2025-11-13 05:59:27,204 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 05:59:27,204 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:59:27,204 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:59:27,204 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 05:59:27,204 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:59:27,305 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 05:59:27,504 [INFO]    ðŸ’µ Current price: $103165.80
2025-11-13 05:59:27,505 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:59:27,505 [INFO]       Balance: $18.75
2025-11-13 05:59:27,505 [INFO]       Price: $103165.80
2025-11-13 05:59:27,505 [INFO]       Capital (fixed): $10.00
2025-11-13 05:59:27,505 [INFO]       Leverage: 10x
2025-11-13 05:59:27,505 [INFO]       Raw quantity: 0.00096931
2025-11-13 05:59:27,505 [INFO]       Formatted quantity: 0.00100000
2025-11-13 05:59:27,506 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 05:59:27,506 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 05:59:27,506 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 05:59:27,858 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:59:28,600 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:59:28,602 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 05:59:29,001 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:59:29,003 [ERROR]    âŒ Order placement failed!
2025-11-13 05:59:29,395 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:59:29,897 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 05:59:29,994 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 05:59:30,343 [INFO] ðŸŽ¯ ETHUSDT Advanced Signal: SHORT
2025-11-13 05:59:30,343 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 05:59:30,343 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:59:30,344 [INFO]       1. ðŸ“ˆ RSI Overbought
2025-11-13 05:59:30,344 [INFO]       2. ðŸ”€ Bearish RSI Divergence
2025-11-13 05:59:30,344 [INFO]       3. ðŸ“ˆ Volume Spike
2025-11-13 05:59:30,344 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.583 | RSI: 73.7 | OB: 3.06
2025-11-13 05:59:30,344 [INFO]    ðŸ“Š Analysis complete: Signal=SHORT, Score=6
2025-11-13 05:59:30,344 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence, ðŸ“ˆ Volume Spike
2025-11-13 05:59:30,345 [INFO]    ðŸŸ¢ Entry signal detected: SHORT
2025-11-13 05:59:30,345 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 05:59:30,345 [INFO]    ðŸ“ Top reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence, ðŸ“ˆ Volume Spike
2025-11-13 05:59:30,345 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:59:30,443 [INFO] âœ… Set leverage 10x for ETHUSDT
2025-11-13 05:59:30,637 [INFO]    ðŸ’µ Current price: $3528.00
2025-11-13 05:59:30,637 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:59:30,637 [INFO]       Balance: $18.75
2025-11-13 05:59:30,637 [INFO]       Price: $3528.00
2025-11-13 05:59:30,637 [INFO]       Capital (fixed): $10.00
2025-11-13 05:59:30,637 [INFO]       Leverage: 10x
2025-11-13 05:59:30,637 [INFO]       Raw quantity: 0.02834467
2025-11-13 05:59:30,637 [INFO]       Formatted quantity: 0.02800000
2025-11-13 05:59:30,638 [INFO]    ðŸ“¤ Placing SELL order for 0.028 ETHUSDT...
2025-11-13 05:59:30,638 [INFO] ðŸ“ Order: SELL ETHUSDT
2025-11-13 05:59:30,638 [INFO]    Raw qty: 0.02800000 -> Formatted: 0.028
2025-11-13 05:59:31,092 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:59:31,501 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:59:31,504 [ERROR]    Symbol: ETHUSDT, Side: SELL, Qty: 0.028
2025-11-13 05:59:31,908 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:59:31,911 [ERROR]    âŒ Order placement failed!
2025-11-13 05:59:35,568 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:59:36,071 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 05:59:36,170 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 05:59:36,516 [INFO] ðŸŽ¯ SOLUSDT Advanced Signal: LONG
2025-11-13 05:59:36,517 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 05:59:36,517 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:59:36,517 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 05:59:36,517 [INFO]       2. ðŸ“ˆ Volume Spike
2025-11-13 05:59:36,517 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.593 | RSI: 73.0 | OB: 1.06
2025-11-13 05:59:36,518 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=4
2025-11-13 05:59:36,518 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 05:59:36,518 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:59:36,518 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 05:59:36,518 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 05:59:36,518 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:59:36,613 [INFO] âœ… Set leverage 10x for SOLUSDT
2025-11-13 05:59:36,906 [INFO]    ðŸ’µ Current price: $156.20
2025-11-13 05:59:36,907 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:59:36,907 [INFO]       Balance: $18.75
2025-11-13 05:59:36,907 [INFO]       Price: $156.20
2025-11-13 05:59:36,907 [INFO]       Capital (fixed): $10.00
2025-11-13 05:59:36,907 [INFO]       Leverage: 10x
2025-11-13 05:59:36,907 [INFO]       Raw quantity: 0.64020487
2025-11-13 05:59:36,907 [INFO]       Formatted quantity: 0.64000000
2025-11-13 05:59:36,907 [INFO]    ðŸ“¤ Placing BUY order for 0.64 SOLUSDT...
2025-11-13 05:59:36,907 [INFO] ðŸ“ Order: BUY SOLUSDT
2025-11-13 05:59:36,907 [INFO]    Raw qty: 0.64000000 -> Formatted: 0.64
2025-11-13 05:59:37,259 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:59:37,667 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:59:37,669 [ERROR]    Symbol: SOLUSDT, Side: BUY, Qty: 0.64
2025-11-13 05:59:38,032 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:59:38,034 [ERROR]    âŒ Order placement failed!
2025-11-13 05:59:38,478 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:59:38,981 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 05:59:39,087 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 05:59:39,460 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 05:59:39,460 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:59:39,461 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 05:59:39,461 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 05:59:39,461 [INFO]    âšª No signal - HOLD
2025-11-13 05:59:39,962 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 05:59:40,062 [INFO]    Current position: LONG 6.0
2025-11-13 05:59:40,062 [INFO]    Entry: $17.52 | Mark: $17.59
2025-11-13 05:59:40,062 [INFO]    PnL: 0.41% ($0.43)
2025-11-13 05:59:40,062 [INFO]    Age: 0.2h / 36.0h
2025-11-13 05:59:40,563 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 05:59:40,666 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 05:59:41,047 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 05:59:41,047 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 05:59:41,047 [INFO]    ðŸ“ Top Reasons:
2025-11-13 05:59:41,047 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 05:59:41,047 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 05:59:41,047 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.509 | RSI: 71.9 | OB: 0.72
2025-11-13 05:59:41,048 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 05:59:41,048 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:59:41,048 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 05:59:41,048 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 05:59:41,048 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 05:59:41,048 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 05:59:41,243 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 05:59:41,444 [INFO]    ðŸ’µ Current price: $2.49
2025-11-13 05:59:41,445 [INFO]    ðŸ’° Position calculation:
2025-11-13 05:59:41,445 [INFO]       Balance: $18.75
2025-11-13 05:59:41,445 [INFO]       Price: $2.49
2025-11-13 05:59:41,445 [INFO]       Capital (fixed): $10.00
2025-11-13 05:59:41,445 [INFO]       Leverage: 10x
2025-11-13 05:59:41,445 [INFO]       Raw quantity: 40.10105466
2025-11-13 05:59:41,445 [INFO]       Formatted quantity: 40.10000000
2025-11-13 05:59:41,445 [INFO]    ðŸ“¤ Placing BUY order for 40.1 XRPUSDT...
2025-11-13 05:59:41,445 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 05:59:41,445 [INFO]    Raw qty: 40.10000000 -> Formatted: 40.1
2025-11-13 05:59:41,799 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 05:59:42,197 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:59:42,199 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.1
2025-11-13 05:59:42,562 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:59:42,564 [ERROR]    âŒ Order placement failed!
2025-11-13 05:59:43,026 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 05:59:43,028 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:00:43,082 [INFO] 
============================================================
2025-11-13 06:00:43,082 [INFO] ðŸ”„ LOOP #64 - 2025-11-13 06:00:43
2025-11-13 06:00:43,082 [INFO] ============================================================
2025-11-13 06:00:43,183 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:00:43,183 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:00:43,282 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:00:43,691 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:00:43,692 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:00:43,692 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:00:43,693 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:00:43,693 [INFO]    âšª No signal - HOLD
2025-11-13 06:00:44,194 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:00:44,295 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:00:44,658 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:00:44,658 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(3): ðŸ“Œ Bearish Pin Bar
2025-11-13 06:00:44,659 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:00:44,659 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:00:44,659 [INFO]    âšª No signal - HOLD
2025-11-13 06:00:45,160 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:00:45,260 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:00:45,631 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:00:45,632 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:00:45,632 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:00:45,632 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:00:45,632 [INFO]    âšª No signal - HOLD
2025-11-13 06:00:46,133 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:00:46,233 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:00:46,608 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:00:46,608 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:00:46,609 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:00:46,609 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:00:46,609 [INFO]    âšª No signal - HOLD
2025-11-13 06:00:47,110 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:00:47,215 [INFO]    Current position: LONG 6.0
2025-11-13 06:00:47,215 [INFO]    Entry: $17.52 | Mark: $17.61
2025-11-13 06:00:47,215 [INFO]    PnL: 0.52% ($0.55)
2025-11-13 06:00:47,215 [INFO]    Age: 0.3h / 36.0h
2025-11-13 06:00:47,716 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:00:47,817 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:00:48,206 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 06:00:48,207 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:00:48,207 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:00:48,207 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:00:48,207 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 06:00:48,207 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.653 | RSI: 71.5 | OB: 0.82
2025-11-13 06:00:48,208 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:00:48,208 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:00:48,209 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:00:48,209 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:00:48,209 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:00:48,209 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:00:48,308 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 06:00:48,608 [INFO]    ðŸ’µ Current price: $2.50
2025-11-13 06:00:48,609 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:00:48,609 [INFO]       Balance: $18.75
2025-11-13 06:00:48,609 [INFO]       Price: $2.50
2025-11-13 06:00:48,609 [INFO]       Capital (fixed): $10.00
2025-11-13 06:00:48,609 [INFO]       Leverage: 10x
2025-11-13 06:00:48,609 [INFO]       Raw quantity: 40.06249750
2025-11-13 06:00:48,609 [INFO]       Formatted quantity: 40.10000000
2025-11-13 06:00:48,609 [INFO]    ðŸ“¤ Placing BUY order for 40.1 XRPUSDT...
2025-11-13 06:00:48,610 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 06:00:48,610 [INFO]    Raw qty: 40.10000000 -> Formatted: 40.1
2025-11-13 06:00:48,964 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:00:49,727 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:00:49,729 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.1
2025-11-13 06:00:50,115 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:00:50,116 [ERROR]    âŒ Order placement failed!
2025-11-13 06:00:50,528 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:00:50,530 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:01:50,584 [INFO] 
============================================================
2025-11-13 06:01:50,584 [INFO] ðŸ”„ LOOP #65 - 2025-11-13 06:01:50
2025-11-13 06:01:50,584 [INFO] ============================================================
2025-11-13 06:01:51,195 [INFO] ðŸ’“ Bot alive - Loop #65 - Active positions: 1
2025-11-13 06:01:51,310 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:01:51,310 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:01:51,412 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:01:51,784 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:01:51,784 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 06:01:51,784 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:01:51,784 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 06:01:51,785 [INFO]    âšª No signal - HOLD
2025-11-13 06:01:52,285 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:01:52,383 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:01:52,734 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:01:52,734 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:01:52,735 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:01:52,735 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:01:52,735 [INFO]    âšª No signal - HOLD
2025-11-13 06:01:53,236 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:01:53,334 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:01:53,687 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:01:53,687 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:01:53,688 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:01:53,688 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:01:53,688 [INFO]    âšª No signal - HOLD
2025-11-13 06:01:54,189 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:01:54,293 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:01:54,755 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:01:54,755 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:01:54,755 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:01:54,756 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:01:54,756 [INFO]    âšª No signal - HOLD
2025-11-13 06:01:55,257 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:01:55,357 [INFO]    Current position: LONG 6.0
2025-11-13 06:01:55,358 [INFO]    Entry: $17.52 | Mark: $17.62
2025-11-13 06:01:55,358 [INFO]    PnL: 0.55% ($0.58)
2025-11-13 06:01:55,358 [INFO]    Age: 0.3h / 36.0h
2025-11-13 06:01:55,859 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:01:55,957 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:01:56,307 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 06:01:56,308 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:01:56,308 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:01:56,308 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:01:56,308 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 06:01:56,308 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.668 | RSI: 71.8 | OB: 1.23
2025-11-13 06:01:56,309 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:01:56,309 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:01:56,309 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:01:56,309 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:01:56,309 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:01:56,309 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:01:56,408 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 06:01:56,602 [INFO]    ðŸ’µ Current price: $2.50
2025-11-13 06:01:56,602 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:01:56,602 [INFO]       Balance: $18.75
2025-11-13 06:01:56,602 [INFO]       Price: $2.50
2025-11-13 06:01:56,602 [INFO]       Capital (fixed): $10.00
2025-11-13 06:01:56,602 [INFO]       Leverage: 10x
2025-11-13 06:01:56,602 [INFO]       Raw quantity: 39.99040230
2025-11-13 06:01:56,602 [INFO]       Formatted quantity: 40.00000000
2025-11-13 06:01:56,603 [INFO]    ðŸ“¤ Placing BUY order for 40.0 XRPUSDT...
2025-11-13 06:01:56,603 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 06:01:56,603 [INFO]    Raw qty: 40.00000000 -> Formatted: 40.0
2025-11-13 06:01:56,957 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:01:57,760 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:01:57,762 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.0
2025-11-13 06:01:58,202 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:01:58,204 [ERROR]    âŒ Order placement failed!
2025-11-13 06:01:58,640 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:01:58,643 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:02:58,653 [INFO] 
============================================================
2025-11-13 06:02:58,654 [INFO] ðŸ”„ LOOP #66 - 2025-11-13 06:02:58
2025-11-13 06:02:58,654 [INFO] ============================================================
2025-11-13 06:02:58,755 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:02:58,756 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:02:58,855 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:02:59,260 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:02:59,260 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 06:02:59,261 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:02:59,261 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 06:02:59,261 [INFO]    âšª No signal - HOLD
2025-11-13 06:02:59,762 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:02:59,862 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:03:00,329 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:03:00,329 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:03:00,330 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:03:00,330 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:03:00,330 [INFO]    âšª No signal - HOLD
2025-11-13 06:03:00,831 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:03:00,929 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:03:01,414 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:03:01,415 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(3): ðŸ’§ Bearish Liquidity Sweep
2025-11-13 06:03:01,415 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:03:01,415 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(3): ðŸ’§ Bearish Liquidity Sweep
2025-11-13 06:03:01,415 [INFO]    âšª No signal - HOLD
2025-11-13 06:03:01,916 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:03:02,020 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:03:02,371 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:03:02,371 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:03:02,372 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:03:02,372 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:03:02,372 [INFO]    âšª No signal - HOLD
2025-11-13 06:03:02,873 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:03:02,974 [INFO]    Current position: LONG 6.0
2025-11-13 06:03:02,974 [INFO]    Entry: $17.52 | Mark: $17.56
2025-11-13 06:03:02,974 [INFO]    PnL: 0.22% ($0.23)
2025-11-13 06:03:02,974 [INFO]    Age: 0.3h / 36.0h
2025-11-13 06:03:03,475 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:03:03,576 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:03:03,919 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 06:03:03,920 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:03:03,920 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:03:03,920 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:03:03,920 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 06:03:03,920 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.667 | RSI: 70.2 | OB: 1.71
2025-11-13 06:03:03,920 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:03:03,921 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:03:03,921 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:03:03,921 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:03:03,921 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:03:03,921 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:03:04,018 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 06:03:04,317 [INFO]    ðŸ’µ Current price: $2.49
2025-11-13 06:03:04,317 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:03:04,317 [INFO]       Balance: $18.75
2025-11-13 06:03:04,317 [INFO]       Price: $2.49
2025-11-13 06:03:04,317 [INFO]       Capital (fixed): $10.00
2025-11-13 06:03:04,317 [INFO]       Leverage: 10x
2025-11-13 06:03:04,318 [INFO]       Raw quantity: 40.12519059
2025-11-13 06:03:04,318 [INFO]       Formatted quantity: 40.10000000
2025-11-13 06:03:04,318 [INFO]    ðŸ“¤ Placing BUY order for 40.1 XRPUSDT...
2025-11-13 06:03:04,318 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 06:03:04,318 [INFO]    Raw qty: 40.10000000 -> Formatted: 40.1
2025-11-13 06:03:04,769 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:03:05,505 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:03:05,507 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.1
2025-11-13 06:03:05,918 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:03:05,920 [ERROR]    âŒ Order placement failed!
2025-11-13 06:03:06,329 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:03:06,331 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:04:06,337 [INFO] 
============================================================
2025-11-13 06:04:06,338 [INFO] ðŸ”„ LOOP #67 - 2025-11-13 06:04:06
2025-11-13 06:04:06,338 [INFO] ============================================================
2025-11-13 06:04:06,441 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:04:06,441 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:04:06,539 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:04:06,937 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:04:06,937 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:04:06,938 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:04:06,938 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:04:06,938 [INFO]    âšª No signal - HOLD
2025-11-13 06:04:07,439 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:04:07,537 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:04:07,889 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:04:07,889 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:04:07,889 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:04:07,890 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:04:07,890 [INFO]    âšª No signal - HOLD
2025-11-13 06:04:08,390 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:04:08,594 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:04:09,044 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:04:09,044 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:04:09,045 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:04:09,045 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:04:09,045 [INFO]    âšª No signal - HOLD
2025-11-13 06:04:09,546 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:04:09,644 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:04:10,093 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:04:10,094 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:04:10,094 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:04:10,094 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:04:10,094 [INFO]    âšª No signal - HOLD
2025-11-13 06:04:10,595 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:04:10,697 [INFO]    Current position: LONG 6.0
2025-11-13 06:04:10,697 [INFO]    Entry: $17.52 | Mark: $17.54
2025-11-13 06:04:10,697 [INFO]    PnL: 0.11% ($0.12)
2025-11-13 06:04:10,697 [INFO]    Age: 0.3h / 36.0h
2025-11-13 06:04:11,198 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:04:11,297 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:04:11,665 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 06:04:11,666 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:04:11,666 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:04:11,666 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:04:11,666 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 06:04:11,666 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.678 | RSI: 71.0 | OB: 1.22
2025-11-13 06:04:11,667 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:04:11,667 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:04:11,667 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:04:11,667 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:04:11,667 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:04:11,667 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:04:11,763 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 06:04:11,963 [INFO]    ðŸ’µ Current price: $2.49
2025-11-13 06:04:11,964 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:04:11,964 [INFO]       Balance: $18.75
2025-11-13 06:04:11,964 [INFO]       Price: $2.49
2025-11-13 06:04:11,964 [INFO]       Capital (fixed): $10.00
2025-11-13 06:04:11,964 [INFO]       Leverage: 10x
2025-11-13 06:04:11,964 [INFO]       Raw quantity: 40.08176680
2025-11-13 06:04:11,964 [INFO]       Formatted quantity: 40.10000000
2025-11-13 06:04:11,964 [INFO]    ðŸ“¤ Placing BUY order for 40.1 XRPUSDT...
2025-11-13 06:04:11,964 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 06:04:11,964 [INFO]    Raw qty: 40.10000000 -> Formatted: 40.1
2025-11-13 06:04:12,321 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:04:13,159 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:04:13,161 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.1
2025-11-13 06:04:13,596 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:04:13,598 [ERROR]    âŒ Order placement failed!
2025-11-13 06:04:14,056 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:04:14,058 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:05:14,110 [INFO] 
============================================================
2025-11-13 06:05:14,110 [INFO] ðŸ”„ LOOP #68 - 2025-11-13 06:05:14
2025-11-13 06:05:14,110 [INFO] ============================================================
2025-11-13 06:05:14,215 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:05:14,216 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:05:14,318 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:05:14,733 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:05:14,734 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:05:14,734 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:05:14,734 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:05:14,735 [INFO]    âšª No signal - HOLD
2025-11-13 06:05:15,235 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:05:15,337 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:05:15,857 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:05:15,857 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:05:15,858 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:05:15,858 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:05:15,858 [INFO]    âšª No signal - HOLD
2025-11-13 06:05:16,359 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:05:16,459 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:05:16,875 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:05:16,877 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:05:16,877 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:05:16,878 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:05:16,878 [INFO]    âšª No signal - HOLD
2025-11-13 06:05:17,379 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:05:17,483 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:05:18,071 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:05:18,071 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:05:18,072 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:05:18,072 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:05:18,072 [INFO]    âšª No signal - HOLD
2025-11-13 06:05:18,573 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:05:18,670 [INFO]    Current position: LONG 6.0
2025-11-13 06:05:18,670 [INFO]    Entry: $17.52 | Mark: $17.54
2025-11-13 06:05:18,670 [INFO]    PnL: 0.10% ($0.11)
2025-11-13 06:05:18,670 [INFO]    Age: 0.3h / 36.0h
2025-11-13 06:05:19,171 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:05:19,275 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:05:19,685 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 06:05:19,686 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:05:19,686 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:05:19,686 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:05:19,686 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 06:05:19,686 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.674 | RSI: 71.5 | OB: 1.06
2025-11-13 06:05:19,687 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:05:19,687 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:05:19,687 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:05:19,687 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:05:19,687 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:05:19,688 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:05:19,786 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 06:05:20,007 [INFO]    ðŸ’µ Current price: $2.50
2025-11-13 06:05:20,007 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:05:20,007 [INFO]       Balance: $18.75
2025-11-13 06:05:20,007 [INFO]       Price: $2.50
2025-11-13 06:05:20,007 [INFO]       Capital (fixed): $10.00
2025-11-13 06:05:20,008 [INFO]       Leverage: 10x
2025-11-13 06:05:20,008 [INFO]       Raw quantity: 40.01280410
2025-11-13 06:05:20,008 [INFO]       Formatted quantity: 40.00000000
2025-11-13 06:05:20,008 [INFO]    ðŸ“¤ Placing BUY order for 40.0 XRPUSDT...
2025-11-13 06:05:20,008 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 06:05:20,008 [INFO]    Raw qty: 40.00000000 -> Formatted: 40.0
2025-11-13 06:05:20,462 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:05:21,245 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:05:21,247 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.0
2025-11-13 06:05:21,709 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:05:21,710 [ERROR]    âŒ Order placement failed!
2025-11-13 06:05:22,176 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:05:22,178 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:06:22,235 [INFO] 
============================================================
2025-11-13 06:06:22,235 [INFO] ðŸ”„ LOOP #69 - 2025-11-13 06:06:22
2025-11-13 06:06:22,235 [INFO] ============================================================
2025-11-13 06:06:22,339 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:06:22,339 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:06:22,440 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:06:22,845 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:06:22,845 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:06:22,846 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:06:22,846 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:06:22,846 [INFO]    âšª No signal - HOLD
2025-11-13 06:06:23,347 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:06:23,447 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:06:23,923 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:06:23,923 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:06:23,924 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:06:23,924 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:06:23,924 [INFO]    âšª No signal - HOLD
2025-11-13 06:06:24,425 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:06:24,523 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:06:24,870 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:06:24,871 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:06:24,871 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:06:24,871 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:06:24,871 [INFO]    âšª No signal - HOLD
2025-11-13 06:06:25,372 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:06:25,473 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:06:25,826 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:06:25,827 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:06:25,827 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:06:25,827 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:06:25,827 [INFO]    âšª No signal - HOLD
2025-11-13 06:06:26,328 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:06:26,429 [INFO]    Current position: LONG 6.0
2025-11-13 06:06:26,429 [INFO]    Entry: $17.52 | Mark: $17.54
2025-11-13 06:06:26,429 [INFO]    PnL: 0.12% ($0.13)
2025-11-13 06:06:26,429 [INFO]    Age: 0.4h / 36.0h
2025-11-13 06:06:26,930 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:06:27,030 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:06:27,390 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 06:06:27,390 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:06:27,391 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:06:27,391 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:06:27,391 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 06:06:27,391 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.646 | RSI: 71.9 | OB: 1.75
2025-11-13 06:06:27,391 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:06:27,392 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:06:27,392 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:06:27,392 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:06:27,392 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:06:27,392 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:06:27,491 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 06:06:27,686 [INFO]    ðŸ’µ Current price: $2.50
2025-11-13 06:06:27,686 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:06:27,686 [INFO]       Balance: $18.75
2025-11-13 06:06:27,686 [INFO]       Price: $2.50
2025-11-13 06:06:27,686 [INFO]       Capital (fixed): $10.00
2025-11-13 06:06:27,686 [INFO]       Leverage: 10x
2025-11-13 06:06:27,686 [INFO]       Raw quantity: 39.96962309
2025-11-13 06:06:27,686 [INFO]       Formatted quantity: 40.00000000
2025-11-13 06:06:27,686 [INFO]    ðŸ“¤ Placing BUY order for 40.0 XRPUSDT...
2025-11-13 06:06:27,687 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 06:06:27,687 [INFO]    Raw qty: 40.00000000 -> Formatted: 40.0
2025-11-13 06:06:28,037 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:06:28,916 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:06:28,918 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.0
2025-11-13 06:06:29,398 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:06:29,400 [ERROR]    âŒ Order placement failed!
2025-11-13 06:06:29,859 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:06:29,861 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:07:29,916 [INFO] 
============================================================
2025-11-13 06:07:29,917 [INFO] ðŸ”„ LOOP #70 - 2025-11-13 06:07:29
2025-11-13 06:07:29,917 [INFO] ============================================================
2025-11-13 06:07:30,514 [INFO] ðŸ’“ Bot alive - Loop #70 - Active positions: 1
2025-11-13 06:07:30,618 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:07:30,619 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:07:30,720 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:07:31,071 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:07:31,071 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:07:31,071 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:07:31,071 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:07:31,071 [INFO]    âšª No signal - HOLD
2025-11-13 06:07:31,572 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:07:31,675 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:07:32,033 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:07:32,033 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:07:32,034 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:07:32,034 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:07:32,034 [INFO]    âšª No signal - HOLD
2025-11-13 06:07:32,537 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:07:32,637 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:07:33,008 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:07:33,008 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:07:33,009 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:07:33,009 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:07:33,009 [INFO]    âšª No signal - HOLD
2025-11-13 06:07:33,510 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:07:33,610 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:07:33,974 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:07:33,974 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:07:33,975 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:07:33,975 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:07:33,975 [INFO]    âšª No signal - HOLD
2025-11-13 06:07:34,476 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:07:34,577 [INFO]    Current position: LONG 6.0
2025-11-13 06:07:34,577 [INFO]    Entry: $17.52 | Mark: $17.56
2025-11-13 06:07:34,577 [INFO]    PnL: 0.19% ($0.20)
2025-11-13 06:07:34,577 [INFO]    Age: 0.4h / 36.0h
2025-11-13 06:07:35,078 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:07:35,178 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:07:35,542 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 06:07:35,543 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:07:35,543 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:07:35,543 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:07:35,543 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 06:07:35,543 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.662 | RSI: 72.1 | OB: 1.40
2025-11-13 06:07:35,544 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:07:35,544 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:07:35,544 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:07:35,544 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:07:35,544 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:07:35,544 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:07:35,645 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 06:07:35,840 [INFO]    ðŸ’µ Current price: $2.50
2025-11-13 06:07:35,840 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:07:35,841 [INFO]       Balance: $18.75
2025-11-13 06:07:35,841 [INFO]       Price: $2.50
2025-11-13 06:07:35,841 [INFO]       Capital (fixed): $10.00
2025-11-13 06:07:35,841 [INFO]       Leverage: 10x
2025-11-13 06:07:35,841 [INFO]       Raw quantity: 39.96483095
2025-11-13 06:07:35,841 [INFO]       Formatted quantity: 40.00000000
2025-11-13 06:07:35,841 [INFO]    ðŸ“¤ Placing BUY order for 40.0 XRPUSDT...
2025-11-13 06:07:35,841 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 06:07:35,841 [INFO]    Raw qty: 40.00000000 -> Formatted: 40.0
2025-11-13 06:07:36,197 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:07:36,912 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:07:36,914 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.0
2025-11-13 06:07:37,370 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:07:37,372 [ERROR]    âŒ Order placement failed!
2025-11-13 06:07:37,795 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:07:38,603 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:08:38,657 [INFO] 
============================================================
2025-11-13 06:08:38,658 [INFO] ðŸ”„ LOOP #71 - 2025-11-13 06:08:38
2025-11-13 06:08:38,658 [INFO] ============================================================
2025-11-13 06:08:38,763 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:08:38,764 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:08:38,863 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:08:39,227 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:08:39,228 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:08:39,228 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:08:39,229 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:08:39,229 [INFO]    âšª No signal - HOLD
2025-11-13 06:08:39,730 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:08:39,830 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:08:40,181 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:08:40,181 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:08:40,182 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:08:40,182 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:08:40,182 [INFO]    âšª No signal - HOLD
2025-11-13 06:08:40,683 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:08:40,782 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:08:41,143 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:08:41,144 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:08:41,144 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:08:41,144 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:08:41,144 [INFO]    âšª No signal - HOLD
2025-11-13 06:08:41,645 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:08:41,749 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:08:42,211 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:08:42,212 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:08:42,212 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:08:42,213 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:08:42,213 [INFO]    âšª No signal - HOLD
2025-11-13 06:08:42,714 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:08:42,813 [INFO]    Current position: LONG 6.0
2025-11-13 06:08:42,814 [INFO]    Entry: $17.52 | Mark: $17.59
2025-11-13 06:08:42,814 [INFO]    PnL: 0.40% ($0.42)
2025-11-13 06:08:42,814 [INFO]    Age: 0.4h / 36.0h
2025-11-13 06:08:43,315 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:08:43,415 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:08:43,772 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 06:08:43,772 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:08:43,772 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:08:43,773 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:08:43,773 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 06:08:43,773 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.675 | RSI: 72.6 | OB: 0.76
2025-11-13 06:08:43,773 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:08:43,774 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:08:43,774 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:08:43,774 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:08:43,774 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:08:43,774 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:08:43,974 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 06:08:44,173 [INFO]    ðŸ’µ Current price: $2.51
2025-11-13 06:08:44,173 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:08:44,173 [INFO]       Balance: $18.75
2025-11-13 06:08:44,173 [INFO]       Price: $2.51
2025-11-13 06:08:44,173 [INFO]       Capital (fixed): $10.00
2025-11-13 06:08:44,173 [INFO]       Leverage: 10x
2025-11-13 06:08:44,173 [INFO]       Raw quantity: 39.89626970
2025-11-13 06:08:44,173 [INFO]       Formatted quantity: 39.90000000
2025-11-13 06:08:44,173 [INFO]    ðŸ“¤ Placing BUY order for 39.9 XRPUSDT...
2025-11-13 06:08:44,174 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 06:08:44,174 [INFO]    Raw qty: 39.90000000 -> Formatted: 39.9
2025-11-13 06:08:44,525 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:08:45,320 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:08:45,322 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 39.9
2025-11-13 06:08:45,762 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:08:45,764 [ERROR]    âŒ Order placement failed!
2025-11-13 06:08:46,164 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:08:46,166 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:09:46,227 [INFO] 
============================================================
2025-11-13 06:09:46,228 [INFO] ðŸ”„ LOOP #72 - 2025-11-13 06:09:46
2025-11-13 06:09:46,228 [INFO] ============================================================
2025-11-13 06:09:46,332 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:09:46,332 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:09:46,435 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:09:46,831 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:09:46,831 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:09:46,831 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:09:46,831 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:09:46,831 [INFO]    âšª No signal - HOLD
2025-11-13 06:09:47,332 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:09:47,431 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:09:47,827 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:09:47,827 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:09:47,828 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:09:47,828 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:09:47,828 [INFO]    âšª No signal - HOLD
2025-11-13 06:09:48,329 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:09:48,427 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:09:48,880 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:09:48,880 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:09:48,881 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:09:48,881 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:09:48,881 [INFO]    âšª No signal - HOLD
2025-11-13 06:09:49,382 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:09:49,481 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:09:49,840 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:09:49,840 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:09:49,841 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:09:49,841 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:09:49,841 [INFO]    âšª No signal - HOLD
2025-11-13 06:09:50,341 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:09:50,546 [INFO]    Current position: LONG 6.0
2025-11-13 06:09:50,546 [INFO]    Entry: $17.52 | Mark: $17.59
2025-11-13 06:09:50,546 [INFO]    PnL: 0.39% ($0.41)
2025-11-13 06:09:50,546 [INFO]    Age: 0.4h / 36.0h
2025-11-13 06:09:51,047 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:09:51,249 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:09:51,639 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 06:09:51,639 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:09:51,640 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:09:51,640 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:09:51,640 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 06:09:51,640 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.669 | RSI: 72.9 | OB: 1.13
2025-11-13 06:09:51,641 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:09:51,641 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:09:51,641 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:09:51,641 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:09:51,641 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:09:51,642 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:09:51,745 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 06:09:51,943 [INFO]    ðŸ’µ Current price: $2.51
2025-11-13 06:09:51,944 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:09:51,944 [INFO]       Balance: $18.75
2025-11-13 06:09:51,944 [INFO]       Price: $2.51
2025-11-13 06:09:51,944 [INFO]       Capital (fixed): $10.00
2025-11-13 06:09:51,944 [INFO]       Leverage: 10x
2025-11-13 06:09:51,944 [INFO]       Raw quantity: 39.88990387
2025-11-13 06:09:51,944 [INFO]       Formatted quantity: 39.90000000
2025-11-13 06:09:51,944 [INFO]    ðŸ“¤ Placing BUY order for 39.9 XRPUSDT...
2025-11-13 06:09:51,944 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 06:09:51,944 [INFO]    Raw qty: 39.90000000 -> Formatted: 39.9
2025-11-13 06:09:52,295 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:09:53,078 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:09:53,080 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 39.9
2025-11-13 06:09:53,521 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:09:53,522 [ERROR]    âŒ Order placement failed!
2025-11-13 06:09:53,970 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:09:53,972 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:10:53,982 [INFO] 
============================================================
2025-11-13 06:10:53,982 [INFO] ðŸ”„ LOOP #73 - 2025-11-13 06:10:53
2025-11-13 06:10:53,982 [INFO] ============================================================
2025-11-13 06:10:54,085 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:10:54,086 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:10:54,187 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:10:54,577 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:10:54,578 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:10:54,578 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:10:54,578 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:10:54,578 [INFO]    âšª No signal - HOLD
2025-11-13 06:10:55,079 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:10:55,181 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:10:55,577 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:10:55,577 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:10:55,582 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:10:55,583 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:10:55,583 [INFO]    âšª No signal - HOLD
2025-11-13 06:10:56,083 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:10:56,183 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:10:56,577 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:10:56,578 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:10:56,578 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:10:56,578 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:10:56,578 [INFO]    âšª No signal - HOLD
2025-11-13 06:10:57,079 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:10:57,183 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:10:57,535 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:10:57,535 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:10:57,536 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:10:57,536 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:10:57,536 [INFO]    âšª No signal - HOLD
2025-11-13 06:10:58,037 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:10:58,136 [INFO]    Current position: LONG 6.0
2025-11-13 06:10:58,136 [INFO]    Entry: $17.52 | Mark: $17.59
2025-11-13 06:10:58,136 [INFO]    PnL: 0.41% ($0.43)
2025-11-13 06:10:58,136 [INFO]    Age: 0.4h / 36.0h
2025-11-13 06:10:58,637 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:10:58,741 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:10:59,193 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 06:10:59,193 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:10:59,193 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:10:59,193 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:10:59,193 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 06:10:59,193 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.680 | RSI: 72.8 | OB: 1.22
2025-11-13 06:10:59,194 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:10:59,194 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:10:59,194 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:10:59,194 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:10:59,194 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:10:59,194 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:10:59,290 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 06:10:59,489 [INFO]    ðŸ’µ Current price: $2.51
2025-11-13 06:10:59,489 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:10:59,490 [INFO]       Balance: $18.75
2025-11-13 06:10:59,490 [INFO]       Price: $2.51
2025-11-13 06:10:59,490 [INFO]       Capital (fixed): $10.00
2025-11-13 06:10:59,490 [INFO]       Leverage: 10x
2025-11-13 06:10:59,490 [INFO]       Raw quantity: 39.87081855
2025-11-13 06:10:59,490 [INFO]       Formatted quantity: 39.90000000
2025-11-13 06:10:59,490 [INFO]    ðŸ“¤ Placing BUY order for 39.9 XRPUSDT...
2025-11-13 06:10:59,490 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 06:10:59,490 [INFO]    Raw qty: 39.90000000 -> Formatted: 39.9
2025-11-13 06:10:59,842 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:11:00,562 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:11:00,565 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 39.9
2025-11-13 06:11:01,389 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:11:01,391 [ERROR]    âŒ Order placement failed!
2025-11-13 06:11:01,799 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:11:01,801 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:12:01,861 [INFO] 
============================================================
2025-11-13 06:12:01,861 [INFO] ðŸ”„ LOOP #74 - 2025-11-13 06:12:01
2025-11-13 06:12:01,862 [INFO] ============================================================
2025-11-13 06:12:01,969 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:12:01,970 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:12:02,072 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:12:02,485 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:12:02,485 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 06:12:02,486 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:12:02,486 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:12:02,486 [INFO]       2. ðŸ“ˆ Volume Spike
2025-11-13 06:12:02,486 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.550 | RSI: 62.3 | OB: 90.09
2025-11-13 06:12:02,486 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=4
2025-11-13 06:12:02,486 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 06:12:02,487 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:12:02,487 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 06:12:02,487 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 06:12:02,487 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:12:02,586 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:12:02,787 [INFO]    ðŸ’µ Current price: $103139.60
2025-11-13 06:12:02,788 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:12:02,788 [INFO]       Balance: $18.75
2025-11-13 06:12:02,788 [INFO]       Price: $103139.60
2025-11-13 06:12:02,788 [INFO]       Capital (fixed): $10.00
2025-11-13 06:12:02,788 [INFO]       Leverage: 10x
2025-11-13 06:12:02,788 [INFO]       Raw quantity: 0.00096956
2025-11-13 06:12:02,788 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:12:02,788 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:12:02,788 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:12:02,788 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:12:03,139 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:12:03,869 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:12:03,870 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:12:04,281 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:12:04,282 [ERROR]    âŒ Order placement failed!
2025-11-13 06:12:04,692 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:12:05,195 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:12:05,298 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:12:05,647 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:12:05,648 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:12:05,648 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:12:05,648 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:12:05,648 [INFO]    âšª No signal - HOLD
2025-11-13 06:12:06,149 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:12:06,251 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:12:06,724 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:12:06,725 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:12:06,725 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:12:06,726 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:12:06,726 [INFO]    âšª No signal - HOLD
2025-11-13 06:12:07,227 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:12:07,334 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:12:07,898 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:12:07,898 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:12:07,899 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:12:07,899 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:12:07,899 [INFO]    âšª No signal - HOLD
2025-11-13 06:12:08,400 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:12:08,499 [INFO]    Current position: LONG 6.0
2025-11-13 06:12:08,500 [INFO]    Entry: $17.52 | Mark: $17.63
2025-11-13 06:12:08,500 [INFO]    PnL: 0.62% ($0.65)
2025-11-13 06:12:08,500 [INFO]    Age: 0.4h / 36.0h
2025-11-13 06:12:09,000 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:12:09,106 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:12:09,559 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 06:12:09,559 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:12:09,559 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:12:09,559 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:12:09,560 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 06:12:09,560 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.683 | RSI: 72.9 | OB: 0.97
2025-11-13 06:12:09,560 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:12:09,560 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:12:09,560 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:12:09,560 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:12:09,561 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:12:09,561 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:12:09,657 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 06:12:09,863 [INFO]    ðŸ’µ Current price: $2.51
2025-11-13 06:12:09,864 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:12:09,864 [INFO]       Balance: $18.75
2025-11-13 06:12:09,864 [INFO]       Price: $2.51
2025-11-13 06:12:09,864 [INFO]       Capital (fixed): $10.00
2025-11-13 06:12:09,864 [INFO]       Leverage: 10x
2025-11-13 06:12:09,864 [INFO]       Raw quantity: 39.87717829
2025-11-13 06:12:09,864 [INFO]       Formatted quantity: 39.90000000
2025-11-13 06:12:09,864 [INFO]    ðŸ“¤ Placing BUY order for 39.9 XRPUSDT...
2025-11-13 06:12:09,864 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 06:12:09,864 [INFO]    Raw qty: 39.90000000 -> Formatted: 39.9
2025-11-13 06:12:10,219 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:12:11,051 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:12:11,052 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 39.9
2025-11-13 06:12:11,450 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:12:11,452 [ERROR]    âŒ Order placement failed!
2025-11-13 06:12:11,874 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:12:11,876 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:13:11,895 [INFO] 
============================================================
2025-11-13 06:13:11,895 [INFO] ðŸ”„ LOOP #75 - 2025-11-13 06:13:11
2025-11-13 06:13:11,895 [INFO] ============================================================
2025-11-13 06:13:12,511 [INFO] ðŸ’“ Bot alive - Loop #75 - Active positions: 1
2025-11-13 06:13:12,615 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:13:12,615 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:13:12,714 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:13:13,074 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:13:13,074 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 06:13:13,075 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:13:13,075 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:13:13,075 [INFO]       2. ðŸ“ˆ Volume Spike
2025-11-13 06:13:13,075 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.590 | RSI: 62.7 | OB: 0.97
2025-11-13 06:13:13,075 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=4
2025-11-13 06:13:13,075 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 06:13:13,076 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:13:13,076 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 06:13:13,076 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 06:13:13,076 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:13:13,176 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:13:13,482 [INFO]    ðŸ’µ Current price: $103111.20
2025-11-13 06:13:13,482 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:13:13,482 [INFO]       Balance: $18.75
2025-11-13 06:13:13,482 [INFO]       Price: $103111.20
2025-11-13 06:13:13,482 [INFO]       Capital (fixed): $10.00
2025-11-13 06:13:13,482 [INFO]       Leverage: 10x
2025-11-13 06:13:13,482 [INFO]       Raw quantity: 0.00096983
2025-11-13 06:13:13,482 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:13:13,482 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:13:13,483 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:13:13,483 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:13:13,836 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:13:14,612 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:13:14,614 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:13:15,037 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:13:15,039 [ERROR]    âŒ Order placement failed!
2025-11-13 06:13:15,466 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:13:15,968 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:13:16,071 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:13:16,436 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:13:16,436 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:13:16,437 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:13:16,437 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:13:16,437 [INFO]    âšª No signal - HOLD
2025-11-13 06:13:16,938 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:13:17,040 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:13:17,386 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:13:17,386 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:13:17,386 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:13:17,386 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:13:17,386 [INFO]    âšª No signal - HOLD
2025-11-13 06:13:17,887 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:13:17,988 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:13:18,335 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:13:18,335 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:13:18,335 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:13:18,336 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:13:18,336 [INFO]    âšª No signal - HOLD
2025-11-13 06:13:18,836 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:13:19,041 [INFO]    Current position: LONG 6.0
2025-11-13 06:13:19,041 [INFO]    Entry: $17.52 | Mark: $17.61
2025-11-13 06:13:19,041 [INFO]    PnL: 0.50% ($0.53)
2025-11-13 06:13:19,041 [INFO]    Age: 0.5h / 36.0h
2025-11-13 06:13:19,542 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:13:19,647 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:13:20,126 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 06:13:20,126 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:13:20,127 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:13:20,127 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:13:20,127 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 06:13:20,127 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.677 | RSI: 72.5 | OB: 1.95
2025-11-13 06:13:20,127 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:13:20,127 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:13:20,128 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:13:20,128 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:13:20,128 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:13:20,128 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:13:20,227 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 06:13:20,429 [INFO]    ðŸ’µ Current price: $2.51
2025-11-13 06:13:20,429 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:13:20,429 [INFO]       Balance: $18.75
2025-11-13 06:13:20,430 [INFO]       Price: $2.51
2025-11-13 06:13:20,430 [INFO]       Capital (fixed): $10.00
2025-11-13 06:13:20,430 [INFO]       Leverage: 10x
2025-11-13 06:13:20,430 [INFO]       Raw quantity: 39.91060026
2025-11-13 06:13:20,430 [INFO]       Formatted quantity: 39.90000000
2025-11-13 06:13:20,430 [INFO]    ðŸ“¤ Placing BUY order for 39.9 XRPUSDT...
2025-11-13 06:13:20,430 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 06:13:20,430 [INFO]    Raw qty: 39.90000000 -> Formatted: 39.9
2025-11-13 06:13:20,782 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:13:21,636 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:13:21,638 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 39.9
2025-11-13 06:13:22,044 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:13:22,045 [ERROR]    âŒ Order placement failed!
2025-11-13 06:13:22,447 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:13:22,448 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:14:22,500 [INFO] 
============================================================
2025-11-13 06:14:22,500 [INFO] ðŸ”„ LOOP #76 - 2025-11-13 06:14:22
2025-11-13 06:14:22,500 [INFO] ============================================================
2025-11-13 06:14:22,604 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:14:22,604 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:14:22,707 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:14:23,111 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:14:23,111 [INFO]    ðŸ“Š Confluence Score: 4/4
2025-11-13 06:14:23,111 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:14:23,112 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:14:23,112 [INFO]       2. ðŸ“ˆ Volume Spike
2025-11-13 06:14:23,112 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.590 | RSI: 62.8 | OB: 0.72
2025-11-13 06:14:23,113 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=4
2025-11-13 06:14:23,113 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 06:14:23,113 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:14:23,113 [INFO]    ðŸ“Š Confluence score: 4/4
2025-11-13 06:14:23,113 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ“ˆ Volume Spike
2025-11-13 06:14:23,113 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:14:23,212 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:14:23,417 [INFO]    ðŸ’µ Current price: $103160.40
2025-11-13 06:14:23,418 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:14:23,418 [INFO]       Balance: $18.75
2025-11-13 06:14:23,418 [INFO]       Price: $103160.40
2025-11-13 06:14:23,418 [INFO]       Capital (fixed): $10.00
2025-11-13 06:14:23,418 [INFO]       Leverage: 10x
2025-11-13 06:14:23,418 [INFO]       Raw quantity: 0.00096936
2025-11-13 06:14:23,418 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:14:23,418 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:14:23,418 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:14:23,418 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:14:23,771 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:14:24,482 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:14:24,484 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:14:24,886 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:14:24,887 [ERROR]    âŒ Order placement failed!
2025-11-13 06:14:25,288 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:14:25,790 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:14:25,891 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:14:26,241 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:14:26,241 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:14:26,242 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:14:26,242 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:14:26,242 [INFO]    âšª No signal - HOLD
2025-11-13 06:14:26,743 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:14:26,843 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:14:27,192 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:14:27,193 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:14:27,193 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:14:27,193 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:14:27,193 [INFO]    âšª No signal - HOLD
2025-11-13 06:14:27,694 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:14:27,900 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:14:28,247 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:14:28,247 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:14:28,248 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:14:28,248 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG
2025-11-13 06:14:28,248 [INFO]    âšª No signal - HOLD
2025-11-13 06:14:28,749 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:14:28,945 [INFO]    Current position: LONG 6.0
2025-11-13 06:14:28,945 [INFO]    Entry: $17.52 | Mark: $17.59
2025-11-13 06:14:28,945 [INFO]    PnL: 0.41% ($0.43)
2025-11-13 06:14:28,945 [INFO]    Age: 0.5h / 36.0h
2025-11-13 06:14:29,446 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:14:29,545 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:14:29,890 [INFO] ðŸŽ¯ XRPUSDT Advanced Signal: LONG
2025-11-13 06:14:29,890 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:14:29,890 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:14:29,890 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:14:29,890 [INFO]       2. ðŸ“Š Bullish FVG
2025-11-13 06:14:29,890 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.660 | RSI: 71.9 | OB: 2.50
2025-11-13 06:14:29,891 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:14:29,891 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:14:29,891 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:14:29,891 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:14:29,891 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ“Š Bullish FVG
2025-11-13 06:14:29,891 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:14:29,990 [INFO] âœ… Set leverage 10x for XRPUSDT
2025-11-13 06:14:30,189 [INFO]    ðŸ’µ Current price: $2.50
2025-11-13 06:14:30,190 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:14:30,190 [INFO]       Balance: $18.75
2025-11-13 06:14:30,190 [INFO]       Price: $2.50
2025-11-13 06:14:30,190 [INFO]       Capital (fixed): $10.00
2025-11-13 06:14:30,190 [INFO]       Leverage: 10x
2025-11-13 06:14:30,190 [INFO]       Raw quantity: 40.00800160
2025-11-13 06:14:30,190 [INFO]       Formatted quantity: 40.00000000
2025-11-13 06:14:30,190 [INFO]    ðŸ“¤ Placing BUY order for 40.0 XRPUSDT...
2025-11-13 06:14:30,190 [INFO] ðŸ“ Order: BUY XRPUSDT
2025-11-13 06:14:30,190 [INFO]    Raw qty: 40.00000000 -> Formatted: 40.0
2025-11-13 06:14:30,540 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:14:31,259 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:14:31,261 [ERROR]    Symbol: XRPUSDT, Side: BUY, Qty: 40.0
2025-11-13 06:14:31,636 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:14:31,638 [ERROR]    âŒ Order placement failed!
2025-11-13 06:14:32,017 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:14:32,019 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:15:32,080 [INFO] 
============================================================
2025-11-13 06:15:32,080 [INFO] ðŸ”„ LOOP #77 - 2025-11-13 06:15:32
2025-11-13 06:15:32,080 [INFO] ============================================================
2025-11-13 06:15:32,181 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:15:32,181 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:15:32,281 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:15:32,706 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:15:32,706 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 06:15:32,707 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:15:32,707 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:15:32,707 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:15:32,707 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.549 | RSI: 63.8 | OB: 1.29
2025-11-13 06:15:32,707 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 06:15:32,707 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:15:32,708 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:15:32,708 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 06:15:32,708 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:15:32,708 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:15:32,806 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:15:33,001 [INFO]    ðŸ’µ Current price: $103201.90
2025-11-13 06:15:33,001 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:15:33,001 [INFO]       Balance: $18.75
2025-11-13 06:15:33,001 [INFO]       Price: $103201.90
2025-11-13 06:15:33,001 [INFO]       Capital (fixed): $10.00
2025-11-13 06:15:33,001 [INFO]       Leverage: 10x
2025-11-13 06:15:33,001 [INFO]       Raw quantity: 0.00096897
2025-11-13 06:15:33,002 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:15:33,002 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:15:33,002 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:15:33,002 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:15:33,354 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:15:34,150 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:15:34,152 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:15:34,581 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:15:34,584 [ERROR]    âŒ Order placement failed!
2025-11-13 06:15:35,009 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:15:35,511 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:15:35,618 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:15:35,986 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:15:35,987 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:15:35,987 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:15:35,988 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:15:35,988 [INFO]    âšª No signal - HOLD
2025-11-13 06:15:36,489 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:15:36,589 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:15:36,954 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:15:36,954 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:15:36,955 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:15:36,955 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:15:36,955 [INFO]    âšª No signal - HOLD
2025-11-13 06:15:37,456 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:15:37,556 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:15:37,922 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 06:15:37,922 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:15:37,922 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:15:37,922 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:15:37,922 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:15:37,922 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.530 | RSI: 67.0 | OB: 1.01
2025-11-13 06:15:37,923 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:15:37,923 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:15:37,923 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:15:37,923 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:15:37,923 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:15:37,923 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:15:38,023 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 06:15:38,224 [INFO]    ðŸ’µ Current price: $101.44
2025-11-13 06:15:38,224 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:15:38,224 [INFO]       Balance: $18.75
2025-11-13 06:15:38,224 [INFO]       Price: $101.44
2025-11-13 06:15:38,224 [INFO]       Capital (fixed): $10.00
2025-11-13 06:15:38,225 [INFO]       Leverage: 10x
2025-11-13 06:15:38,225 [INFO]       Raw quantity: 0.98580442
2025-11-13 06:15:38,225 [INFO]       Formatted quantity: 0.98600000
2025-11-13 06:15:38,225 [INFO]    ðŸ“¤ Placing BUY order for 0.986 LTCUSDT...
2025-11-13 06:15:38,225 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 06:15:38,225 [INFO]    Raw qty: 0.98600000 -> Formatted: 0.986
2025-11-13 06:15:38,575 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:15:39,033 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:15:39,034 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.986
2025-11-13 06:15:39,464 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:15:39,466 [ERROR]    âŒ Order placement failed!
2025-11-13 06:15:39,908 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:15:40,411 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:15:40,618 [INFO]    Current position: LONG 6.0
2025-11-13 06:15:40,619 [INFO]    Entry: $17.52 | Mark: $17.61
2025-11-13 06:15:40,619 [INFO]    PnL: 0.51% ($0.54)
2025-11-13 06:15:40,619 [INFO]    Age: 0.5h / 36.0h
2025-11-13 06:15:41,120 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:15:41,221 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:15:41,582 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:15:41,582 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:15:41,583 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:15:41,583 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:15:41,583 [INFO]    âšª No signal - HOLD
2025-11-13 06:15:41,583 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:16:41,622 [INFO] 
============================================================
2025-11-13 06:16:41,623 [INFO] ðŸ”„ LOOP #78 - 2025-11-13 06:16:41
2025-11-13 06:16:41,623 [INFO] ============================================================
2025-11-13 06:16:41,727 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:16:41,727 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:16:41,828 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:16:42,222 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:16:42,222 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 06:16:42,222 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:16:42,222 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:16:42,222 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:16:42,222 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.587 | RSI: 64.4 | OB: 4.12
2025-11-13 06:16:42,223 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 06:16:42,224 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:16:42,224 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:16:42,224 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 06:16:42,224 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:16:42,224 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:16:42,325 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:16:42,526 [INFO]    ðŸ’µ Current price: $103261.50
2025-11-13 06:16:42,527 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:16:42,527 [INFO]       Balance: $18.75
2025-11-13 06:16:42,527 [INFO]       Price: $103261.50
2025-11-13 06:16:42,527 [INFO]       Capital (fixed): $10.00
2025-11-13 06:16:42,527 [INFO]       Leverage: 10x
2025-11-13 06:16:42,527 [INFO]       Raw quantity: 0.00096842
2025-11-13 06:16:42,527 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:16:42,527 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:16:42,527 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:16:42,527 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:16:42,880 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:16:43,682 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:16:43,684 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:16:44,269 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:16:44,271 [ERROR]    âŒ Order placement failed!
2025-11-13 06:16:44,707 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:16:45,211 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:16:45,312 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:16:45,668 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:16:45,668 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:16:45,669 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:16:45,669 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:16:45,669 [INFO]    âšª No signal - HOLD
2025-11-13 06:16:46,170 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:16:46,376 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:16:46,729 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:16:46,730 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:16:46,730 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:16:46,730 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:16:46,730 [INFO]    âšª No signal - HOLD
2025-11-13 06:16:47,231 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:16:47,329 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:16:47,810 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 06:16:47,810 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:16:47,810 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:16:47,810 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:16:47,810 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:16:47,810 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.532 | RSI: 67.0 | OB: 0.89
2025-11-13 06:16:47,811 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:16:47,811 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:16:47,811 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:16:47,811 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:16:47,811 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:16:47,811 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:16:47,907 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 06:16:48,106 [INFO]    ðŸ’µ Current price: $101.44
2025-11-13 06:16:48,106 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:16:48,106 [INFO]       Balance: $18.75
2025-11-13 06:16:48,106 [INFO]       Price: $101.44
2025-11-13 06:16:48,106 [INFO]       Capital (fixed): $10.00
2025-11-13 06:16:48,106 [INFO]       Leverage: 10x
2025-11-13 06:16:48,106 [INFO]       Raw quantity: 0.98580442
2025-11-13 06:16:48,107 [INFO]       Formatted quantity: 0.98600000
2025-11-13 06:16:48,107 [INFO]    ðŸ“¤ Placing BUY order for 0.986 LTCUSDT...
2025-11-13 06:16:48,107 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 06:16:48,107 [INFO]    Raw qty: 0.98600000 -> Formatted: 0.986
2025-11-13 06:16:48,564 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:16:49,006 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:16:49,008 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.986
2025-11-13 06:16:49,450 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:16:49,452 [ERROR]    âŒ Order placement failed!
2025-11-13 06:16:49,890 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:16:50,393 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:16:50,493 [INFO]    Current position: LONG 6.0
2025-11-13 06:16:50,493 [INFO]    Entry: $17.52 | Mark: $17.63
2025-11-13 06:16:50,493 [INFO]    PnL: 0.64% ($0.67)
2025-11-13 06:16:50,494 [INFO]    Age: 0.5h / 36.0h
2025-11-13 06:16:50,994 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:16:51,092 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:16:51,459 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:16:51,459 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:16:51,460 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:16:51,460 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:16:51,460 [INFO]    âšª No signal - HOLD
2025-11-13 06:16:51,460 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:17:51,516 [INFO] 
============================================================
2025-11-13 06:17:51,516 [INFO] ðŸ”„ LOOP #79 - 2025-11-13 06:17:51
2025-11-13 06:17:51,516 [INFO] ============================================================
2025-11-13 06:17:51,619 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:17:51,619 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:17:51,719 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:17:52,107 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:17:52,108 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 06:17:52,108 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:17:52,108 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:17:52,108 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:17:52,108 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.593 | RSI: 64.1 | OB: 5.59
2025-11-13 06:17:52,108 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 06:17:52,108 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:17:52,108 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:17:52,108 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 06:17:52,109 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:17:52,109 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:17:52,214 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:17:52,414 [INFO]    ðŸ’µ Current price: $103212.10
2025-11-13 06:17:52,415 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:17:52,415 [INFO]       Balance: $18.75
2025-11-13 06:17:52,415 [INFO]       Price: $103212.10
2025-11-13 06:17:52,415 [INFO]       Capital (fixed): $10.00
2025-11-13 06:17:52,415 [INFO]       Leverage: 10x
2025-11-13 06:17:52,415 [INFO]       Raw quantity: 0.00096888
2025-11-13 06:17:52,415 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:17:52,415 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:17:52,415 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:17:52,415 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:17:52,767 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:17:53,526 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:17:53,528 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:17:53,962 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:17:53,965 [ERROR]    âŒ Order placement failed!
2025-11-13 06:17:54,392 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:17:54,895 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:17:54,996 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:17:55,382 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:17:55,382 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:17:55,383 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:17:55,383 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:17:55,384 [INFO]    âšª No signal - HOLD
2025-11-13 06:17:55,884 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:17:55,990 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:17:56,354 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:17:56,354 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:17:56,355 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:17:56,355 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:17:56,355 [INFO]    âšª No signal - HOLD
2025-11-13 06:17:56,856 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:17:56,955 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:17:57,340 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 06:17:57,340 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:17:57,340 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:17:57,340 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:17:57,340 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:17:57,340 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.533 | RSI: 67.0 | OB: 0.83
2025-11-13 06:17:57,341 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:17:57,342 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:17:57,342 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:17:57,342 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:17:57,342 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:17:57,342 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:17:57,441 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 06:17:57,744 [INFO]    ðŸ’µ Current price: $101.44
2025-11-13 06:17:57,744 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:17:57,744 [INFO]       Balance: $18.75
2025-11-13 06:17:57,744 [INFO]       Price: $101.44
2025-11-13 06:17:57,744 [INFO]       Capital (fixed): $10.00
2025-11-13 06:17:57,744 [INFO]       Leverage: 10x
2025-11-13 06:17:57,744 [INFO]       Raw quantity: 0.98580442
2025-11-13 06:17:57,744 [INFO]       Formatted quantity: 0.98600000
2025-11-13 06:17:57,744 [INFO]    ðŸ“¤ Placing BUY order for 0.986 LTCUSDT...
2025-11-13 06:17:57,744 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 06:17:57,745 [INFO]    Raw qty: 0.98600000 -> Formatted: 0.986
2025-11-13 06:17:58,098 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:17:58,601 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:17:58,603 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.986
2025-11-13 06:17:59,031 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:17:59,033 [ERROR]    âŒ Order placement failed!
2025-11-13 06:17:59,458 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:17:59,960 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:18:00,071 [INFO]    Current position: LONG 6.0
2025-11-13 06:18:00,072 [INFO]    Entry: $17.52 | Mark: $17.64
2025-11-13 06:18:00,072 [INFO]    PnL: 0.66% ($0.70)
2025-11-13 06:18:00,072 [INFO]    Age: 0.5h / 36.0h
2025-11-13 06:18:00,573 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:18:00,676 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:18:01,048 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:18:01,048 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:18:01,049 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:18:01,049 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:18:01,049 [INFO]    âšª No signal - HOLD
2025-11-13 06:18:01,049 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:19:01,050 [INFO] 
============================================================
2025-11-13 06:19:01,050 [INFO] ðŸ”„ LOOP #80 - 2025-11-13 06:19:01
2025-11-13 06:19:01,050 [INFO] ============================================================
2025-11-13 06:19:01,650 [INFO] ðŸ’“ Bot alive - Loop #80 - Active positions: 1
2025-11-13 06:19:01,752 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:19:01,752 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:19:01,853 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:19:02,355 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:19:02,356 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 06:19:02,356 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:19:02,356 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:19:02,356 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:19:02,356 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.593 | RSI: 63.8 | OB: 6.68
2025-11-13 06:19:02,357 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 06:19:02,357 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:19:02,358 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:19:02,358 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 06:19:02,358 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:19:02,358 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:19:02,456 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:19:02,659 [INFO]    ðŸ’µ Current price: $103239.30
2025-11-13 06:19:02,659 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:19:02,660 [INFO]       Balance: $18.75
2025-11-13 06:19:02,660 [INFO]       Price: $103239.30
2025-11-13 06:19:02,660 [INFO]       Capital (fixed): $10.00
2025-11-13 06:19:02,660 [INFO]       Leverage: 10x
2025-11-13 06:19:02,660 [INFO]       Raw quantity: 0.00096862
2025-11-13 06:19:02,660 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:19:02,660 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:19:02,660 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:19:02,660 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:19:03,015 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:19:03,778 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:19:03,780 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:19:04,209 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:19:04,210 [ERROR]    âŒ Order placement failed!
2025-11-13 06:19:04,630 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:19:05,133 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:19:05,234 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:19:05,696 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:19:05,696 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:19:05,697 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:19:05,697 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:19:05,697 [INFO]    âšª No signal - HOLD
2025-11-13 06:19:06,198 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:19:06,299 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:19:06,660 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:19:06,660 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:19:06,662 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:19:06,662 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:19:06,662 [INFO]    âšª No signal - HOLD
2025-11-13 06:19:07,163 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:19:07,263 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:19:07,638 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 06:19:07,639 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:19:07,639 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:19:07,639 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:19:07,639 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:19:07,639 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.529 | RSI: 67.0 | OB: 1.18
2025-11-13 06:19:07,640 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:19:07,640 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:19:07,640 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:19:07,640 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:19:07,640 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:19:07,640 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:19:07,738 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 06:19:08,042 [INFO]    ðŸ’µ Current price: $101.44
2025-11-13 06:19:08,042 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:19:08,042 [INFO]       Balance: $18.75
2025-11-13 06:19:08,042 [INFO]       Price: $101.44
2025-11-13 06:19:08,043 [INFO]       Capital (fixed): $10.00
2025-11-13 06:19:08,043 [INFO]       Leverage: 10x
2025-11-13 06:19:08,043 [INFO]       Raw quantity: 0.98580442
2025-11-13 06:19:08,043 [INFO]       Formatted quantity: 0.98600000
2025-11-13 06:19:08,043 [INFO]    ðŸ“¤ Placing BUY order for 0.986 LTCUSDT...
2025-11-13 06:19:08,043 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 06:19:08,043 [INFO]    Raw qty: 0.98600000 -> Formatted: 0.986
2025-11-13 06:19:08,396 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:19:08,888 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:19:08,890 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.986
2025-11-13 06:19:09,380 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:19:09,381 [ERROR]    âŒ Order placement failed!
2025-11-13 06:19:09,808 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:19:10,319 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:19:10,422 [INFO]    Current position: LONG 6.0
2025-11-13 06:19:10,423 [INFO]    Entry: $17.52 | Mark: $17.65
2025-11-13 06:19:10,423 [INFO]    PnL: 0.72% ($0.76)
2025-11-13 06:19:10,423 [INFO]    Age: 0.6h / 36.0h
2025-11-13 06:19:10,924 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:19:11,026 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:19:11,489 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:19:11,489 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:19:11,490 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:19:11,490 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:19:11,490 [INFO]    âšª No signal - HOLD
2025-11-13 06:19:12,201 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:20:12,235 [INFO] 
============================================================
2025-11-13 06:20:12,235 [INFO] ðŸ”„ LOOP #81 - 2025-11-13 06:20:12
2025-11-13 06:20:12,235 [INFO] ============================================================
2025-11-13 06:20:12,340 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:20:12,340 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:20:12,443 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:20:12,802 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:20:12,802 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 06:20:12,802 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:20:12,802 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:20:12,802 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:20:12,802 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.596 | RSI: 64.3 | OB: 0.75
2025-11-13 06:20:12,803 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 06:20:12,803 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:20:12,803 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:20:12,803 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 06:20:12,803 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:20:12,803 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:20:12,903 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:20:13,101 [INFO]    ðŸ’µ Current price: $103233.40
2025-11-13 06:20:13,101 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:20:13,101 [INFO]       Balance: $18.75
2025-11-13 06:20:13,101 [INFO]       Price: $103233.40
2025-11-13 06:20:13,101 [INFO]       Capital (fixed): $10.00
2025-11-13 06:20:13,101 [INFO]       Leverage: 10x
2025-11-13 06:20:13,102 [INFO]       Raw quantity: 0.00096868
2025-11-13 06:20:13,102 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:20:13,102 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:20:13,102 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:20:13,102 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:20:13,455 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:20:14,323 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:20:14,325 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:20:14,763 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:20:14,765 [ERROR]    âŒ Order placement failed!
2025-11-13 06:20:15,231 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:20:15,733 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:20:15,834 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:20:16,209 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:20:16,210 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:20:16,210 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:20:16,210 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:20:16,211 [INFO]    âšª No signal - HOLD
2025-11-13 06:20:16,711 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:20:16,814 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:20:17,173 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:20:17,173 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:20:17,174 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:20:17,174 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:20:17,174 [INFO]    âšª No signal - HOLD
2025-11-13 06:20:17,675 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:20:17,775 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:20:18,127 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 06:20:18,127 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:20:18,128 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:20:18,128 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:20:18,128 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:20:18,128 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.530 | RSI: 67.0 | OB: 1.11
2025-11-13 06:20:18,128 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:20:18,128 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:20:18,128 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:20:18,129 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:20:18,129 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:20:18,129 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:20:18,229 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 06:20:18,522 [INFO]    ðŸ’µ Current price: $101.44
2025-11-13 06:20:18,522 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:20:18,522 [INFO]       Balance: $18.75
2025-11-13 06:20:18,522 [INFO]       Price: $101.44
2025-11-13 06:20:18,523 [INFO]       Capital (fixed): $10.00
2025-11-13 06:20:18,523 [INFO]       Leverage: 10x
2025-11-13 06:20:18,523 [INFO]       Raw quantity: 0.98580442
2025-11-13 06:20:18,523 [INFO]       Formatted quantity: 0.98600000
2025-11-13 06:20:18,523 [INFO]    ðŸ“¤ Placing BUY order for 0.986 LTCUSDT...
2025-11-13 06:20:18,523 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 06:20:18,523 [INFO]    Raw qty: 0.98600000 -> Formatted: 0.986
2025-11-13 06:20:18,970 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:20:19,439 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:20:19,441 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.986
2025-11-13 06:20:19,931 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:20:19,933 [ERROR]    âŒ Order placement failed!
2025-11-13 06:20:20,425 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:20:20,928 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:20:21,031 [INFO]    Current position: LONG 6.0
2025-11-13 06:20:21,032 [INFO]    Entry: $17.52 | Mark: $17.67
2025-11-13 06:20:21,032 [INFO]    PnL: 0.87% ($0.92)
2025-11-13 06:20:21,032 [INFO]    Age: 0.6h / 36.0h
2025-11-13 06:20:21,533 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:20:21,634 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:20:21,990 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:20:21,991 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:20:21,991 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:20:21,991 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:20:21,991 [INFO]    âšª No signal - HOLD
2025-11-13 06:20:21,992 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:21:22,052 [INFO] 
============================================================
2025-11-13 06:21:22,052 [INFO] ðŸ”„ LOOP #82 - 2025-11-13 06:21:22
2025-11-13 06:21:22,052 [INFO] ============================================================
2025-11-13 06:21:22,154 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:21:22,155 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:21:22,266 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:21:22,666 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:21:22,666 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 06:21:22,666 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:21:22,666 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:21:22,666 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:21:22,666 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.594 | RSI: 64.7 | OB: 3.01
2025-11-13 06:21:22,667 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 06:21:22,667 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:21:22,667 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:21:22,667 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 06:21:22,667 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:21:22,667 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:21:22,770 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:21:22,970 [INFO]    ðŸ’µ Current price: $103402.30
2025-11-13 06:21:22,970 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:21:22,970 [INFO]       Balance: $18.75
2025-11-13 06:21:22,970 [INFO]       Price: $103402.30
2025-11-13 06:21:22,971 [INFO]       Capital (fixed): $10.00
2025-11-13 06:21:22,971 [INFO]       Leverage: 10x
2025-11-13 06:21:22,971 [INFO]       Raw quantity: 0.00096710
2025-11-13 06:21:22,971 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:21:22,971 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:21:22,971 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:21:22,971 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:21:23,324 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:21:24,120 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:21:24,122 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:21:24,563 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:21:24,566 [ERROR]    âŒ Order placement failed!
2025-11-13 06:21:25,074 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:21:25,577 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:21:25,679 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:21:26,065 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:21:26,066 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:21:26,066 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:21:26,066 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:21:26,066 [INFO]    âšª No signal - HOLD
2025-11-13 06:21:26,569 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:21:26,670 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:21:27,047 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:21:27,048 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:21:27,048 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:21:27,049 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:21:27,049 [INFO]    âšª No signal - HOLD
2025-11-13 06:21:27,549 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:21:27,651 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:21:28,197 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 06:21:28,197 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:21:28,197 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:21:28,197 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:21:28,197 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:21:28,198 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.529 | RSI: 67.3 | OB: 1.16
2025-11-13 06:21:28,198 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:21:28,198 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:21:28,198 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:21:28,198 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:21:28,199 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:21:28,199 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:21:28,297 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 06:21:28,495 [INFO]    ðŸ’µ Current price: $101.49
2025-11-13 06:21:28,495 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:21:28,496 [INFO]       Balance: $18.75
2025-11-13 06:21:28,496 [INFO]       Price: $101.49
2025-11-13 06:21:28,496 [INFO]       Capital (fixed): $10.00
2025-11-13 06:21:28,496 [INFO]       Leverage: 10x
2025-11-13 06:21:28,496 [INFO]       Raw quantity: 0.98531875
2025-11-13 06:21:28,496 [INFO]       Formatted quantity: 0.98500000
2025-11-13 06:21:28,496 [INFO]    ðŸ“¤ Placing BUY order for 0.985 LTCUSDT...
2025-11-13 06:21:28,496 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 06:21:28,496 [INFO]    Raw qty: 0.98500000 -> Formatted: 0.985
2025-11-13 06:21:28,847 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:21:29,313 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:21:29,316 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.985
2025-11-13 06:21:29,749 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:21:29,751 [ERROR]    âŒ Order placement failed!
2025-11-13 06:21:30,195 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:21:30,698 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:21:30,903 [INFO]    Current position: LONG 6.0
2025-11-13 06:21:30,904 [INFO]    Entry: $17.52 | Mark: $17.68
2025-11-13 06:21:30,904 [INFO]    PnL: 0.88% ($0.93)
2025-11-13 06:21:30,904 [INFO]    Age: 0.6h / 36.0h
2025-11-13 06:21:31,405 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:21:31,503 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:21:31,852 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:21:31,852 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:21:31,852 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:21:31,852 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:21:31,852 [INFO]    âšª No signal - HOLD
2025-11-13 06:21:31,852 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:22:31,882 [INFO] 
============================================================
2025-11-13 06:22:31,882 [INFO] ðŸ”„ LOOP #83 - 2025-11-13 06:22:31
2025-11-13 06:22:31,882 [INFO] ============================================================
2025-11-13 06:22:31,982 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:22:31,983 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:22:32,083 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:22:32,494 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:22:32,495 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 06:22:32,495 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:22:32,495 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:22:32,495 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:22:32,495 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.593 | RSI: 65.3 | OB: 3.79
2025-11-13 06:22:32,496 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 06:22:32,496 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:22:32,496 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:22:32,496 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 06:22:32,496 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:22:32,496 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:22:32,595 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:22:32,796 [INFO]    ðŸ’µ Current price: $103353.20
2025-11-13 06:22:32,796 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:22:32,797 [INFO]       Balance: $18.75
2025-11-13 06:22:32,797 [INFO]       Price: $103353.20
2025-11-13 06:22:32,797 [INFO]       Capital (fixed): $10.00
2025-11-13 06:22:32,797 [INFO]       Leverage: 10x
2025-11-13 06:22:32,797 [INFO]       Raw quantity: 0.00096756
2025-11-13 06:22:32,797 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:22:32,797 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:22:32,797 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:22:32,797 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:22:33,150 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:22:34,049 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:22:34,050 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:22:34,560 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:22:34,561 [ERROR]    âŒ Order placement failed!
2025-11-13 06:22:35,019 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:22:35,523 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:22:35,623 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:22:35,974 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:22:35,974 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:22:35,974 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:22:35,975 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:22:35,975 [INFO]    âšª No signal - HOLD
2025-11-13 06:22:36,476 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:22:36,578 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:22:36,963 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:22:36,963 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:22:36,964 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:22:36,964 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:22:36,964 [INFO]    âšª No signal - HOLD
2025-11-13 06:22:37,465 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:22:37,566 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:22:37,916 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 06:22:37,916 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:22:37,917 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:22:37,917 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:22:37,917 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:22:37,917 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.537 | RSI: 67.3 | OB: 0.73
2025-11-13 06:22:37,917 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:22:37,917 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:22:37,917 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:22:37,917 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:22:37,918 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:22:37,918 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:22:38,113 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 06:22:38,413 [INFO]    ðŸ’µ Current price: $101.49
2025-11-13 06:22:38,413 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:22:38,413 [INFO]       Balance: $18.75
2025-11-13 06:22:38,413 [INFO]       Price: $101.49
2025-11-13 06:22:38,413 [INFO]       Capital (fixed): $10.00
2025-11-13 06:22:38,413 [INFO]       Leverage: 10x
2025-11-13 06:22:38,413 [INFO]       Raw quantity: 0.98531875
2025-11-13 06:22:38,414 [INFO]       Formatted quantity: 0.98500000
2025-11-13 06:22:38,414 [INFO]    ðŸ“¤ Placing BUY order for 0.985 LTCUSDT...
2025-11-13 06:22:38,414 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 06:22:38,414 [INFO]    Raw qty: 0.98500000 -> Formatted: 0.985
2025-11-13 06:22:38,764 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:22:39,226 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:22:39,227 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.985
2025-11-13 06:22:39,711 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:22:39,713 [ERROR]    âŒ Order placement failed!
2025-11-13 06:22:40,224 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:22:40,726 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:22:40,824 [INFO]    Current position: LONG 6.0
2025-11-13 06:22:40,824 [INFO]    Entry: $17.52 | Mark: $17.65
2025-11-13 06:22:40,824 [INFO]    PnL: 0.75% ($0.79)
2025-11-13 06:22:40,824 [INFO]    Age: 0.6h / 36.0h
2025-11-13 06:22:41,325 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:22:41,428 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:22:41,782 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:22:41,782 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:22:41,782 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:22:41,782 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:22:41,782 [INFO]    âšª No signal - HOLD
2025-11-13 06:22:41,782 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:23:41,827 [INFO] 
============================================================
2025-11-13 06:23:41,828 [INFO] ðŸ”„ LOOP #84 - 2025-11-13 06:23:41
2025-11-13 06:23:41,828 [INFO] ============================================================
2025-11-13 06:23:41,928 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:23:41,928 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:23:42,025 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:23:42,419 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:23:42,420 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 06:23:42,420 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:23:42,420 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:23:42,420 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:23:42,420 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.590 | RSI: 66.2 | OB: 50.37
2025-11-13 06:23:42,421 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 06:23:42,421 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:23:42,421 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:23:42,421 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 06:23:42,421 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:23:42,421 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:23:42,524 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:23:42,723 [INFO]    ðŸ’µ Current price: $103496.10
2025-11-13 06:23:42,723 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:23:42,723 [INFO]       Balance: $18.75
2025-11-13 06:23:42,723 [INFO]       Price: $103496.10
2025-11-13 06:23:42,723 [INFO]       Capital (fixed): $10.00
2025-11-13 06:23:42,724 [INFO]       Leverage: 10x
2025-11-13 06:23:42,724 [INFO]       Raw quantity: 0.00096622
2025-11-13 06:23:42,724 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:23:42,724 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:23:42,724 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:23:42,724 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:23:43,079 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:23:44,932 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:23:44,933 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:23:45,325 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:23:45,327 [ERROR]    âŒ Order placement failed!
2025-11-13 06:23:45,810 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:23:46,313 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:23:46,410 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:23:46,761 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:23:46,762 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:23:46,762 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:23:46,762 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:23:46,762 [INFO]    âšª No signal - HOLD
2025-11-13 06:23:47,263 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:23:47,366 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:23:47,738 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:23:47,738 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:23:47,739 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:23:47,739 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:23:47,740 [INFO]    âšª No signal - HOLD
2025-11-13 06:23:48,240 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:23:48,341 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:23:48,714 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 06:23:48,714 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:23:48,714 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:23:48,714 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:23:48,714 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:23:48,715 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.539 | RSI: 67.3 | OB: 0.68
2025-11-13 06:23:48,715 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:23:48,716 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:23:48,716 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:23:48,716 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:23:48,716 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:23:48,716 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:23:48,818 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 06:23:49,122 [INFO]    ðŸ’µ Current price: $101.49
2025-11-13 06:23:49,123 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:23:49,123 [INFO]       Balance: $18.75
2025-11-13 06:23:49,123 [INFO]       Price: $101.49
2025-11-13 06:23:49,123 [INFO]       Capital (fixed): $10.00
2025-11-13 06:23:49,123 [INFO]       Leverage: 10x
2025-11-13 06:23:49,123 [INFO]       Raw quantity: 0.98531875
2025-11-13 06:23:49,123 [INFO]       Formatted quantity: 0.98500000
2025-11-13 06:23:49,123 [INFO]    ðŸ“¤ Placing BUY order for 0.985 LTCUSDT...
2025-11-13 06:23:49,123 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 06:23:49,123 [INFO]    Raw qty: 0.98500000 -> Formatted: 0.985
2025-11-13 06:23:49,474 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:23:49,929 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:23:49,932 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.985
2025-11-13 06:23:50,370 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:23:50,372 [ERROR]    âŒ Order placement failed!
2025-11-13 06:23:50,833 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:23:51,335 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:23:51,438 [INFO]    Current position: LONG 6.0
2025-11-13 06:23:51,438 [INFO]    Entry: $17.52 | Mark: $17.67
2025-11-13 06:23:51,438 [INFO]    PnL: 0.82% ($0.87)
2025-11-13 06:23:51,438 [INFO]    Age: 0.6h / 36.0h
2025-11-13 06:23:51,939 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:23:52,040 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:23:52,410 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:23:52,411 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:23:52,411 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:23:52,412 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:23:52,412 [INFO]    âšª No signal - HOLD
2025-11-13 06:23:52,412 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:24:52,459 [INFO] 
============================================================
2025-11-13 06:24:52,459 [INFO] ðŸ”„ LOOP #85 - 2025-11-13 06:24:52
2025-11-13 06:24:52,459 [INFO] ============================================================
2025-11-13 06:24:53,067 [INFO] ðŸ’“ Bot alive - Loop #85 - Active positions: 1
2025-11-13 06:24:53,171 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:24:53,171 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:24:53,276 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:24:53,646 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:24:53,647 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 06:24:53,647 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:24:53,647 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:24:53,647 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:24:53,647 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.598 | RSI: 66.9 | OB: 0.48
2025-11-13 06:24:53,647 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 06:24:53,648 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:24:53,648 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:24:53,648 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 06:24:53,648 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:24:53,648 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:24:53,747 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:24:53,944 [INFO]    ðŸ’µ Current price: $103555.70
2025-11-13 06:24:53,945 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:24:53,945 [INFO]       Balance: $18.75
2025-11-13 06:24:53,945 [INFO]       Price: $103555.70
2025-11-13 06:24:53,945 [INFO]       Capital (fixed): $10.00
2025-11-13 06:24:53,945 [INFO]       Leverage: 10x
2025-11-13 06:24:53,945 [INFO]       Raw quantity: 0.00096566
2025-11-13 06:24:53,945 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:24:53,945 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:24:53,945 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:24:53,945 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:24:54,299 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:24:55,035 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:24:55,037 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:24:55,467 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:24:55,469 [ERROR]    âŒ Order placement failed!
2025-11-13 06:24:55,901 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:24:56,403 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:24:56,502 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:24:56,852 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:24:56,853 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:24:56,853 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:24:56,853 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:24:56,854 [INFO]    âšª No signal - HOLD
2025-11-13 06:24:57,354 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:24:57,463 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:24:57,816 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:24:57,816 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:24:57,817 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:24:57,817 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:24:57,817 [INFO]    âšª No signal - HOLD
2025-11-13 06:24:58,318 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:24:58,417 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:24:58,792 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 06:24:58,792 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:24:58,792 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:24:58,792 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:24:58,792 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:24:58,792 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.551 | RSI: 67.3 | OB: 0.38
2025-11-13 06:24:58,793 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:24:58,793 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:24:58,794 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:24:58,794 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:24:58,794 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:24:58,794 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:24:58,895 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 06:24:59,198 [INFO]    ðŸ’µ Current price: $101.73
2025-11-13 06:24:59,198 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:24:59,198 [INFO]       Balance: $18.75
2025-11-13 06:24:59,198 [INFO]       Price: $101.73
2025-11-13 06:24:59,198 [INFO]       Capital (fixed): $10.00
2025-11-13 06:24:59,198 [INFO]       Leverage: 10x
2025-11-13 06:24:59,198 [INFO]       Raw quantity: 0.98299420
2025-11-13 06:24:59,198 [INFO]       Formatted quantity: 0.98300000
2025-11-13 06:24:59,199 [INFO]    ðŸ“¤ Placing BUY order for 0.983 LTCUSDT...
2025-11-13 06:24:59,199 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 06:24:59,199 [INFO]    Raw qty: 0.98300000 -> Formatted: 0.983
2025-11-13 06:24:59,553 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:24:59,965 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:24:59,967 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.983
2025-11-13 06:25:00,385 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:25:00,386 [ERROR]    âŒ Order placement failed!
2025-11-13 06:25:00,815 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:25:01,317 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:25:01,418 [INFO]    Current position: LONG 6.0
2025-11-13 06:25:01,418 [INFO]    Entry: $17.52 | Mark: $17.68
2025-11-13 06:25:01,418 [INFO]    PnL: 0.90% ($0.95)
2025-11-13 06:25:01,418 [INFO]    Age: 0.7h / 36.0h
2025-11-13 06:25:01,919 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:25:02,018 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:25:02,371 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:25:02,371 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:25:02,371 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:25:02,371 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:25:02,372 [INFO]    âšª No signal - HOLD
2025-11-13 06:25:02,372 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:26:02,422 [INFO] 
============================================================
2025-11-13 06:26:02,422 [INFO] ðŸ”„ LOOP #86 - 2025-11-13 06:26:02
2025-11-13 06:26:02,422 [INFO] ============================================================
2025-11-13 06:26:02,519 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:26:02,520 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:26:02,621 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:26:03,019 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:26:03,019 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 06:26:03,019 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:26:03,019 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:26:03,019 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:26:03,019 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.598 | RSI: 66.3 | OB: 1.80
2025-11-13 06:26:03,020 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 06:26:03,020 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:26:03,020 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:26:03,020 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 06:26:03,020 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:26:03,020 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:26:03,122 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:26:03,317 [INFO]    ðŸ’µ Current price: $103495.80
2025-11-13 06:26:03,318 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:26:03,318 [INFO]       Balance: $18.75
2025-11-13 06:26:03,318 [INFO]       Price: $103495.80
2025-11-13 06:26:03,318 [INFO]       Capital (fixed): $10.00
2025-11-13 06:26:03,318 [INFO]       Leverage: 10x
2025-11-13 06:26:03,318 [INFO]       Raw quantity: 0.00096622
2025-11-13 06:26:03,318 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:26:03,318 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:26:03,318 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:26:03,318 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:26:03,672 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:26:04,551 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:26:04,553 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:26:04,988 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:26:04,995 [ERROR]    âŒ Order placement failed!
2025-11-13 06:26:05,430 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:26:05,933 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:26:06,033 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:26:06,520 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:26:06,520 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:26:06,521 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:26:06,521 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:26:06,521 [INFO]    âšª No signal - HOLD
2025-11-13 06:26:07,022 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:26:07,125 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:26:07,508 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:26:07,509 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(3): ðŸ“Œ Bearish Pin Bar
2025-11-13 06:26:07,510 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:26:07,510 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:26:07,510 [INFO]    âšª No signal - HOLD
2025-11-13 06:26:08,011 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:26:08,109 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:26:08,471 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 06:26:08,472 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:26:08,472 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:26:08,472 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:26:08,472 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:26:08,472 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.529 | RSI: 66.7 | OB: 1.31
2025-11-13 06:26:08,472 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:26:08,472 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:26:08,473 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:26:08,473 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:26:08,473 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:26:08,473 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:26:08,572 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 06:26:08,773 [INFO]    ðŸ’µ Current price: $101.41
2025-11-13 06:26:08,773 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:26:08,773 [INFO]       Balance: $18.75
2025-11-13 06:26:08,773 [INFO]       Price: $101.41
2025-11-13 06:26:08,773 [INFO]       Capital (fixed): $10.00
2025-11-13 06:26:08,773 [INFO]       Leverage: 10x
2025-11-13 06:26:08,773 [INFO]       Raw quantity: 0.98609605
2025-11-13 06:26:08,773 [INFO]       Formatted quantity: 0.98600000
2025-11-13 06:26:08,773 [INFO]    ðŸ“¤ Placing BUY order for 0.986 LTCUSDT...
2025-11-13 06:26:08,774 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 06:26:08,774 [INFO]    Raw qty: 0.98600000 -> Formatted: 0.986
2025-11-13 06:26:09,127 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:26:09,591 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:26:09,594 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.986
2025-11-13 06:26:10,063 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:26:10,064 [ERROR]    âŒ Order placement failed!
2025-11-13 06:26:10,523 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:26:11,026 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:26:11,227 [INFO]    Current position: LONG 6.0
2025-11-13 06:26:11,227 [INFO]    Entry: $17.52 | Mark: $17.65
2025-11-13 06:26:11,228 [INFO]    PnL: 0.75% ($0.79)
2025-11-13 06:26:11,228 [INFO]    Age: 0.7h / 36.0h
2025-11-13 06:26:11,728 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:26:11,832 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:26:12,189 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:26:12,189 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:26:12,190 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:26:12,190 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:26:12,190 [INFO]    âšª No signal - HOLD
2025-11-13 06:26:12,190 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:27:12,235 [INFO] 
============================================================
2025-11-13 06:27:12,235 [INFO] ðŸ”„ LOOP #87 - 2025-11-13 06:27:12
2025-11-13 06:27:12,236 [INFO] ============================================================
2025-11-13 06:27:12,336 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:27:12,336 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:27:12,441 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:27:12,841 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:27:12,841 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 06:27:12,841 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:27:12,841 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:27:12,841 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:27:12,841 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.597 | RSI: 65.6 | OB: 0.07
2025-11-13 06:27:12,842 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 06:27:12,842 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:27:12,842 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:27:12,842 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 06:27:12,842 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:27:12,842 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:27:12,942 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:27:13,142 [INFO]    ðŸ’µ Current price: $103428.90
2025-11-13 06:27:13,143 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:27:13,143 [INFO]       Balance: $18.75
2025-11-13 06:27:13,143 [INFO]       Price: $103428.90
2025-11-13 06:27:13,143 [INFO]       Capital (fixed): $10.00
2025-11-13 06:27:13,143 [INFO]       Leverage: 10x
2025-11-13 06:27:13,143 [INFO]       Raw quantity: 0.00096685
2025-11-13 06:27:13,143 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:27:13,143 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:27:13,143 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:27:13,143 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:27:13,496 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:27:14,223 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:27:14,225 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:27:14,612 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:27:14,613 [ERROR]    âŒ Order placement failed!
2025-11-13 06:27:14,993 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:27:15,495 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:27:15,599 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:27:15,995 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:27:15,996 [INFO]    Partial signals: SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:27:15,996 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:27:15,996 [INFO]    ðŸ“ Signal reasons: SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:27:15,997 [INFO]    âšª No signal - HOLD
2025-11-13 06:27:16,497 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:27:16,598 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:27:16,969 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:27:16,970 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:27:16,970 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:27:16,971 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:27:16,971 [INFO]    âšª No signal - HOLD
2025-11-13 06:27:17,471 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:27:17,572 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:27:17,937 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 06:27:17,937 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:27:17,938 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:27:17,938 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:27:17,938 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:27:17,938 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.529 | RSI: 66.7 | OB: 2.64
2025-11-13 06:27:17,939 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:27:17,939 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:27:17,939 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:27:17,939 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:27:17,939 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:27:17,939 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:27:18,041 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 06:27:18,245 [INFO]    ðŸ’µ Current price: $101.41
2025-11-13 06:27:18,245 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:27:18,245 [INFO]       Balance: $18.75
2025-11-13 06:27:18,246 [INFO]       Price: $101.41
2025-11-13 06:27:18,246 [INFO]       Capital (fixed): $10.00
2025-11-13 06:27:18,246 [INFO]       Leverage: 10x
2025-11-13 06:27:18,246 [INFO]       Raw quantity: 0.98609605
2025-11-13 06:27:18,246 [INFO]       Formatted quantity: 0.98600000
2025-11-13 06:27:18,246 [INFO]    ðŸ“¤ Placing BUY order for 0.986 LTCUSDT...
2025-11-13 06:27:18,246 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 06:27:18,246 [INFO]    Raw qty: 0.98600000 -> Formatted: 0.986
2025-11-13 06:27:18,598 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:27:18,984 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:27:18,986 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.986
2025-11-13 06:27:19,379 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:27:19,380 [ERROR]    âŒ Order placement failed!
2025-11-13 06:27:19,781 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:27:20,283 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:27:20,382 [INFO]    Current position: LONG 6.0
2025-11-13 06:27:20,382 [INFO]    Entry: $17.52 | Mark: $17.67
2025-11-13 06:27:20,383 [INFO]    PnL: 0.83% ($0.88)
2025-11-13 06:27:20,383 [INFO]    Age: 0.7h / 36.0h
2025-11-13 06:27:20,883 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:27:20,985 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:27:21,408 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:27:21,409 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:27:21,409 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:27:21,409 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:27:21,410 [INFO]    âšª No signal - HOLD
2025-11-13 06:27:21,410 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:28:21,451 [INFO] 
============================================================
2025-11-13 06:28:21,452 [INFO] ðŸ”„ LOOP #88 - 2025-11-13 06:28:21
2025-11-13 06:28:21,452 [INFO] ============================================================
2025-11-13 06:28:21,555 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:28:21,555 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:28:21,652 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:28:22,032 [INFO] ðŸŽ¯ BTCUSDT Advanced Signal: LONG
2025-11-13 06:28:22,032 [INFO]    ðŸ“Š Confluence Score: 6/4
2025-11-13 06:28:22,032 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:28:22,032 [INFO]       1. ðŸ”· Bullish Order Block
2025-11-13 06:28:22,032 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:28:22,032 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.594 | RSI: 65.7 | OB: 7.28
2025-11-13 06:28:22,033 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=6
2025-11-13 06:28:22,033 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:28:22,033 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:28:22,033 [INFO]    ðŸ“Š Confluence score: 6/4
2025-11-13 06:28:22,034 [INFO]    ðŸ“ Top reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:28:22,034 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:28:22,132 [INFO] âœ… Set leverage 10x for BTCUSDT
2025-11-13 06:28:22,333 [INFO]    ðŸ’µ Current price: $103525.80
2025-11-13 06:28:22,334 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:28:22,334 [INFO]       Balance: $18.75
2025-11-13 06:28:22,334 [INFO]       Price: $103525.80
2025-11-13 06:28:22,334 [INFO]       Capital (fixed): $10.00
2025-11-13 06:28:22,334 [INFO]       Leverage: 10x
2025-11-13 06:28:22,334 [INFO]       Raw quantity: 0.00096594
2025-11-13 06:28:22,334 [INFO]       Formatted quantity: 0.00100000
2025-11-13 06:28:22,334 [INFO]    ðŸ“¤ Placing BUY order for 0.001 BTCUSDT...
2025-11-13 06:28:22,334 [INFO] ðŸ“ Order: BUY BTCUSDT
2025-11-13 06:28:22,335 [INFO]    Raw qty: 0.00100000 -> Formatted: 0.001
2025-11-13 06:28:22,685 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:28:23,415 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:28:23,421 [ERROR]    Symbol: BTCUSDT, Side: BUY, Qty: 0.001
2025-11-13 06:28:23,831 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:28:23,836 [ERROR]    âŒ Order placement failed!
2025-11-13 06:28:24,228 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:28:24,730 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:28:24,831 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:28:25,201 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:28:25,202 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:28:25,202 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:28:25,202 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:28:25,202 [INFO]    âšª No signal - HOLD
2025-11-13 06:28:25,703 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:28:25,808 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:28:26,204 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:28:26,204 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(3): ðŸ“Œ Bearish Pin Bar
2025-11-13 06:28:26,205 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:28:26,206 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:28:26,206 [INFO]    âšª No signal - HOLD
2025-11-13 06:28:26,707 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:28:26,807 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:28:27,177 [INFO] ðŸŽ¯ LTCUSDT Advanced Signal: LONG
2025-11-13 06:28:27,178 [INFO]    ðŸ“Š Confluence Score: 5/4
2025-11-13 06:28:27,178 [INFO]    ðŸ“ Top Reasons:
2025-11-13 06:28:27,178 [INFO]       1. ðŸ“Š Bullish FVG
2025-11-13 06:28:27,178 [INFO]       2. ðŸ”€ Bullish RSI Divergence
2025-11-13 06:28:27,178 [INFO]    ðŸ“ˆ Legacy Signals - LSTM: 0.532 | RSI: 66.7 | OB: 0.88
2025-11-13 06:28:27,179 [INFO]    ðŸ“Š Analysis complete: Signal=LONG, Score=5
2025-11-13 06:28:27,179 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:28:27,179 [INFO]    ðŸŸ¢ Entry signal detected: LONG
2025-11-13 06:28:27,179 [INFO]    ðŸ“Š Confluence score: 5/4
2025-11-13 06:28:27,179 [INFO]    ðŸ“ Top reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:28:27,180 [INFO]    âš™ï¸ Setting up leverage 10x and ISOLATED margin...
2025-11-13 06:28:27,383 [INFO] âœ… Set leverage 10x for LTCUSDT
2025-11-13 06:28:27,583 [INFO]    ðŸ’µ Current price: $101.41
2025-11-13 06:28:27,584 [INFO]    ðŸ’° Position calculation:
2025-11-13 06:28:27,584 [INFO]       Balance: $18.75
2025-11-13 06:28:27,584 [INFO]       Price: $101.41
2025-11-13 06:28:27,584 [INFO]       Capital (fixed): $10.00
2025-11-13 06:28:27,584 [INFO]       Leverage: 10x
2025-11-13 06:28:27,584 [INFO]       Raw quantity: 0.98609605
2025-11-13 06:28:27,584 [INFO]       Formatted quantity: 0.98600000
2025-11-13 06:28:27,584 [INFO]    ðŸ“¤ Placing BUY order for 0.986 LTCUSDT...
2025-11-13 06:28:27,584 [INFO] ðŸ“ Order: BUY LTCUSDT
2025-11-13 06:28:27,584 [INFO]    Raw qty: 0.98600000 -> Formatted: 0.986
2025-11-13 06:28:27,936 [ERROR] Create order error: APIError(code=-2019): Margin is insufficient.
2025-11-13 06:28:28,336 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:28:28,338 [ERROR]    Symbol: LTCUSDT, Side: BUY, Qty: 0.986
2025-11-13 06:28:28,725 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:28:28,727 [ERROR]    âŒ Order placement failed!
2025-11-13 06:28:29,112 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:28:29,615 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:28:29,716 [INFO]    Current position: LONG 6.0
2025-11-13 06:28:29,716 [INFO]    Entry: $17.52 | Mark: $17.67
2025-11-13 06:28:29,716 [INFO]    PnL: 0.85% ($0.89)
2025-11-13 06:28:29,716 [INFO]    Age: 0.7h / 36.0h
2025-11-13 06:28:30,217 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:28:30,319 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:28:30,698 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:28:30,698 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:28:30,698 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:28:30,699 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:28:30,699 [INFO]    âšª No signal - HOLD
2025-11-13 06:28:30,699 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:28:39,421 [INFO] 
ðŸ›‘ Shutdown signal received...
2025-11-13 06:29:30,749 [INFO] 
============================================================
2025-11-13 06:29:30,750 [INFO] ðŸ›‘ SHUTTING DOWN BOT
2025-11-13 06:29:30,750 [INFO] ============================================================
2025-11-13 06:29:30,750 [INFO] ðŸ“Š <b>DAILY STATS</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
Trades: 2
Volume: $0.00M
PnL: 0.00%

<b>Overall</b>
Total Trades: 2
Win Rate: 50.0%
W/L: 1/0
2025-11-13 06:29:31,465 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:29:31,468 [INFO] ðŸ‘‹ Bot stopped!
2025-11-13 06:29:31,862 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
âœ… Using fixed position size: $10.0 USDT per trade
âœ… Config validation passed!
2025-11-13 06:29:37,783 [INFO] âœ… Telegram bot initialized
2025-11-13 06:29:45,759 [INFO] ============================================================
2025-11-13 06:29:45,760 [INFO] ðŸš€ ASTERDEX PERP FARM BOT - INITIALIZING
2025-11-13 06:29:45,760 [INFO] ============================================================
2025-11-13 06:29:46,170 [INFO] ðŸ”Œ AsterDEX Client initialized (MAINNET)
2025-11-13 06:29:46,170 [INFO]    URL: https://fapi.asterdex.com/fapi
2025-11-13 06:29:46,171 [INFO] ðŸ“‚ Loaded 1 position timestamps
2025-11-13 06:29:46,171 [INFO] ðŸ“ˆ Trailing Stop enabled: Activation=1.0%, Trail=0.3%
2025-11-13 06:29:46,171 [INFO] ðŸŽ­ Loading Ensemble models...
2025-11-13 06:29:46,213 [INFO] ðŸ§  LSTM Model initialized on cpu
2025-11-13 06:29:46,214 [INFO]    Input: 14, Hidden: 128, Layers: 3, Dropout: 0.3
2025-11-13 06:29:46,214 [INFO] ðŸŽ­ Ensemble initialized with 2 models
2025-11-13 06:29:46,214 [INFO]    Models: ['lstm', 'xgboost']
2025-11-13 06:29:46,215 [INFO]    Weights: [0.3 0.7]
2025-11-13 06:29:46,238 [INFO] âœ… Model loaded from models/lstm_model.pt
2025-11-13 06:29:46,239 [INFO] âœ… LSTM loaded
2025-11-13 06:29:46,308 [INFO] âœ… XGBoost model loaded from models/xgboost_model.json
2025-11-13 06:29:46,308 [INFO] âœ… XGBoost loaded
2025-11-13 06:29:46,308 [INFO] âœ… Ensemble loaded: 2/2 models
2025-11-13 06:29:46,308 [INFO] ðŸŽ­ Using Ensemble predictor: ['lstm', 'xgboost']
2025-11-13 06:29:46,308 [INFO]    Weights: [0.3, 0.7]
2025-11-13 06:29:46,308 [INFO] ðŸŽ¯ Advanced Entry System enabled (min score: 4)
2025-11-13 06:29:46,308 [INFO] ðŸš« Signal Cooldown enabled: 60 minutes
2025-11-13 06:29:46,309 [INFO] âœ… Bot initialized successfully!
2025-11-13 06:29:46,309 [INFO]    Symbols: ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'LTCUSDT', 'AVAXUSDT', 'XRPUSDT']
2025-11-13 06:29:46,309 [INFO]    Leverage: 10x
2025-11-13 06:29:46,309 [INFO]    Position Size: 20.0%
2025-11-13 06:29:46,309 [INFO]    TP/SL: 1.00% / Disabled
2025-11-13 06:29:46,309 [INFO]    Position Timeout: 36.0h
2025-11-13 06:29:46,309 [INFO] ============================================================
2025-11-13 06:29:46,309 [INFO] ðŸ BOT STARTED!
2025-11-13 06:29:47,089 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:29:47,277 [INFO] ðŸ“Š Daily start balance: $18.75
2025-11-13 06:29:47,277 [INFO] ðŸ’° Starting balance: $18.75
2025-11-13 06:29:47,708 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 06:29:47,710 [INFO] 
============================================================
2025-11-13 06:29:47,710 [INFO] ðŸ”„ LOOP #1 - 2025-11-13 06:29:47
2025-11-13 06:29:47,711 [INFO] ============================================================
2025-11-13 06:29:47,800 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:29:47,800 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:29:47,885 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:29:48,280 [INFO]    ðŸš« ML Conviction too low: 0.598 (distance from 0.5: 0.098 < 0.1)
2025-11-13 06:29:48,280 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 6/4)
2025-11-13 06:29:48,280 [INFO]    Partial signals: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:29:48,281 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=6
2025-11-13 06:29:48,281 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:29:48,281 [INFO]    âšª No signal - HOLD
2025-11-13 06:29:48,782 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:29:48,873 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:29:49,223 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:29:49,224 [INFO]    Partial signals: SHORT(3): ðŸ“ˆ RSI Overbought, SHORT(3): ðŸ“ˆ Volume Spike
2025-11-13 06:29:49,224 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:29:49,225 [INFO]    ðŸ“ Signal reasons: SHORT(3): ðŸ“ˆ RSI Overbought, SHORT(3): ðŸ“ˆ Volume Spike
2025-11-13 06:29:49,225 [INFO]    âšª No signal - HOLD
2025-11-13 06:29:49,726 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:29:49,818 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:29:50,147 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:29:50,148 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:29:50,148 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:29:50,149 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:29:50,149 [INFO]    âšª No signal - HOLD
2025-11-13 06:29:50,653 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:29:50,743 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:29:51,073 [INFO]    ðŸš« ML Conviction too low: 0.530 (distance from 0.5: 0.030 < 0.1)
2025-11-13 06:29:51,073 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 5/4)
2025-11-13 06:29:51,074 [INFO]    Partial signals: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:29:51,074 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 06:29:51,074 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:29:51,074 [INFO]    âšª No signal - HOLD
2025-11-13 06:29:51,575 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:29:51,663 [INFO]    Current position: LONG 6.0
2025-11-13 06:29:51,664 [INFO]    Entry: $17.52 | Mark: $17.68
2025-11-13 06:29:51,664 [INFO]    PnL: 0.89% ($0.94)
2025-11-13 06:29:51,664 [INFO]    Age: 0.7h / 36.0h
2025-11-13 06:29:52,165 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:29:52,251 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:29:52,577 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:29:52,578 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:29:52,578 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:29:52,578 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:29:52,578 [INFO]    âšª No signal - HOLD
2025-11-13 06:29:52,578 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:30:52,637 [INFO] 
============================================================
2025-11-13 06:30:52,638 [INFO] ðŸ”„ LOOP #2 - 2025-11-13 06:30:52
2025-11-13 06:30:52,638 [INFO] ============================================================
2025-11-13 06:30:52,724 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:30:52,725 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:30:52,814 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:30:53,145 [INFO]    ðŸš« ML Conviction too low: 0.585 (distance from 0.5: 0.085 < 0.1)
2025-11-13 06:30:53,146 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 5/4)
2025-11-13 06:30:53,146 [INFO]    Partial signals: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:30:53,146 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 06:30:53,146 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:30:53,146 [INFO]    âšª No signal - HOLD
2025-11-13 06:30:53,647 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:30:53,732 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:30:54,062 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:30:54,062 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:30:54,063 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:30:54,063 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:30:54,063 [INFO]    âšª No signal - HOLD
2025-11-13 06:30:54,564 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:30:54,652 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:30:54,979 [INFO]    ðŸš« ML Conviction too low: 0.574 (distance from 0.5: 0.074 < 0.1)
2025-11-13 06:30:54,979 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 5/4)
2025-11-13 06:30:54,979 [INFO]    Partial signals: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:30:54,980 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 06:30:54,980 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:30:54,980 [INFO]    âšª No signal - HOLD
2025-11-13 06:30:55,481 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:30:55,566 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:30:55,953 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:30:55,953 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:30:55,954 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:30:55,954 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:30:55,954 [INFO]    âšª No signal - HOLD
2025-11-13 06:30:56,455 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:30:56,681 [INFO]    Current position: LONG 6.0
2025-11-13 06:30:56,683 [INFO]    Entry: $17.52 | Mark: $17.68
2025-11-13 06:30:56,683 [INFO]    PnL: 0.91% ($0.96)
2025-11-13 06:30:56,683 [INFO]    Age: 0.8h / 36.0h
2025-11-13 06:30:57,184 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:30:57,272 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:30:57,595 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:30:57,595 [INFO]    Partial signals: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:30:57,596 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:30:57,596 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Š Bullish FVG, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:30:57,596 [INFO]    âšª No signal - HOLD
2025-11-13 06:30:57,596 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:31:57,640 [INFO] 
============================================================
2025-11-13 06:31:57,640 [INFO] ðŸ”„ LOOP #3 - 2025-11-13 06:31:57
2025-11-13 06:31:57,641 [INFO] ============================================================
2025-11-13 06:31:57,726 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:31:57,726 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:31:57,811 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:31:58,139 [INFO]    ðŸš« ML Conviction too low: 0.596 (distance from 0.5: 0.096 < 0.1)
2025-11-13 06:31:58,139 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 5/4)
2025-11-13 06:31:58,139 [INFO]    Partial signals: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:31:58,139 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 06:31:58,139 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:31:58,139 [INFO]    âšª No signal - HOLD
2025-11-13 06:31:58,640 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:31:58,726 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:31:59,060 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:31:59,060 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:31:59,061 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:31:59,061 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:31:59,061 [INFO]    âšª No signal - HOLD
2025-11-13 06:31:59,561 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:31:59,650 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:31:59,989 [INFO]    ðŸš« ML Conviction too low: 0.577 (distance from 0.5: 0.077 < 0.1)
2025-11-13 06:31:59,989 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 5/4)
2025-11-13 06:31:59,989 [INFO]    Partial signals: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:31:59,990 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 06:31:59,990 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:31:59,990 [INFO]    âšª No signal - HOLD
2025-11-13 06:32:00,491 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:32:00,578 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:32:00,895 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:32:00,895 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:32:00,896 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:32:00,896 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:32:00,896 [INFO]    âšª No signal - HOLD
2025-11-13 06:32:01,398 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:32:01,488 [INFO]    Current position: LONG 6.0
2025-11-13 06:32:01,489 [INFO]    Entry: $17.52 | Mark: $17.66
2025-11-13 06:32:01,489 [INFO]    PnL: 0.80% ($0.84)
2025-11-13 06:32:01,489 [INFO]    Age: 0.8h / 36.0h
2025-11-13 06:32:01,990 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:32:02,083 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:32:02,404 [INFO]    ðŸš« ML Conviction too low: 0.497 (distance from 0.5: 0.003 < 0.1)
2025-11-13 06:32:02,405 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:32:02,405 [INFO]    Partial signals: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:32:02,405 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:32:02,405 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:32:02,405 [INFO]    âšª No signal - HOLD
2025-11-13 06:32:02,406 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:33:02,445 [INFO] 
============================================================
2025-11-13 06:33:02,445 [INFO] ðŸ”„ LOOP #4 - 2025-11-13 06:33:02
2025-11-13 06:33:02,446 [INFO] ============================================================
2025-11-13 06:33:02,537 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:33:02,537 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:33:02,623 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:33:02,954 [INFO]    ðŸš« ML Conviction too low: 0.599 (distance from 0.5: 0.099 < 0.1)
2025-11-13 06:33:02,954 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 5/4)
2025-11-13 06:33:02,954 [INFO]    Partial signals: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:33:02,955 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 06:33:02,955 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:33:02,955 [INFO]    âšª No signal - HOLD
2025-11-13 06:33:03,456 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:33:03,543 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:33:03,873 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:33:03,874 [INFO]    Partial signals: SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:33:03,874 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:33:03,875 [INFO]    ðŸ“ Signal reasons: SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:33:03,875 [INFO]    âšª No signal - HOLD
2025-11-13 06:33:04,376 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:33:04,466 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:33:04,806 [INFO]    ðŸš« ML Conviction too low: 0.576 (distance from 0.5: 0.076 < 0.1)
2025-11-13 06:33:04,806 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 5/4)
2025-11-13 06:33:04,806 [INFO]    Partial signals: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:33:04,807 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 06:33:04,807 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:33:04,807 [INFO]    âšª No signal - HOLD
2025-11-13 06:33:05,308 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:33:05,397 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:33:05,723 [INFO]    ðŸš« ML Conviction too low: 0.533 (distance from 0.5: 0.033 < 0.1)
2025-11-13 06:33:05,723 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:33:05,723 [INFO]    Partial signals: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:33:05,724 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:33:05,724 [INFO]    ðŸ“ Signal reasons: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:33:05,724 [INFO]    âšª No signal - HOLD
2025-11-13 06:33:06,225 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:33:06,318 [INFO]    Current position: LONG 6.0
2025-11-13 06:33:06,318 [INFO]    Entry: $17.52 | Mark: $17.66
2025-11-13 06:33:06,318 [INFO]    PnL: 0.79% ($0.83)
2025-11-13 06:33:06,318 [INFO]    Age: 0.8h / 36.0h
2025-11-13 06:33:06,819 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:33:06,907 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:33:07,261 [INFO]    ðŸš« ML Conviction too low: 0.490 (distance from 0.5: 0.010 < 0.1)
2025-11-13 06:33:07,261 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:33:07,261 [INFO]    Partial signals: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:33:07,262 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:33:07,262 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:33:07,262 [INFO]    âšª No signal - HOLD
2025-11-13 06:33:07,262 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:34:07,322 [INFO] 
============================================================
2025-11-13 06:34:07,322 [INFO] ðŸ”„ LOOP #5 - 2025-11-13 06:34:07
2025-11-13 06:34:07,323 [INFO] ============================================================
2025-11-13 06:34:07,853 [INFO] ðŸ’“ Bot alive - Loop #5 - Active positions: 1
2025-11-13 06:34:07,938 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:34:07,938 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:34:08,023 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:34:08,349 [INFO]    ðŸš« ML Conviction too low: 0.597 (distance from 0.5: 0.097 < 0.1)
2025-11-13 06:34:08,349 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 5/4)
2025-11-13 06:34:08,355 [INFO]    Partial signals: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:34:08,356 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 06:34:08,356 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:34:08,357 [INFO]    âšª No signal - HOLD
2025-11-13 06:34:08,857 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:34:08,945 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:34:09,252 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:34:09,252 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:34:09,253 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:34:09,253 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:34:09,253 [INFO]    âšª No signal - HOLD
2025-11-13 06:34:09,754 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:34:09,840 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:34:10,171 [INFO]    ðŸš« ML Conviction too low: 0.564 (distance from 0.5: 0.064 < 0.1)
2025-11-13 06:34:10,172 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 5/4)
2025-11-13 06:34:10,172 [INFO]    Partial signals: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:34:10,172 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 06:34:10,172 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:34:10,172 [INFO]    âšª No signal - HOLD
2025-11-13 06:34:10,673 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:34:10,756 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:34:11,089 [INFO]    ðŸš« ML Conviction too low: 0.538 (distance from 0.5: 0.038 < 0.1)
2025-11-13 06:34:11,089 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:34:11,090 [INFO]    Partial signals: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:34:11,090 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:34:11,090 [INFO]    ðŸ“ Signal reasons: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:34:11,090 [INFO]    âšª No signal - HOLD
2025-11-13 06:34:11,591 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:34:11,677 [INFO]    Current position: LONG 6.0
2025-11-13 06:34:11,677 [INFO]    Entry: $17.52 | Mark: $17.66
2025-11-13 06:34:11,677 [INFO]    PnL: 0.80% ($0.84)
2025-11-13 06:34:11,677 [INFO]    Age: 0.8h / 36.0h
2025-11-13 06:34:12,178 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:34:12,271 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:34:12,595 [INFO]    ðŸš« ML Conviction too low: 0.484 (distance from 0.5: 0.016 < 0.1)
2025-11-13 06:34:12,595 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:34:12,595 [INFO]    Partial signals: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:34:12,596 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:34:12,596 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:34:12,596 [INFO]    âšª No signal - HOLD
2025-11-13 06:34:12,596 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:35:12,656 [INFO] 
============================================================
2025-11-13 06:35:12,657 [INFO] ðŸ”„ LOOP #6 - 2025-11-13 06:35:12
2025-11-13 06:35:12,657 [INFO] ============================================================
2025-11-13 06:35:12,743 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:35:12,743 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:35:12,834 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:35:13,166 [INFO]    ðŸš« ML Conviction too low: 0.597 (distance from 0.5: 0.097 < 0.1)
2025-11-13 06:35:13,166 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 5/4)
2025-11-13 06:35:13,166 [INFO]    Partial signals: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:35:13,167 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 06:35:13,167 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:35:13,167 [INFO]    âšª No signal - HOLD
2025-11-13 06:35:13,668 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:35:13,762 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:35:14,076 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:35:14,077 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:35:14,078 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:35:14,078 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:35:14,078 [INFO]    âšª No signal - HOLD
2025-11-13 06:35:14,579 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:35:14,667 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:35:14,987 [INFO]    ðŸš« ML Conviction too low: 0.567 (distance from 0.5: 0.067 < 0.1)
2025-11-13 06:35:14,988 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 5/4)
2025-11-13 06:35:14,988 [INFO]    Partial signals: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:35:14,988 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 06:35:14,989 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:35:14,989 [INFO]    âšª No signal - HOLD
2025-11-13 06:35:15,489 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:35:15,576 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:35:15,894 [INFO]    ðŸš« ML Conviction too low: 0.541 (distance from 0.5: 0.041 < 0.1)
2025-11-13 06:35:15,894 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:35:15,894 [INFO]    Partial signals: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:35:15,895 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:35:15,895 [INFO]    ðŸ“ Signal reasons: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:35:15,895 [INFO]    âšª No signal - HOLD
2025-11-13 06:35:16,396 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:35:16,481 [INFO]    Current position: LONG 6.0
2025-11-13 06:35:16,481 [INFO]    Entry: $17.52 | Mark: $17.66
2025-11-13 06:35:16,481 [INFO]    PnL: 0.81% ($0.85)
2025-11-13 06:35:16,481 [INFO]    Age: 0.8h / 36.0h
2025-11-13 06:35:16,982 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:35:17,070 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:35:17,385 [INFO]    ðŸš« ML Conviction too low: 0.490 (distance from 0.5: 0.010 < 0.1)
2025-11-13 06:35:17,385 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:35:17,385 [INFO]    Partial signals: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:35:17,386 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:35:17,386 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:35:17,386 [INFO]    âšª No signal - HOLD
2025-11-13 06:35:17,386 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:36:17,436 [INFO] 
============================================================
2025-11-13 06:36:17,436 [INFO] ðŸ”„ LOOP #7 - 2025-11-13 06:36:17
2025-11-13 06:36:17,436 [INFO] ============================================================
2025-11-13 06:36:17,539 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:36:17,539 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:36:17,651 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:36:17,970 [INFO]    ðŸš« ML Conviction too low: 0.599 (distance from 0.5: 0.099 < 0.1)
2025-11-13 06:36:17,971 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 6/4)
2025-11-13 06:36:17,971 [INFO]    Partial signals: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:36:17,971 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=6
2025-11-13 06:36:17,972 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:36:17,972 [INFO]    âšª No signal - HOLD
2025-11-13 06:36:18,472 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:36:18,562 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:36:18,891 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:36:18,892 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:36:18,892 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:36:18,893 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:36:18,893 [INFO]    âšª No signal - HOLD
2025-11-13 06:36:19,393 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:36:19,592 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:36:19,908 [INFO]    ðŸš« ML Conviction too low: 0.543 (distance from 0.5: 0.043 < 0.1)
2025-11-13 06:36:19,909 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 5/4)
2025-11-13 06:36:19,909 [INFO]    Partial signals: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:36:19,910 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 06:36:19,910 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:36:19,910 [INFO]    âšª No signal - HOLD
2025-11-13 06:36:20,411 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:36:20,509 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:36:20,851 [INFO]    ðŸš« ML Conviction too low: 0.538 (distance from 0.5: 0.038 < 0.1)
2025-11-13 06:36:20,851 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:36:20,852 [INFO]    Partial signals: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:36:20,852 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:36:20,853 [INFO]    ðŸ“ Signal reasons: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:36:20,853 [INFO]    âšª No signal - HOLD
2025-11-13 06:36:21,354 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:36:21,447 [INFO]    Current position: LONG 6.0
2025-11-13 06:36:21,448 [INFO]    Entry: $17.52 | Mark: $17.66
2025-11-13 06:36:21,448 [INFO]    PnL: 0.80% ($0.84)
2025-11-13 06:36:21,448 [INFO]    Age: 0.9h / 36.0h
2025-11-13 06:36:21,949 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:36:22,038 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:36:22,357 [INFO]    ðŸš« ML Conviction too low: 0.462 (distance from 0.5: 0.038 < 0.1)
2025-11-13 06:36:22,357 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:36:22,358 [INFO]    Partial signals: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:36:22,358 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:36:22,358 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:36:22,358 [INFO]    âšª No signal - HOLD
2025-11-13 06:36:22,358 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:37:22,371 [INFO] 
============================================================
2025-11-13 06:37:22,371 [INFO] ðŸ”„ LOOP #8 - 2025-11-13 06:37:22
2025-11-13 06:37:22,371 [INFO] ============================================================
2025-11-13 06:37:22,462 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:37:22,462 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:37:22,549 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:37:22,880 [INFO]    ðŸš« ML Conviction too low: 0.599 (distance from 0.5: 0.099 < 0.1)
2025-11-13 06:37:22,881 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 6/4)
2025-11-13 06:37:22,881 [INFO]    Partial signals: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:37:22,882 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=6
2025-11-13 06:37:22,882 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:37:22,882 [INFO]    âšª No signal - HOLD
2025-11-13 06:37:23,383 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:37:23,473 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:37:23,807 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:37:23,807 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:37:23,807 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:37:23,808 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:37:23,808 [INFO]    âšª No signal - HOLD
2025-11-13 06:37:24,309 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:37:24,393 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:37:24,847 [INFO]    ðŸš« ML Conviction too low: 0.557 (distance from 0.5: 0.057 < 0.1)
2025-11-13 06:37:24,847 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 5/4)
2025-11-13 06:37:24,848 [INFO]    Partial signals: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:37:24,848 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 06:37:24,848 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:37:24,849 [INFO]    âšª No signal - HOLD
2025-11-13 06:37:25,349 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:37:25,439 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:37:25,843 [INFO]    ðŸš« ML Conviction too low: 0.570 (distance from 0.5: 0.070 < 0.1)
2025-11-13 06:37:25,843 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:37:25,843 [INFO]    Partial signals: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:37:25,844 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:37:25,844 [INFO]    ðŸ“ Signal reasons: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:37:25,844 [INFO]    âšª No signal - HOLD
2025-11-13 06:37:26,345 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:37:26,432 [INFO]    Current position: LONG 6.0
2025-11-13 06:37:26,433 [INFO]    Entry: $17.52 | Mark: $17.65
2025-11-13 06:37:26,433 [INFO]    PnL: 0.76% ($0.79)
2025-11-13 06:37:26,433 [INFO]    Age: 0.9h / 36.0h
2025-11-13 06:37:26,934 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:37:27,019 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:37:27,341 [INFO]    ðŸš« ML Conviction too low: 0.492 (distance from 0.5: 0.008 < 0.1)
2025-11-13 06:37:27,341 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:37:27,342 [INFO]    Partial signals: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:37:27,342 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:37:27,342 [INFO]    ðŸ“ Signal reasons: ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:37:27,343 [INFO]    âšª No signal - HOLD
2025-11-13 06:37:27,343 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:38:27,371 [INFO] 
============================================================
2025-11-13 06:38:27,371 [INFO] ðŸ”„ LOOP #9 - 2025-11-13 06:38:27
2025-11-13 06:38:27,371 [INFO] ============================================================
2025-11-13 06:38:27,472 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:38:27,472 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:38:27,558 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:38:27,890 [INFO]    ðŸš« ML Conviction too low: 0.596 (distance from 0.5: 0.096 < 0.1)
2025-11-13 06:38:27,890 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 6/4)
2025-11-13 06:38:27,890 [INFO]    Partial signals: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:38:27,891 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=6
2025-11-13 06:38:27,891 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:38:27,891 [INFO]    âšª No signal - HOLD
2025-11-13 06:38:28,392 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:38:28,482 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:38:28,806 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:38:28,806 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:38:28,807 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:38:28,807 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:38:28,807 [INFO]    âšª No signal - HOLD
2025-11-13 06:38:29,308 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:38:29,397 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:38:29,714 [INFO]    ðŸš« ML Conviction too low: 0.567 (distance from 0.5: 0.067 < 0.1)
2025-11-13 06:38:29,714 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 5/4)
2025-11-13 06:38:29,714 [INFO]    Partial signals: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:38:29,715 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 06:38:29,715 [INFO]    ðŸ“ Signal reasons: ðŸ“Š Bullish FVG, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:38:29,715 [INFO]    âšª No signal - HOLD
2025-11-13 06:38:30,216 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:38:30,302 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:38:30,655 [INFO]    ðŸš« ML Conviction too low: 0.586 (distance from 0.5: 0.086 < 0.1)
2025-11-13 06:38:30,656 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:38:30,656 [INFO]    Partial signals: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:38:30,656 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:38:30,656 [INFO]    ðŸ“ Signal reasons: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:38:30,656 [INFO]    âšª No signal - HOLD
2025-11-13 06:38:31,157 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:38:31,247 [INFO]    Current position: LONG 6.0
2025-11-13 06:38:31,248 [INFO]    Entry: $17.52 | Mark: $17.67
2025-11-13 06:38:31,248 [INFO]    PnL: 0.82% ($0.87)
2025-11-13 06:38:31,248 [INFO]    Age: 0.9h / 36.0h
2025-11-13 06:38:31,748 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:38:31,844 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:38:32,160 [INFO]    ðŸš« ML Conviction too low: 0.486 (distance from 0.5: 0.014 < 0.1)
2025-11-13 06:38:32,161 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 7/4)
2025-11-13 06:38:32,161 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:38:32,162 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-11-13 06:38:32,162 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:38:32,162 [INFO]    âšª No signal - HOLD
2025-11-13 06:38:32,162 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:39:32,211 [INFO] 
============================================================
2025-11-13 06:39:32,211 [INFO] ðŸ”„ LOOP #10 - 2025-11-13 06:39:32
2025-11-13 06:39:32,211 [INFO] ============================================================
2025-11-13 06:39:32,730 [INFO] ðŸ’“ Bot alive - Loop #10 - Active positions: 1
2025-11-13 06:39:32,818 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:39:32,818 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:39:32,908 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:39:33,222 [INFO]    ðŸš« ML Conviction too low: 0.592 (distance from 0.5: 0.092 < 0.1)
2025-11-13 06:39:33,222 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 6/4)
2025-11-13 06:39:33,222 [INFO]    Partial signals: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:39:33,222 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=6
2025-11-13 06:39:33,223 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:39:33,223 [INFO]    âšª No signal - HOLD
2025-11-13 06:39:33,723 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:39:33,817 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:39:34,261 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:39:34,261 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:39:34,262 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:39:34,262 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:39:34,262 [INFO]    âšª No signal - HOLD
2025-11-13 06:39:34,763 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:39:34,852 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:39:35,165 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:39:35,166 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(3): ðŸ“Œ Bearish Pin Bar
2025-11-13 06:39:35,166 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:39:35,167 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:39:35,167 [INFO]    âšª No signal - HOLD
2025-11-13 06:39:35,667 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:39:35,753 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:39:36,056 [INFO]    ðŸš« ML Conviction too low: 0.579 (distance from 0.5: 0.079 < 0.1)
2025-11-13 06:39:36,056 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:39:36,056 [INFO]    Partial signals: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:39:36,057 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:39:36,057 [INFO]    ðŸ“ Signal reasons: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:39:36,057 [INFO]    âšª No signal - HOLD
2025-11-13 06:39:36,558 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:39:36,642 [INFO]    Current position: LONG 6.0
2025-11-13 06:39:36,642 [INFO]    Entry: $17.52 | Mark: $17.65
2025-11-13 06:39:36,642 [INFO]    PnL: 0.72% ($0.76)
2025-11-13 06:39:36,643 [INFO]    Age: 0.9h / 36.0h
2025-11-13 06:39:37,143 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:39:37,228 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:39:37,537 [INFO]    ðŸš« ML Conviction too low: 0.464 (distance from 0.5: 0.036 < 0.1)
2025-11-13 06:39:37,537 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 7/4)
2025-11-13 06:39:37,537 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:39:37,538 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-11-13 06:39:37,538 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:39:37,538 [INFO]    âšª No signal - HOLD
2025-11-13 06:39:38,054 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:40:38,066 [INFO] 
============================================================
2025-11-13 06:40:38,066 [INFO] ðŸ”„ LOOP #11 - 2025-11-13 06:40:38
2025-11-13 06:40:38,066 [INFO] ============================================================
2025-11-13 06:40:38,157 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:40:38,157 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:40:38,243 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:40:38,575 [INFO]    ðŸš« ML Conviction too low: 0.590 (distance from 0.5: 0.090 < 0.1)
2025-11-13 06:40:38,576 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 6/4)
2025-11-13 06:40:38,576 [INFO]    Partial signals: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:40:38,576 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=6
2025-11-13 06:40:38,576 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:40:38,576 [INFO]    âšª No signal - HOLD
2025-11-13 06:40:39,077 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:40:39,163 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:40:39,469 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:40:39,469 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:40:39,470 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:40:39,470 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:40:39,470 [INFO]    âšª No signal - HOLD
2025-11-13 06:40:39,971 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:40:40,057 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:40:40,384 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:40:40,399 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(3): ðŸ“Œ Bearish Pin Bar
2025-11-13 06:40:40,399 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:40:40,399 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:40:40,400 [INFO]    âšª No signal - HOLD
2025-11-13 06:40:40,900 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:40:40,987 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:40:41,297 [INFO]    ðŸš« ML Conviction too low: 0.574 (distance from 0.5: 0.074 < 0.1)
2025-11-13 06:40:41,297 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:40:41,297 [INFO]    Partial signals: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:40:41,298 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:40:41,298 [INFO]    ðŸ“ Signal reasons: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:40:41,298 [INFO]    âšª No signal - HOLD
2025-11-13 06:40:41,799 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:40:41,887 [INFO]    Current position: LONG 6.0
2025-11-13 06:40:41,887 [INFO]    Entry: $17.52 | Mark: $17.64
2025-11-13 06:40:41,887 [INFO]    PnL: 0.67% ($0.70)
2025-11-13 06:40:41,887 [INFO]    Age: 0.9h / 36.0h
2025-11-13 06:40:42,388 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:40:42,473 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:40:42,783 [INFO]    ðŸš« ML Conviction too low: 0.481 (distance from 0.5: 0.019 < 0.1)
2025-11-13 06:40:42,783 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 7/4)
2025-11-13 06:40:42,783 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:40:42,783 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-11-13 06:40:42,784 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:40:42,784 [INFO]    âšª No signal - HOLD
2025-11-13 06:40:42,784 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:41:42,800 [INFO] 
============================================================
2025-11-13 06:41:42,800 [INFO] ðŸ”„ LOOP #12 - 2025-11-13 06:41:42
2025-11-13 06:41:42,800 [INFO] ============================================================
2025-11-13 06:41:42,890 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:41:42,890 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:41:42,978 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:41:43,293 [INFO]    ðŸš« ML Conviction too low: 0.590 (distance from 0.5: 0.090 < 0.1)
2025-11-13 06:41:43,293 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 8/4)
2025-11-13 06:41:43,293 [INFO]    Partial signals: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:41:43,294 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=8
2025-11-13 06:41:43,294 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence, ðŸ“ˆ Volume Spike
2025-11-13 06:41:43,294 [INFO]    âšª No signal - HOLD
2025-11-13 06:41:43,795 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:41:43,886 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:41:44,218 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:41:44,218 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:41:44,219 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:41:44,219 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:41:44,219 [INFO]    âšª No signal - HOLD
2025-11-13 06:41:44,720 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:41:44,811 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:41:45,188 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:41:45,189 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:41:45,189 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:41:45,190 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:41:45,190 [INFO]    âšª No signal - HOLD
2025-11-13 06:41:45,690 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:41:45,778 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:41:46,148 [INFO]    ðŸš« ML Conviction too low: 0.578 (distance from 0.5: 0.078 < 0.1)
2025-11-13 06:41:46,148 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:41:46,148 [INFO]    Partial signals: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:41:46,149 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:41:46,149 [INFO]    ðŸ“ Signal reasons: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:41:46,149 [INFO]    âšª No signal - HOLD
2025-11-13 06:41:46,650 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:41:46,751 [INFO]    Current position: LONG 6.0
2025-11-13 06:41:46,751 [INFO]    Entry: $17.52 | Mark: $17.64
2025-11-13 06:41:46,751 [INFO]    PnL: 0.65% ($0.68)
2025-11-13 06:41:46,751 [INFO]    Age: 0.9h / 36.0h
2025-11-13 06:41:47,252 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:41:47,337 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:41:47,807 [INFO]    ðŸš« ML Conviction too low: 0.482 (distance from 0.5: 0.018 < 0.1)
2025-11-13 06:41:47,808 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 7/4)
2025-11-13 06:41:47,808 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:41:47,808 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-11-13 06:41:47,808 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:41:47,809 [INFO]    âšª No signal - HOLD
2025-11-13 06:41:47,809 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:42:47,842 [INFO] 
============================================================
2025-11-13 06:42:47,842 [INFO] ðŸ”„ LOOP #13 - 2025-11-13 06:42:47
2025-11-13 06:42:47,842 [INFO] ============================================================
2025-11-13 06:42:47,927 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:42:47,928 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:42:48,015 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:42:48,328 [INFO]    ðŸš« ML Conviction too low: 0.590 (distance from 0.5: 0.090 < 0.1)
2025-11-13 06:42:48,328 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 8/4)
2025-11-13 06:42:48,328 [INFO]    Partial signals: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:42:48,329 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=8
2025-11-13 06:42:48,329 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence, ðŸ“ˆ Volume Spike
2025-11-13 06:42:48,329 [INFO]    âšª No signal - HOLD
2025-11-13 06:42:48,830 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:42:48,923 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:42:49,259 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:42:49,259 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:42:49,260 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:42:49,260 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:42:49,260 [INFO]    âšª No signal - HOLD
2025-11-13 06:42:49,761 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:42:49,848 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:42:50,177 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:42:50,178 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:42:50,178 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:42:50,178 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:42:50,178 [INFO]    âšª No signal - HOLD
2025-11-13 06:42:50,679 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:42:50,765 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:42:51,089 [INFO]    ðŸš« ML Conviction too low: 0.577 (distance from 0.5: 0.077 < 0.1)
2025-11-13 06:42:51,090 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:42:51,090 [INFO]    Partial signals: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:42:51,091 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:42:51,091 [INFO]    ðŸ“ Signal reasons: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:42:51,091 [INFO]    âšª No signal - HOLD
2025-11-13 06:42:51,592 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:42:51,687 [INFO]    Current position: LONG 6.0
2025-11-13 06:42:51,687 [INFO]    Entry: $17.52 | Mark: $17.62
2025-11-13 06:42:51,687 [INFO]    PnL: 0.59% ($0.62)
2025-11-13 06:42:51,688 [INFO]    Age: 1.0h / 36.0h
2025-11-13 06:42:52,188 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:42:52,275 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:42:52,589 [INFO]    ðŸš« ML Conviction too low: 0.483 (distance from 0.5: 0.017 < 0.1)
2025-11-13 06:42:52,590 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 7/4)
2025-11-13 06:42:52,590 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:42:52,590 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-11-13 06:42:52,590 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:42:52,590 [INFO]    âšª No signal - HOLD
2025-11-13 06:42:52,591 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:43:52,642 [INFO] 
============================================================
2025-11-13 06:43:52,642 [INFO] ðŸ”„ LOOP #14 - 2025-11-13 06:43:52
2025-11-13 06:43:52,642 [INFO] ============================================================
2025-11-13 06:43:52,734 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:43:52,734 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:43:52,822 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:43:53,147 [INFO]    ðŸš« ML Conviction too low: 0.585 (distance from 0.5: 0.085 < 0.1)
2025-11-13 06:43:53,148 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 8/4)
2025-11-13 06:43:53,148 [INFO]    Partial signals: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:43:53,148 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=8
2025-11-13 06:43:53,148 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence, ðŸ“ˆ Volume Spike
2025-11-13 06:43:53,148 [INFO]    âšª No signal - HOLD
2025-11-13 06:43:53,649 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:43:53,735 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:43:54,050 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:43:54,050 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:43:54,051 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:43:54,051 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:43:54,051 [INFO]    âšª No signal - HOLD
2025-11-13 06:43:54,552 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:43:54,638 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:43:55,079 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:43:55,079 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:43:55,080 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:43:55,080 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:43:55,080 [INFO]    âšª No signal - HOLD
2025-11-13 06:43:55,581 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:43:55,669 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:43:55,985 [INFO]    ðŸš« ML Conviction too low: 0.577 (distance from 0.5: 0.077 < 0.1)
2025-11-13 06:43:55,985 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:43:55,985 [INFO]    Partial signals: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:43:55,986 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:43:55,986 [INFO]    ðŸ“ Signal reasons: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:43:55,986 [INFO]    âšª No signal - HOLD
2025-11-13 06:43:56,487 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:43:56,574 [INFO]    Current position: LONG 6.0
2025-11-13 06:43:56,574 [INFO]    Entry: $17.52 | Mark: $17.64
2025-11-13 06:43:56,575 [INFO]    PnL: 0.65% ($0.69)
2025-11-13 06:43:56,575 [INFO]    Age: 1.0h / 36.0h
2025-11-13 06:43:57,075 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:43:57,158 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:43:57,473 [INFO]    ðŸš« ML Conviction too low: 0.471 (distance from 0.5: 0.029 < 0.1)
2025-11-13 06:43:57,474 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 7/4)
2025-11-13 06:43:57,474 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:43:57,474 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-11-13 06:43:57,474 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:43:57,474 [INFO]    âšª No signal - HOLD
2025-11-13 06:43:57,474 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:44:57,501 [INFO] 
============================================================
2025-11-13 06:44:57,502 [INFO] ðŸ”„ LOOP #15 - 2025-11-13 06:44:57
2025-11-13 06:44:57,502 [INFO] ============================================================
2025-11-13 06:44:58,012 [INFO] ðŸ’“ Bot alive - Loop #15 - Active positions: 1
2025-11-13 06:44:58,099 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:44:58,099 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:44:58,185 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:44:58,490 [INFO]    ðŸš« ML Conviction too low: 0.575 (distance from 0.5: 0.075 < 0.1)
2025-11-13 06:44:58,491 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 8/4)
2025-11-13 06:44:58,491 [INFO]    Partial signals: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence
2025-11-13 06:44:58,491 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=8
2025-11-13 06:44:58,491 [INFO]    ðŸ“ Signal reasons: ðŸ”· Bullish Order Block, ðŸ”€ Bullish RSI Divergence, ðŸ“ˆ Volume Spike
2025-11-13 06:44:58,491 [INFO]    âšª No signal - HOLD
2025-11-13 06:44:58,992 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:44:59,077 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:44:59,401 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:44:59,401 [INFO]    Partial signals: SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:44:59,402 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:44:59,402 [INFO]    ðŸ“ Signal reasons: SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:44:59,402 [INFO]    âšª No signal - HOLD
2025-11-13 06:44:59,903 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:44:59,990 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:45:00,403 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:45:00,403 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:45:00,404 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:45:00,404 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:45:00,404 [INFO]    âšª No signal - HOLD
2025-11-13 06:45:00,905 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:45:00,995 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:45:01,317 [INFO]    ðŸš« ML Conviction too low: 0.599 (distance from 0.5: 0.099 < 0.1)
2025-11-13 06:45:01,318 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:45:01,318 [INFO]    Partial signals: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:45:01,318 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:45:01,318 [INFO]    ðŸ“ Signal reasons: â­ Evening Star, ðŸ“ˆ RSI Overbought
2025-11-13 06:45:01,318 [INFO]    âšª No signal - HOLD
2025-11-13 06:45:01,819 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:45:01,909 [INFO]    Current position: LONG 6.0
2025-11-13 06:45:01,910 [INFO]    Entry: $17.52 | Mark: $17.64
2025-11-13 06:45:01,910 [INFO]    PnL: 0.70% ($0.73)
2025-11-13 06:45:01,910 [INFO]    Age: 1.0h / 36.0h
2025-11-13 06:45:02,411 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:45:02,496 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:45:02,944 [INFO]    ðŸš« ML Conviction too low: 0.480 (distance from 0.5: 0.020 < 0.1)
2025-11-13 06:45:02,945 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 7/4)
2025-11-13 06:45:02,945 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:45:02,945 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-11-13 06:45:02,945 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought, ðŸ”€ Bearish RSI Divergence
2025-11-13 06:45:02,946 [INFO]    âšª No signal - HOLD
2025-11-13 06:45:02,946 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:46:02,978 [INFO] 
============================================================
2025-11-13 06:46:02,978 [INFO] ðŸ”„ LOOP #16 - 2025-11-13 06:46:02
2025-11-13 06:46:02,978 [INFO] ============================================================
2025-11-13 06:46:03,082 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:46:03,083 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:46:03,175 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:46:03,498 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:46:03,499 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:46:03,500 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:46:03,500 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:46:03,500 [INFO]    âšª No signal - HOLD
2025-11-13 06:46:04,001 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:46:04,096 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:46:04,421 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:46:04,421 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:46:04,422 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:46:04,422 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:46:04,422 [INFO]    âšª No signal - HOLD
2025-11-13 06:46:04,923 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:46:05,014 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:46:05,484 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:46:05,484 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:46:05,485 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:46:05,485 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:46:05,485 [INFO]    âšª No signal - HOLD
2025-11-13 06:46:05,986 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:46:06,072 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:46:06,404 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:46:06,404 [INFO]    Partial signals: SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:46:06,405 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:46:06,405 [INFO]    ðŸ“ Signal reasons: SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:46:06,405 [INFO]    âšª No signal - HOLD
2025-11-13 06:46:06,906 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:46:06,993 [INFO]    Current position: LONG 6.0
2025-11-13 06:46:06,993 [INFO]    Entry: $17.52 | Mark: $17.66
2025-11-13 06:46:06,993 [INFO]    PnL: 0.79% ($0.83)
2025-11-13 06:46:06,994 [INFO]    Age: 1.0h / 36.0h
2025-11-13 06:46:07,494 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:46:07,609 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:46:08,009 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:46:08,009 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:46:08,010 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:46:08,010 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:46:08,010 [INFO]    âšª No signal - HOLD
2025-11-13 06:46:08,010 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:47:08,070 [INFO] 
============================================================
2025-11-13 06:47:08,071 [INFO] ðŸ”„ LOOP #17 - 2025-11-13 06:47:08
2025-11-13 06:47:08,071 [INFO] ============================================================
2025-11-13 06:47:08,287 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:47:08,288 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:47:08,565 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:47:08,886 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:47:08,886 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:47:08,887 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:47:08,887 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:47:08,887 [INFO]    âšª No signal - HOLD
2025-11-13 06:47:09,388 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:47:09,477 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:47:09,798 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:47:09,799 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:47:09,799 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:47:09,799 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:47:09,800 [INFO]    âšª No signal - HOLD
2025-11-13 06:47:10,300 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:47:10,386 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:47:10,707 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:47:10,708 [INFO]    Partial signals: LONG(2): ðŸ•¯ï¸ Bullish Engulfing, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:47:10,709 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:47:10,709 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ•¯ï¸ Bullish Engulfing, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:47:10,709 [INFO]    âšª No signal - HOLD
2025-11-13 06:47:11,210 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:47:11,296 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:47:11,625 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:47:11,625 [INFO]    Partial signals: SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:47:11,625 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:47:11,626 [INFO]    ðŸ“ Signal reasons: SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:47:11,626 [INFO]    âšª No signal - HOLD
2025-11-13 06:47:12,126 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:47:12,213 [INFO]    Current position: LONG 6.0
2025-11-13 06:47:12,213 [INFO]    Entry: $17.52 | Mark: $17.65
2025-11-13 06:47:12,213 [INFO]    PnL: 0.76% ($0.80)
2025-11-13 06:47:12,213 [INFO]    Age: 1.0h / 36.0h
2025-11-13 06:47:12,714 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:47:12,800 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:47:13,115 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:47:13,115 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:47:13,116 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:47:13,116 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:47:13,116 [INFO]    âšª No signal - HOLD
2025-11-13 06:47:13,116 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:48:13,176 [INFO] 
============================================================
2025-11-13 06:48:13,177 [INFO] ðŸ”„ LOOP #18 - 2025-11-13 06:48:13
2025-11-13 06:48:13,177 [INFO] ============================================================
2025-11-13 06:48:13,270 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:48:13,270 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:48:13,359 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:48:13,675 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:48:13,675 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:48:13,676 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:48:13,676 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:48:13,676 [INFO]    âšª No signal - HOLD
2025-11-13 06:48:14,177 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:48:14,262 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:48:14,578 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:48:14,578 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:48:14,579 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:48:14,579 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:48:14,579 [INFO]    âšª No signal - HOLD
2025-11-13 06:48:15,080 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:48:15,169 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:48:15,487 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:48:15,487 [INFO]    Partial signals: LONG(2): ðŸ•¯ï¸ Bullish Engulfing, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:48:15,488 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:48:15,488 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ•¯ï¸ Bullish Engulfing, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:48:15,488 [INFO]    âšª No signal - HOLD
2025-11-13 06:48:15,989 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:48:16,074 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:48:16,399 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:48:16,399 [INFO]    Partial signals: SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:48:16,400 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:48:16,400 [INFO]    ðŸ“ Signal reasons: SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:48:16,400 [INFO]    âšª No signal - HOLD
2025-11-13 06:48:16,901 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:48:16,985 [INFO]    Current position: LONG 6.0
2025-11-13 06:48:16,990 [INFO]    Entry: $17.52 | Mark: $17.66
2025-11-13 06:48:16,990 [INFO]    PnL: 0.77% ($0.81)
2025-11-13 06:48:16,990 [INFO]    Age: 1.1h / 36.0h
2025-11-13 06:48:17,491 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:48:17,577 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:48:17,906 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:48:17,906 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:48:17,907 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:48:17,907 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:48:17,907 [INFO]    âšª No signal - HOLD
2025-11-13 06:48:17,907 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:49:17,961 [INFO] 
============================================================
2025-11-13 06:49:17,962 [INFO] ðŸ”„ LOOP #19 - 2025-11-13 06:49:17
2025-11-13 06:49:17,962 [INFO] ============================================================
2025-11-13 06:49:18,050 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:49:18,051 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:49:18,137 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:49:18,459 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:49:18,459 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:49:18,460 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:49:18,460 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:49:18,460 [INFO]    âšª No signal - HOLD
2025-11-13 06:49:18,961 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:49:19,050 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:49:19,362 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:49:19,362 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:49:19,363 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:49:19,363 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:49:19,363 [INFO]    âšª No signal - HOLD
2025-11-13 06:49:19,864 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:49:19,949 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:49:20,267 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:49:20,267 [INFO]    Partial signals: LONG(2): ðŸ•¯ï¸ Bullish Engulfing, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:49:20,268 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:49:20,268 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ•¯ï¸ Bullish Engulfing, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:49:20,268 [INFO]    âšª No signal - HOLD
2025-11-13 06:49:20,769 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:49:20,853 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:49:21,164 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:49:21,164 [INFO]    Partial signals: SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:49:21,164 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:49:21,164 [INFO]    ðŸ“ Signal reasons: SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:49:21,164 [INFO]    âšª No signal - HOLD
2025-11-13 06:49:21,665 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:49:21,757 [INFO]    Current position: LONG 6.0
2025-11-13 06:49:21,757 [INFO]    Entry: $17.52 | Mark: $17.66
2025-11-13 06:49:21,757 [INFO]    PnL: 0.79% ($0.83)
2025-11-13 06:49:21,757 [INFO]    Age: 1.1h / 36.0h
2025-11-13 06:49:22,257 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:49:22,369 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:49:22,699 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:49:22,699 [INFO]    Partial signals: SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:49:22,700 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:49:22,700 [INFO]    ðŸ“ Signal reasons: SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:49:22,700 [INFO]    âšª No signal - HOLD
2025-11-13 06:49:22,700 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:50:22,753 [INFO] 
============================================================
2025-11-13 06:50:22,754 [INFO] ðŸ”„ LOOP #20 - 2025-11-13 06:50:22
2025-11-13 06:50:22,754 [INFO] ============================================================
2025-11-13 06:50:23,291 [INFO] ðŸ’“ Bot alive - Loop #20 - Active positions: 1
2025-11-13 06:50:23,388 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:50:23,389 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:50:23,485 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:50:23,796 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:50:23,796 [INFO]    Partial signals: SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:50:23,797 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:50:23,797 [INFO]    ðŸ“ Signal reasons: SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 06:50:23,797 [INFO]    âšª No signal - HOLD
2025-11-13 06:50:24,298 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:50:24,380 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:50:24,706 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:50:24,706 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:50:24,706 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:50:24,706 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:50:24,707 [INFO]    âšª No signal - HOLD
2025-11-13 06:50:25,207 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:50:25,296 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:50:25,616 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:50:25,617 [INFO]    Partial signals: LONG(2): ðŸ•¯ï¸ Bullish Engulfing, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:50:25,617 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:50:25,618 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ•¯ï¸ Bullish Engulfing, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:50:25,618 [INFO]    âšª No signal - HOLD
2025-11-13 06:50:26,118 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:50:26,207 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:50:26,537 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:50:26,537 [INFO]    Partial signals: SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:50:26,538 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:50:26,538 [INFO]    ðŸ“ Signal reasons: SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:50:26,538 [INFO]    âšª No signal - HOLD
2025-11-13 06:50:27,039 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:50:27,132 [INFO]    Current position: LONG 6.0
2025-11-13 06:50:27,132 [INFO]    Entry: $17.52 | Mark: $17.66
2025-11-13 06:50:27,132 [INFO]    PnL: 0.81% ($0.85)
2025-11-13 06:50:27,132 [INFO]    Age: 1.1h / 36.0h
2025-11-13 06:50:27,633 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:50:27,855 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:50:28,173 [INFO]    ðŸš« HTF trend not bearish (UP), filtering SHORT signal
2025-11-13 06:50:28,173 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 6/4)
2025-11-13 06:50:28,173 [INFO]    Partial signals: ðŸ“Œ Bearish Pin Bar, ðŸ’§ Bearish Liquidity Sweep
2025-11-13 06:50:28,174 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=6
2025-11-13 06:50:28,174 [INFO]    ðŸ“ Signal reasons: ðŸ“Œ Bearish Pin Bar, ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:50:28,175 [INFO]    âšª No signal - HOLD
2025-11-13 06:50:28,693 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:51:28,754 [INFO] 
============================================================
2025-11-13 06:51:28,754 [INFO] ðŸ”„ LOOP #21 - 2025-11-13 06:51:28
2025-11-13 06:51:28,754 [INFO] ============================================================
2025-11-13 06:51:28,845 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:51:28,846 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:51:28,930 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:51:29,240 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:51:29,240 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:51:29,241 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:51:29,241 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:51:29,241 [INFO]    âšª No signal - HOLD
2025-11-13 06:51:29,742 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:51:29,833 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:51:30,145 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:51:30,145 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:51:30,146 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:51:30,146 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:51:30,147 [INFO]    âšª No signal - HOLD
2025-11-13 06:51:30,647 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:51:30,734 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:51:31,060 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:51:31,061 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:51:31,061 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:51:31,062 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:51:31,062 [INFO]    âšª No signal - HOLD
2025-11-13 06:51:31,562 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:51:31,649 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:51:31,962 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:51:31,962 [INFO]    Partial signals: SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:51:31,962 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:51:31,963 [INFO]    ðŸ“ Signal reasons: SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:51:31,963 [INFO]    âšª No signal - HOLD
2025-11-13 06:51:32,463 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:51:32,551 [INFO]    Current position: LONG 6.0
2025-11-13 06:51:32,552 [INFO]    Entry: $17.52 | Mark: $17.63
2025-11-13 06:51:32,552 [INFO]    PnL: 0.63% ($0.67)
2025-11-13 06:51:32,552 [INFO]    Age: 1.1h / 36.0h
2025-11-13 06:51:33,053 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:51:33,138 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:51:33,495 [INFO]    ðŸš« HTF trend not bearish (UP), filtering SHORT signal
2025-11-13 06:51:33,495 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:51:33,495 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:51:33,496 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:51:33,496 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:51:33,496 [INFO]    âšª No signal - HOLD
2025-11-13 06:51:33,496 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:52:33,547 [INFO] 
============================================================
2025-11-13 06:52:33,547 [INFO] ðŸ”„ LOOP #22 - 2025-11-13 06:52:33
2025-11-13 06:52:33,547 [INFO] ============================================================
2025-11-13 06:52:33,637 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:52:33,637 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:52:33,721 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:52:34,037 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:52:34,037 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:52:34,038 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:52:34,038 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:52:34,038 [INFO]    âšª No signal - HOLD
2025-11-13 06:52:34,543 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:52:34,633 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:52:34,949 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:52:34,949 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:52:34,949 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:52:34,949 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:52:34,950 [INFO]    âšª No signal - HOLD
2025-11-13 06:52:35,450 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:52:35,541 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:52:35,867 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:52:35,868 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:52:35,869 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:52:35,869 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:52:35,869 [INFO]    âšª No signal - HOLD
2025-11-13 06:52:36,370 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:52:36,461 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:52:36,791 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:52:36,791 [INFO]    Partial signals: SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:52:36,791 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:52:36,791 [INFO]    ðŸ“ Signal reasons: SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:52:36,792 [INFO]    âšª No signal - HOLD
2025-11-13 06:52:37,292 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:52:37,383 [INFO]    Current position: LONG 6.0
2025-11-13 06:52:37,384 [INFO]    Entry: $17.52 | Mark: $17.63
2025-11-13 06:52:37,384 [INFO]    PnL: 0.64% ($0.67)
2025-11-13 06:52:37,384 [INFO]    Age: 1.1h / 36.0h
2025-11-13 06:52:37,885 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:52:37,973 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:52:38,319 [INFO]    ðŸš« HTF trend not bearish (UP), filtering SHORT signal
2025-11-13 06:52:38,320 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:52:38,320 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:52:38,320 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:52:38,320 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:52:38,320 [INFO]    âšª No signal - HOLD
2025-11-13 06:52:38,320 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:53:38,377 [INFO] 
============================================================
2025-11-13 06:53:38,378 [INFO] ðŸ”„ LOOP #23 - 2025-11-13 06:53:38
2025-11-13 06:53:38,378 [INFO] ============================================================
2025-11-13 06:53:38,466 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:53:38,466 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:53:38,551 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:53:38,888 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:53:38,888 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:53:38,889 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:53:38,894 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:53:38,894 [INFO]    âšª No signal - HOLD
2025-11-13 06:53:39,395 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:53:39,488 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:53:39,819 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:53:39,819 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:53:39,820 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:53:39,820 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:53:39,820 [INFO]    âšª No signal - HOLD
2025-11-13 06:53:40,321 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:53:40,408 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:53:40,736 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:53:40,737 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:53:40,737 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:53:40,738 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:53:40,738 [INFO]    âšª No signal - HOLD
2025-11-13 06:53:41,239 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:53:41,326 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:53:41,630 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:53:41,630 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:53:41,631 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:53:41,631 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:53:41,631 [INFO]    âšª No signal - HOLD
2025-11-13 06:53:42,131 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:53:42,219 [INFO]    Current position: LONG 6.0
2025-11-13 06:53:42,219 [INFO]    Entry: $17.52 | Mark: $17.65
2025-11-13 06:53:42,219 [INFO]    PnL: 0.74% ($0.78)
2025-11-13 06:53:42,219 [INFO]    Age: 1.1h / 36.0h
2025-11-13 06:53:42,720 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:53:42,807 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:53:43,136 [INFO]    ðŸš« HTF trend not bearish (UP), filtering SHORT signal
2025-11-13 06:53:43,136 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:53:43,136 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:53:43,137 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:53:43,137 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:53:43,137 [INFO]    âšª No signal - HOLD
2025-11-13 06:53:43,137 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:54:43,181 [INFO] 
============================================================
2025-11-13 06:54:43,181 [INFO] ðŸ”„ LOOP #24 - 2025-11-13 06:54:43
2025-11-13 06:54:43,181 [INFO] ============================================================
2025-11-13 06:54:43,269 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:54:43,269 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:54:43,353 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:54:43,667 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:54:43,667 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:54:43,668 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:54:43,668 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:54:43,668 [INFO]    âšª No signal - HOLD
2025-11-13 06:54:44,169 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:54:44,256 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:54:44,573 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:54:44,574 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:54:44,574 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:54:44,575 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:54:44,575 [INFO]    âšª No signal - HOLD
2025-11-13 06:54:45,076 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:54:45,161 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:54:45,487 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:54:45,487 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:54:45,488 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:54:45,488 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:54:45,488 [INFO]    âšª No signal - HOLD
2025-11-13 06:54:45,989 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:54:46,079 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:54:46,418 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:54:46,418 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:54:46,419 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:54:46,419 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:54:46,419 [INFO]    âšª No signal - HOLD
2025-11-13 06:54:46,920 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:54:47,010 [INFO]    Current position: LONG 6.0
2025-11-13 06:54:47,010 [INFO]    Entry: $17.52 | Mark: $17.65
2025-11-13 06:54:47,010 [INFO]    PnL: 0.71% ($0.75)
2025-11-13 06:54:47,010 [INFO]    Age: 1.2h / 36.0h
2025-11-13 06:54:47,511 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:54:47,597 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:54:47,923 [INFO]    ðŸš« HTF trend not bearish (UP), filtering SHORT signal
2025-11-13 06:54:47,923 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:54:47,923 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:54:47,924 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:54:47,924 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:54:47,924 [INFO]    âšª No signal - HOLD
2025-11-13 06:54:47,924 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:55:47,942 [INFO] 
============================================================
2025-11-13 06:55:47,943 [INFO] ðŸ”„ LOOP #25 - 2025-11-13 06:55:47
2025-11-13 06:55:47,943 [INFO] ============================================================
2025-11-13 06:55:48,471 [INFO] ðŸ’“ Bot alive - Loop #25 - Active positions: 1
2025-11-13 06:55:48,557 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:55:48,558 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:55:48,646 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:55:48,957 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:55:48,957 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:55:48,958 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:55:48,958 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:55:48,958 [INFO]    âšª No signal - HOLD
2025-11-13 06:55:49,459 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:55:49,546 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:55:49,855 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:55:49,855 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:55:49,856 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:55:49,856 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:55:49,856 [INFO]    âšª No signal - HOLD
2025-11-13 06:55:50,357 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:55:50,446 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:55:50,894 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:55:50,894 [INFO]    Partial signals: LONG(2): ðŸ•¯ï¸ Bullish Engulfing, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:55:50,895 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:55:50,895 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ•¯ï¸ Bullish Engulfing, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:55:50,895 [INFO]    âšª No signal - HOLD
2025-11-13 06:55:51,396 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:55:51,486 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:55:51,801 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:55:51,802 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:55:51,802 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:55:51,803 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:55:51,803 [INFO]    âšª No signal - HOLD
2025-11-13 06:55:52,304 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:55:52,652 [INFO]    Current position: LONG 6.0
2025-11-13 06:55:52,652 [INFO]    Entry: $17.52 | Mark: $17.66
2025-11-13 06:55:52,653 [INFO]    PnL: 0.77% ($0.81)
2025-11-13 06:55:52,653 [INFO]    Age: 1.2h / 36.0h
2025-11-13 06:55:53,153 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:55:53,241 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:55:53,728 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:55:53,728 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:55:53,729 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:55:53,729 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:55:53,729 [INFO]    âšª No signal - HOLD
2025-11-13 06:55:53,729 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:56:53,789 [INFO] 
============================================================
2025-11-13 06:56:53,790 [INFO] ðŸ”„ LOOP #26 - 2025-11-13 06:56:53
2025-11-13 06:56:53,790 [INFO] ============================================================
2025-11-13 06:56:53,876 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:56:53,876 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:56:53,963 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:56:54,284 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:56:54,285 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:56:54,285 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:56:54,285 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:56:54,286 [INFO]    âšª No signal - HOLD
2025-11-13 06:56:54,786 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:56:54,873 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:56:55,187 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:56:55,187 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:56:55,188 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:56:55,188 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:56:55,188 [INFO]    âšª No signal - HOLD
2025-11-13 06:56:55,689 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:56:55,782 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:56:56,120 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:56:56,120 [INFO]    Partial signals: LONG(2): ðŸ•¯ï¸ Bullish Engulfing, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:56:56,121 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:56:56,121 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ•¯ï¸ Bullish Engulfing, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:56:56,121 [INFO]    âšª No signal - HOLD
2025-11-13 06:56:56,622 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:56:56,706 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:56:57,019 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:56:57,019 [INFO]    Partial signals: LONG(2): ðŸ“Œ Bullish Pin Bar, SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:56:57,024 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:56:57,025 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ“Œ Bullish Pin Bar, SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:56:57,025 [INFO]    âšª No signal - HOLD
2025-11-13 06:56:57,525 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:56:57,611 [INFO]    Current position: LONG 6.0
2025-11-13 06:56:57,611 [INFO]    Entry: $17.52 | Mark: $17.66
2025-11-13 06:56:57,611 [INFO]    PnL: 0.76% ($0.80)
2025-11-13 06:56:57,611 [INFO]    Age: 1.2h / 36.0h
2025-11-13 06:56:58,112 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:56:58,198 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:56:58,547 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:56:58,547 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:56:58,548 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:56:58,548 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:56:58,548 [INFO]    âšª No signal - HOLD
2025-11-13 06:56:58,548 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:57:58,562 [INFO] 
============================================================
2025-11-13 06:57:58,562 [INFO] ðŸ”„ LOOP #27 - 2025-11-13 06:57:58
2025-11-13 06:57:58,562 [INFO] ============================================================
2025-11-13 06:57:58,650 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:57:58,651 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:57:58,735 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:57:59,054 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:57:59,054 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:57:59,055 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:57:59,055 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:57:59,055 [INFO]    âšª No signal - HOLD
2025-11-13 06:57:59,556 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:57:59,643 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:57:59,958 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:57:59,958 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:57:59,959 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:57:59,959 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:57:59,959 [INFO]    âšª No signal - HOLD
2025-11-13 06:58:00,460 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:58:00,546 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:58:00,868 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:58:00,869 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:58:00,869 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:58:00,869 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:58:00,869 [INFO]    âšª No signal - HOLD
2025-11-13 06:58:01,370 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:58:01,455 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:58:01,763 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:58:01,763 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:58:01,764 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:58:01,764 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:58:01,764 [INFO]    âšª No signal - HOLD
2025-11-13 06:58:02,265 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:58:02,355 [INFO]    Current position: LONG 6.0
2025-11-13 06:58:02,355 [INFO]    Entry: $17.52 | Mark: $17.63
2025-11-13 06:58:02,355 [INFO]    PnL: 0.64% ($0.67)
2025-11-13 06:58:02,355 [INFO]    Age: 1.2h / 36.0h
2025-11-13 06:58:02,856 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:58:02,942 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:58:03,260 [INFO]    ðŸš« HTF trend not bearish (UP), filtering SHORT signal
2025-11-13 06:58:03,260 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:58:03,260 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:58:03,261 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:58:03,261 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:58:03,261 [INFO]    âšª No signal - HOLD
2025-11-13 06:58:03,261 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 06:59:03,302 [INFO] 
============================================================
2025-11-13 06:59:03,303 [INFO] ðŸ”„ LOOP #28 - 2025-11-13 06:59:03
2025-11-13 06:59:03,303 [INFO] ============================================================
2025-11-13 06:59:03,389 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 06:59:03,390 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 06:59:03,479 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 06:59:03,804 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:59:03,804 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:59:03,805 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:59:03,805 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:59:03,805 [INFO]    âšª No signal - HOLD
2025-11-13 06:59:04,306 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 06:59:04,393 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 06:59:04,708 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 06:59:04,708 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:59:04,709 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 06:59:04,709 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:59:04,709 [INFO]    âšª No signal - HOLD
2025-11-13 06:59:05,210 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 06:59:05,296 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 06:59:05,617 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 2/4)
2025-11-13 06:59:05,617 [INFO]    Partial signals: LONG(2): ðŸ•¯ï¸ Bullish Engulfing, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:59:05,618 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 06:59:05,618 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ•¯ï¸ Bullish Engulfing, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 06:59:05,618 [INFO]    âšª No signal - HOLD
2025-11-13 06:59:06,119 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 06:59:06,207 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 06:59:06,535 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 06:59:06,536 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:59:06,536 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 06:59:06,536 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(2): ðŸ“Š Bearish FVG
2025-11-13 06:59:06,536 [INFO]    âšª No signal - HOLD
2025-11-13 06:59:07,037 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 06:59:07,126 [INFO]    Current position: LONG 6.0
2025-11-13 06:59:07,126 [INFO]    Entry: $17.52 | Mark: $17.61
2025-11-13 06:59:07,126 [INFO]    PnL: 0.51% ($0.53)
2025-11-13 06:59:07,126 [INFO]    Age: 1.2h / 36.0h
2025-11-13 06:59:07,627 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 06:59:07,716 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 06:59:08,042 [INFO]    ðŸš« HTF trend not bearish (UP), filtering SHORT signal
2025-11-13 06:59:08,043 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 4/4)
2025-11-13 06:59:08,043 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:59:08,043 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 06:59:08,044 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 06:59:08,044 [INFO]    âšª No signal - HOLD
2025-11-13 06:59:08,044 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 07:00:08,101 [INFO] 
============================================================
2025-11-13 07:00:08,102 [INFO] ðŸ”„ LOOP #29 - 2025-11-13 07:00:08
2025-11-13 07:00:08,102 [INFO] ============================================================
2025-11-13 07:00:08,190 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 07:00:08,191 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 07:00:08,282 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 07:00:08,732 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 07:00:08,733 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:00:08,738 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 07:00:08,738 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:00:08,738 [INFO]    âšª No signal - HOLD
2025-11-13 07:00:09,239 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 07:00:09,326 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 07:00:09,802 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 07:00:09,803 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:00:09,803 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 07:00:09,803 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:00:09,803 [INFO]    âšª No signal - HOLD
2025-11-13 07:00:10,305 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 07:00:10,396 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 07:00:10,865 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 1/4)
2025-11-13 07:00:10,866 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:00:10,866 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 07:00:10,866 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:00:10,866 [INFO]    âšª No signal - HOLD
2025-11-13 07:00:11,367 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 07:00:11,456 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 07:00:11,917 [INFO]    ðŸš« ML Conviction too low: 0.578 (distance from 0.5: 0.078 < 0.1)
2025-11-13 07:00:11,930 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 5/4)
2025-11-13 07:00:11,930 [INFO]    Partial signals: ðŸ”€ Bullish RSI Divergence, ðŸ“ˆ Volume Spike
2025-11-13 07:00:11,930 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=5
2025-11-13 07:00:11,931 [INFO]    ðŸ“ Signal reasons: ðŸ”€ Bullish RSI Divergence, ðŸ“ˆ Volume Spike
2025-11-13 07:00:11,931 [INFO]    âšª No signal - HOLD
2025-11-13 07:00:12,434 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 07:00:12,520 [INFO]    Current position: LONG 6.0
2025-11-13 07:00:12,521 [INFO]    Entry: $17.52 | Mark: $17.59
2025-11-13 07:00:12,521 [INFO]    PnL: 0.38% ($0.40)
2025-11-13 07:00:12,521 [INFO]    Age: 1.2h / 36.0h
2025-11-13 07:00:13,024 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 07:00:13,111 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 07:00:13,576 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 0/4)
2025-11-13 07:00:13,594 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 07:00:13,595 [INFO]    âšª No signal - HOLD
2025-11-13 07:00:13,595 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 07:01:13,650 [INFO] 
============================================================
2025-11-13 07:01:13,650 [INFO] ðŸ”„ LOOP #30 - 2025-11-13 07:01:13
2025-11-13 07:01:13,650 [INFO] ============================================================
2025-11-13 07:01:14,308 [INFO] ðŸ’“ Bot alive - Loop #30 - Active positions: 1
2025-11-13 07:01:14,395 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 07:01:14,395 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 07:01:14,485 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 07:01:14,810 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 07:01:14,810 [INFO]    Partial signals: SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 07:01:14,811 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 07:01:14,811 [INFO]    ðŸ“ Signal reasons: SHORT(2): ðŸ“Œ Bearish Pin Bar
2025-11-13 07:01:14,811 [INFO]    âšª No signal - HOLD
2025-11-13 07:01:15,312 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 07:01:15,398 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 07:01:15,720 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 07:01:15,720 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:01:15,721 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 07:01:15,721 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:01:15,721 [INFO]    âšª No signal - HOLD
2025-11-13 07:01:16,222 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 07:01:16,306 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 07:01:16,654 [INFO]    ðŸš« ML Conviction too low: 0.578 (distance from 0.5: 0.078 < 0.1)
2025-11-13 07:01:16,655 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 4/4)
2025-11-13 07:01:16,655 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:01:16,656 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 07:01:16,656 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:01:16,656 [INFO]    âšª No signal - HOLD
2025-11-13 07:01:17,157 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 07:01:17,243 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 07:01:17,557 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 3/4)
2025-11-13 07:01:17,557 [INFO]    Partial signals: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(3): ðŸ’§ Bearish Liquidity Sweep
2025-11-13 07:01:17,558 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 07:01:17,558 [INFO]    ðŸ“ Signal reasons: LONG(3): ðŸ”€ Bullish RSI Divergence, SHORT(3): ðŸ’§ Bearish Liquidity Sweep
2025-11-13 07:01:17,558 [INFO]    âšª No signal - HOLD
2025-11-13 07:01:18,059 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 07:01:18,145 [INFO]    Current position: LONG 6.0
2025-11-13 07:01:18,145 [INFO]    Entry: $17.52 | Mark: $17.59
2025-11-13 07:01:18,146 [INFO]    PnL: 0.39% ($0.41)
2025-11-13 07:01:18,146 [INFO]    Age: 1.3h / 36.0h
2025-11-13 07:01:18,646 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 07:01:18,734 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 07:01:19,066 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 0/4)
2025-11-13 07:01:19,067 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 07:01:19,067 [INFO]    âšª No signal - HOLD
2025-11-13 07:01:19,595 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 07:02:19,618 [INFO] 
============================================================
2025-11-13 07:02:19,618 [INFO] ðŸ”„ LOOP #31 - 2025-11-13 07:02:19
2025-11-13 07:02:19,618 [INFO] ============================================================
2025-11-13 07:02:19,706 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 07:02:19,706 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 07:02:19,791 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 07:02:20,113 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 07:02:20,113 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:02:20,114 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 07:02:20,114 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:02:20,115 [INFO]    âšª No signal - HOLD
2025-11-13 07:02:20,615 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 07:02:20,705 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 07:02:21,035 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 07:02:21,036 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:02:21,036 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 07:02:21,036 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:02:21,036 [INFO]    âšª No signal - HOLD
2025-11-13 07:02:21,537 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 07:02:21,624 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 07:02:22,087 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 07:02:22,088 [INFO]    Partial signals: LONG(3): â­ Morning Star, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:02:22,088 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 07:02:22,089 [INFO]    ðŸ“ Signal reasons: LONG(3): â­ Morning Star, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:02:22,089 [INFO]    âšª No signal - HOLD
2025-11-13 07:02:22,589 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 07:02:22,677 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 07:02:22,997 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 0/4)
2025-11-13 07:02:22,997 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 07:02:22,998 [INFO]    âšª No signal - HOLD
2025-11-13 07:02:23,498 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 07:02:23,584 [INFO]    Current position: LONG 6.0
2025-11-13 07:02:23,585 [INFO]    Entry: $17.52 | Mark: $17.61
2025-11-13 07:02:23,585 [INFO]    PnL: 0.50% ($0.53)
2025-11-13 07:02:23,585 [INFO]    Age: 1.3h / 36.0h
2025-11-13 07:02:24,086 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 07:02:24,171 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 07:02:24,496 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 0/4)
2025-11-13 07:02:24,497 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 07:02:24,497 [INFO]    âšª No signal - HOLD
2025-11-13 07:02:24,497 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 07:03:24,553 [INFO] 
============================================================
2025-11-13 07:03:24,554 [INFO] ðŸ”„ LOOP #32 - 2025-11-13 07:03:24
2025-11-13 07:03:24,554 [INFO] ============================================================
2025-11-13 07:03:24,657 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 07:03:24,657 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 07:03:24,739 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 07:03:25,148 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 07:03:25,149 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:03:25,149 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 07:03:25,154 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:03:25,154 [INFO]    âšª No signal - HOLD
2025-11-13 07:03:25,655 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 07:03:25,744 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 07:03:26,050 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 07:03:26,050 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:03:26,053 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 07:03:26,053 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:03:26,053 [INFO]    âšª No signal - HOLD
2025-11-13 07:03:26,554 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 07:03:26,639 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 07:03:27,089 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 3/4)
2025-11-13 07:03:27,089 [INFO]    Partial signals: LONG(3): â­ Morning Star, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:03:27,089 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 07:03:27,090 [INFO]    ðŸ“ Signal reasons: LONG(3): â­ Morning Star, SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:03:27,090 [INFO]    âšª No signal - HOLD
2025-11-13 07:03:27,590 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 07:03:27,675 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 07:03:27,992 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 07:03:27,992 [INFO]    Partial signals: LONG(2): ðŸ•¯ï¸ Bullish Engulfing
2025-11-13 07:03:27,993 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 07:03:27,993 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ•¯ï¸ Bullish Engulfing
2025-11-13 07:03:27,993 [INFO]    âšª No signal - HOLD
2025-11-13 07:03:28,494 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 07:03:28,581 [INFO]    Current position: LONG 6.0
2025-11-13 07:03:28,581 [INFO]    Entry: $17.52 | Mark: $17.61
2025-11-13 07:03:28,581 [INFO]    PnL: 0.50% ($0.53)
2025-11-13 07:03:28,581 [INFO]    Age: 1.3h / 36.0h
2025-11-13 07:03:29,082 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 07:03:29,167 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 07:03:29,509 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 0/4)
2025-11-13 07:03:29,510 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 07:03:29,510 [INFO]    âšª No signal - HOLD
2025-11-13 07:03:29,510 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 07:03:33,569 [INFO] 
ðŸ›‘ Shutdown signal received...
2025-11-13 07:04:29,522 [INFO] 
============================================================
2025-11-13 07:04:29,522 [INFO] ðŸ›‘ SHUTTING DOWN BOT
2025-11-13 07:04:29,522 [INFO] ============================================================
2025-11-13 07:04:29,522 [INFO] ðŸ“Š <b>DAILY STATS</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
Trades: 0
Volume: $0.00M
PnL: 0.00%

<b>Overall</b>
Total Trades: 0
Win Rate: 0.0%
W/L: 0/0
2025-11-13 07:04:30,287 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 07:04:30,289 [INFO] ðŸ‘‹ Bot stopped!
2025-11-13 07:04:30,718 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
âœ… Using fixed position size: $10.0 USDT per trade
âœ… Config validation passed!
2025-11-13 07:04:34,233 [INFO] âœ… Telegram bot initialized
2025-11-13 07:04:41,422 [INFO] ============================================================
2025-11-13 07:04:41,424 [INFO] ðŸš€ ASTERDEX PERP FARM BOT - INITIALIZING
2025-11-13 07:04:41,424 [INFO] ============================================================
2025-11-13 07:04:41,915 [INFO] ðŸ”Œ AsterDEX Client initialized (MAINNET)
2025-11-13 07:04:41,915 [INFO]    URL: https://fapi.asterdex.com/fapi
2025-11-13 07:04:41,916 [INFO] ðŸ“‚ Loaded 1 position timestamps
2025-11-13 07:04:41,916 [INFO] ðŸ“ˆ Trailing Stop enabled: Activation=1.0%, Trail=0.3%
2025-11-13 07:04:41,916 [INFO] ðŸŽ­ Loading Ensemble models...
2025-11-13 07:04:41,929 [INFO] ðŸ§  LSTM Model initialized on cpu
2025-11-13 07:04:41,929 [INFO]    Input: 14, Hidden: 128, Layers: 3, Dropout: 0.3
2025-11-13 07:04:41,929 [INFO] ðŸŽ­ Ensemble initialized with 2 models
2025-11-13 07:04:41,929 [INFO]    Models: ['lstm', 'xgboost']
2025-11-13 07:04:41,930 [INFO]    Weights: [0.3 0.7]
2025-11-13 07:04:41,952 [INFO] âœ… Model loaded from models/lstm_model.pt
2025-11-13 07:04:41,952 [INFO] âœ… LSTM loaded
2025-11-13 07:04:42,025 [INFO] âœ… XGBoost model loaded from models/xgboost_model.json
2025-11-13 07:04:42,026 [INFO] âœ… XGBoost loaded
2025-11-13 07:04:42,026 [INFO] âœ… Ensemble loaded: 2/2 models
2025-11-13 07:04:42,026 [INFO] ðŸŽ­ Using Ensemble predictor: ['lstm', 'xgboost']
2025-11-13 07:04:42,026 [INFO]    Weights: [0.3, 0.7]
2025-11-13 07:04:42,026 [INFO] ðŸŽ¯ Advanced Entry System enabled (min score: 4)
2025-11-13 07:04:42,026 [INFO] ðŸš« Signal Cooldown enabled: 60 minutes
2025-11-13 07:04:42,026 [INFO] âœ… Bot initialized successfully!
2025-11-13 07:04:42,026 [INFO]    Symbols: ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'LTCUSDT', 'AVAXUSDT', 'XRPUSDT']
2025-11-13 07:04:42,026 [INFO]    Leverage: 10x
2025-11-13 07:04:42,026 [INFO]    Position Size: 20.0%
2025-11-13 07:04:42,026 [INFO]    TP/SL: 1.00% / Disabled
2025-11-13 07:04:42,027 [INFO]    Position Timeout: 36.0h
2025-11-13 07:04:42,027 [INFO] ============================================================
2025-11-13 07:04:42,027 [INFO] ðŸ BOT STARTED!
2025-11-13 07:04:42,789 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 07:04:42,964 [INFO] ðŸ“Š Daily start balance: $18.75
2025-11-13 07:04:42,964 [INFO] ðŸ’° Starting balance: $18.75
2025-11-13 07:04:43,398 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 07:04:43,400 [INFO] 
============================================================
2025-11-13 07:04:43,400 [INFO] ðŸ”„ LOOP #1 - 2025-11-13 07:04:43
2025-11-13 07:04:43,400 [INFO] ============================================================
2025-11-13 07:04:43,486 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 07:04:43,486 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 07:04:43,580 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 07:04:43,967 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 07:04:43,968 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:04:43,968 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 07:04:43,968 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:04:43,968 [INFO]    âšª No signal - HOLD
2025-11-13 07:04:44,469 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 07:04:44,560 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 07:04:44,925 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 3/4)
2025-11-13 07:04:44,925 [INFO]    Partial signals: SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 07:04:44,926 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=3
2025-11-13 07:04:44,926 [INFO]    ðŸ“ Signal reasons: SHORT(3): ðŸ“Œ Bearish Pin Bar, SHORT(3): ðŸ“ˆ RSI Overbought
2025-11-13 07:04:44,926 [INFO]    âšª No signal - HOLD
2025-11-13 07:04:45,427 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 07:04:45,518 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 07:04:45,977 [INFO]    ðŸš« ML Conviction too low: 0.543 (distance from 0.5: 0.043 < 0.1)
2025-11-13 07:04:45,978 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 4/4)
2025-11-13 07:04:45,978 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:04:45,978 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 07:04:45,978 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:04:45,978 [INFO]    âšª No signal - HOLD
2025-11-13 07:04:46,479 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 07:04:46,563 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 07:04:46,883 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 07:04:46,883 [INFO]    Partial signals: LONG(2): ðŸ•¯ï¸ Bullish Engulfing
2025-11-13 07:04:46,883 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 07:04:46,884 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ•¯ï¸ Bullish Engulfing
2025-11-13 07:04:46,884 [INFO]    âšª No signal - HOLD
2025-11-13 07:04:47,385 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 07:04:47,471 [INFO]    Current position: LONG 6.0
2025-11-13 07:04:47,472 [INFO]    Entry: $17.52 | Mark: $17.60
2025-11-13 07:04:47,472 [INFO]    PnL: 0.44% ($0.46)
2025-11-13 07:04:47,472 [INFO]    Age: 1.3h / 36.0h
2025-11-13 07:04:47,973 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 07:04:48,058 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 07:04:48,368 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 0/4)
2025-11-13 07:04:48,368 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 07:04:48,368 [INFO]    âšª No signal - HOLD
2025-11-13 07:04:48,369 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 07:05:48,426 [INFO] 
============================================================
2025-11-13 07:05:48,427 [INFO] ðŸ”„ LOOP #2 - 2025-11-13 07:05:48
2025-11-13 07:05:48,427 [INFO] ============================================================
2025-11-13 07:05:48,514 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 07:05:48,514 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 07:05:48,600 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 07:05:48,922 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 07:05:48,922 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:05:48,923 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 07:05:48,923 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:05:48,923 [INFO]    âšª No signal - HOLD
2025-11-13 07:05:49,424 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 07:05:49,511 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 07:05:49,827 [INFO]    ðŸš« ML Conviction too low: 0.544 (distance from 0.5: 0.044 < 0.1)
2025-11-13 07:05:49,827 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 9/4)
2025-11-13 07:05:49,827 [INFO]    Partial signals: ðŸ“Œ Bearish Pin Bar, â­ Evening Star
2025-11-13 07:05:49,828 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=9
2025-11-13 07:05:49,828 [INFO]    ðŸ“ Signal reasons: ðŸ“Œ Bearish Pin Bar, â­ Evening Star, ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:05:49,828 [INFO]    âšª No signal - HOLD
2025-11-13 07:05:50,329 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 07:05:50,419 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 07:05:50,753 [INFO]    ðŸš« ML Conviction too low: 0.568 (distance from 0.5: 0.068 < 0.1)
2025-11-13 07:05:50,753 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 4/4)
2025-11-13 07:05:50,753 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:05:50,754 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 07:05:50,754 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:05:50,754 [INFO]    âšª No signal - HOLD
2025-11-13 07:05:51,255 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 07:05:51,342 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 07:05:51,677 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 07:05:51,677 [INFO]    Partial signals: LONG(2): ðŸ•¯ï¸ Bullish Engulfing
2025-11-13 07:05:51,678 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 07:05:51,678 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ•¯ï¸ Bullish Engulfing
2025-11-13 07:05:51,678 [INFO]    âšª No signal - HOLD
2025-11-13 07:05:52,179 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 07:05:52,266 [INFO]    Current position: LONG 6.0
2025-11-13 07:05:52,266 [INFO]    Entry: $17.52 | Mark: $17.60
2025-11-13 07:05:52,266 [INFO]    PnL: 0.42% ($0.44)
2025-11-13 07:05:52,266 [INFO]    Age: 1.3h / 36.0h
2025-11-13 07:05:52,767 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 07:05:52,859 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 07:05:53,178 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 0/4)
2025-11-13 07:05:53,179 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 07:05:53,179 [INFO]    âšª No signal - HOLD
2025-11-13 07:05:53,179 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 07:06:53,239 [INFO] 
============================================================
2025-11-13 07:06:53,239 [INFO] ðŸ”„ LOOP #3 - 2025-11-13 07:06:53
2025-11-13 07:06:53,239 [INFO] ============================================================
2025-11-13 07:06:53,330 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 07:06:53,330 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 07:06:53,415 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 07:06:53,729 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 07:06:53,729 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:06:53,730 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 07:06:53,730 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:06:53,730 [INFO]    âšª No signal - HOLD
2025-11-13 07:06:54,231 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 07:06:54,315 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 07:06:54,623 [INFO]    ðŸš« ML Conviction too low: 0.565 (distance from 0.5: 0.065 < 0.1)
2025-11-13 07:06:54,624 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 7/4)
2025-11-13 07:06:54,624 [INFO]    Partial signals: â­ Evening Star, ðŸ’§ Bearish Liquidity Sweep
2025-11-13 07:06:54,624 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-11-13 07:06:54,624 [INFO]    ðŸ“ Signal reasons: â­ Evening Star, ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:06:54,624 [INFO]    âšª No signal - HOLD
2025-11-13 07:06:55,125 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 07:06:55,211 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 07:06:55,520 [INFO]    ðŸš« ML Conviction too low: 0.569 (distance from 0.5: 0.069 < 0.1)
2025-11-13 07:06:55,521 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 4/4)
2025-11-13 07:06:55,521 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:06:55,521 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 07:06:55,522 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:06:55,522 [INFO]    âšª No signal - HOLD
2025-11-13 07:06:56,022 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 07:06:56,108 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 07:06:56,417 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 0/4)
2025-11-13 07:06:56,417 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 07:06:56,418 [INFO]    âšª No signal - HOLD
2025-11-13 07:06:56,918 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 07:06:57,008 [INFO]    Current position: LONG 6.0
2025-11-13 07:06:57,008 [INFO]    Entry: $17.52 | Mark: $17.60
2025-11-13 07:06:57,008 [INFO]    PnL: 0.45% ($0.47)
2025-11-13 07:06:57,008 [INFO]    Age: 1.4h / 36.0h
2025-11-13 07:06:57,509 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 07:06:57,596 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 07:06:57,916 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 0/4)
2025-11-13 07:06:57,916 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 07:06:57,917 [INFO]    âšª No signal - HOLD
2025-11-13 07:06:57,917 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 07:07:57,973 [INFO] 
============================================================
2025-11-13 07:07:57,974 [INFO] ðŸ”„ LOOP #4 - 2025-11-13 07:07:57
2025-11-13 07:07:57,974 [INFO] ============================================================
2025-11-13 07:07:58,068 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 07:07:58,068 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 07:07:58,164 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 07:07:58,474 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 07:07:58,474 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:07:58,475 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 07:07:58,475 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:07:58,475 [INFO]    âšª No signal - HOLD
2025-11-13 07:07:58,976 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 07:07:59,060 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 07:07:59,369 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 1/4)
2025-11-13 07:07:59,369 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:07:59,370 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 07:07:59,370 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:07:59,370 [INFO]    âšª No signal - HOLD
2025-11-13 07:07:59,871 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 07:07:59,958 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 07:08:00,270 [INFO]    ðŸš« ML Conviction too low: 0.568 (distance from 0.5: 0.068 < 0.1)
2025-11-13 07:08:00,270 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 4/4)
2025-11-13 07:08:00,270 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:08:00,271 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 07:08:00,271 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:08:00,271 [INFO]    âšª No signal - HOLD
2025-11-13 07:08:00,771 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 07:08:00,862 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 07:08:01,181 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 0/4)
2025-11-13 07:08:01,182 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 07:08:01,182 [INFO]    âšª No signal - HOLD
2025-11-13 07:08:01,683 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 07:08:01,768 [INFO]    Current position: LONG 6.0
2025-11-13 07:08:01,768 [INFO]    Entry: $17.52 | Mark: $17.61
2025-11-13 07:08:01,768 [INFO]    PnL: 0.50% ($0.53)
2025-11-13 07:08:01,768 [INFO]    Age: 1.4h / 36.0h
2025-11-13 07:08:02,269 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 07:08:02,360 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 07:08:02,815 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 0/4)
2025-11-13 07:08:02,816 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 07:08:02,816 [INFO]    âšª No signal - HOLD
2025-11-13 07:08:02,816 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 07:09:02,841 [INFO] 
============================================================
2025-11-13 07:09:02,842 [INFO] ðŸ”„ LOOP #5 - 2025-11-13 07:09:02
2025-11-13 07:09:02,842 [INFO] ============================================================
2025-11-13 07:09:03,373 [INFO] ðŸ’“ Bot alive - Loop #5 - Active positions: 1
2025-11-13 07:09:03,462 [INFO] ðŸ’° Current balance: $18.75
2025-11-13 07:09:03,462 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 07:09:03,549 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 07:09:03,868 [INFO] ðŸ“¡ BTCUSDT Signal: HOLD (score: 1/4)
2025-11-13 07:09:03,868 [INFO]    Partial signals: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:09:03,869 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=1
2025-11-13 07:09:03,869 [INFO]    ðŸ“ Signal reasons: SHORT(1): ðŸ“ˆ RSI Overbought
2025-11-13 07:09:03,869 [INFO]    âšª No signal - HOLD
2025-11-13 07:09:04,370 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 07:09:04,457 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 07:09:04,772 [INFO]    ðŸš« ML Conviction too low: 0.568 (distance from 0.5: 0.068 < 0.1)
2025-11-13 07:09:04,772 [INFO] ðŸ“¡ ETHUSDT Signal: HOLD (score: 7/4)
2025-11-13 07:09:04,773 [INFO]    Partial signals: â­ Evening Star, ðŸ’§ Bearish Liquidity Sweep
2025-11-13 07:09:04,774 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=7
2025-11-13 07:09:04,774 [INFO]    ðŸ“ Signal reasons: â­ Evening Star, ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:09:04,774 [INFO]    âšª No signal - HOLD
2025-11-13 07:09:05,275 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 07:09:05,367 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 07:09:05,686 [INFO]    ðŸš« ML Conviction too low: 0.560 (distance from 0.5: 0.060 < 0.1)
2025-11-13 07:09:05,686 [INFO] ðŸ“¡ SOLUSDT Signal: HOLD (score: 4/4)
2025-11-13 07:09:05,687 [INFO]    Partial signals: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:09:05,687 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=4
2025-11-13 07:09:05,687 [INFO]    ðŸ“ Signal reasons: ðŸ’§ Bearish Liquidity Sweep, ðŸ“ˆ RSI Overbought
2025-11-13 07:09:05,687 [INFO]    âšª No signal - HOLD
2025-11-13 07:09:06,188 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 07:09:06,275 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 07:09:06,734 [INFO] ðŸ“¡ LTCUSDT Signal: HOLD (score: 2/4)
2025-11-13 07:09:06,734 [INFO]    Partial signals: LONG(2): ðŸ•¯ï¸ Bullish Engulfing
2025-11-13 07:09:06,735 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=2
2025-11-13 07:09:06,735 [INFO]    ðŸ“ Signal reasons: LONG(2): ðŸ•¯ï¸ Bullish Engulfing
2025-11-13 07:09:06,735 [INFO]    âšª No signal - HOLD
2025-11-13 07:09:07,236 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 07:09:07,322 [INFO]    Current position: LONG 6.0
2025-11-13 07:09:07,322 [INFO]    Entry: $17.52 | Mark: $17.61
2025-11-13 07:09:07,322 [INFO]    PnL: 0.50% ($0.52)
2025-11-13 07:09:07,322 [INFO]    Age: 1.4h / 36.0h
2025-11-13 07:09:07,824 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 07:09:07,911 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 07:09:08,217 [INFO] ðŸ“¡ XRPUSDT Signal: HOLD (score: 0/4)
2025-11-13 07:09:08,218 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 07:09:08,218 [INFO]    âšª No signal - HOLD
2025-11-13 07:09:08,218 [INFO] 
ðŸ’¤ Sleeping 60s...
