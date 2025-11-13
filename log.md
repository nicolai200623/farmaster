2025-11-13 03:58:18,245 [INFO] 
============================================================
2025-11-13 03:58:18,246 [INFO] ðŸ›‘ SHUTTING DOWN BOT
2025-11-13 03:58:18,246 [INFO] ============================================================
2025-11-13 03:58:18,246 [INFO] ðŸ“Š <b>DAILY STATS</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
Trades: 0
Volume: $0.00M
PnL: 0.00%

<b>Overall</b>
Total Trades: 0
Win Rate: 0.0%
W/L: 0/0
2025-11-13 03:58:18,959 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:18,961 [INFO] ðŸ‘‹ Bot stopped!
2025-11-13 03:58:19,342 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
âœ… Using fixed position size: $10.0 USDT per trade
âœ… Config validation passed!
2025-11-13 03:58:21,596 [INFO] âœ… Telegram bot initialized
2025-11-13 03:58:27,391 [INFO] ============================================================
2025-11-13 03:58:27,392 [INFO] ðŸš€ ASTERDEX PERP FARM BOT - INITIALIZING
2025-11-13 03:58:27,392 [INFO] ============================================================
2025-11-13 03:58:27,794 [INFO] ðŸ”Œ AsterDEX Client initialized (MAINNET)
2025-11-13 03:58:27,794 [INFO]    URL: https://fapi.asterdex.com/fapi
2025-11-13 03:58:27,795 [INFO] ðŸ“‚ Loaded 1 position timestamps
2025-11-13 03:58:27,795 [INFO] ðŸŽ­ Loading Ensemble models...
2025-11-13 03:58:27,806 [INFO] ðŸ§  LSTM Model initialized on cpu
2025-11-13 03:58:27,806 [INFO]    Input: 14, Hidden: 128, Layers: 3, Dropout: 0.3
2025-11-13 03:58:27,807 [INFO] ðŸŽ­ Ensemble initialized with 2 models
2025-11-13 03:58:27,807 [INFO]    Models: ['lstm', 'xgboost']
2025-11-13 03:58:27,807 [INFO]    Weights: [0.3 0.7]
2025-11-13 03:58:27,833 [INFO] âœ… Model loaded from models/lstm_model.pt
2025-11-13 03:58:27,834 [INFO] âœ… LSTM loaded
2025-11-13 03:58:27,907 [INFO] âœ… XGBoost model loaded from models/xgboost_model.json
2025-11-13 03:58:27,907 [INFO] âœ… XGBoost loaded
2025-11-13 03:58:27,907 [INFO] âœ… Ensemble loaded: 2/2 models
2025-11-13 03:58:27,907 [INFO] ðŸŽ­ Using Ensemble predictor: ['lstm', 'xgboost']
2025-11-13 03:58:27,907 [INFO]    Weights: [0.3, 0.7]
2025-11-13 03:58:27,907 [INFO] ðŸŽ¯ Advanced Entry System enabled (min score: 4)
2025-11-13 03:58:27,908 [INFO] âœ… Bot initialized successfully!
2025-11-13 03:58:27,908 [INFO]    Symbols: ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'LTCUSDT', 'AVAXUSDT', 'XRPUSDT']
2025-11-13 03:58:27,908 [INFO]    Leverage: 10x
2025-11-13 03:58:27,908 [INFO]    Position Size: 20.0%
2025-11-13 03:58:27,908 [INFO]    TP/SL: 100.0% / Disabled
2025-11-13 03:58:27,908 [INFO]    Position Timeout: 36.0h
2025-11-13 03:58:27,908 [INFO] ============================================================
2025-11-13 03:58:27,908 [INFO] ðŸ BOT STARTED!
2025-11-13 03:58:28,646 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:28,821 [INFO] ðŸ“Š Daily start balance: $18.76
2025-11-13 03:58:28,822 [INFO] ðŸ’° Starting balance: $18.76
2025-11-13 03:58:29,202 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:29,204 [INFO] 
============================================================
2025-11-13 03:58:29,204 [INFO] ðŸ”„ LOOP #1 - 2025-11-13 03:58:29
2025-11-13 03:58:29,204 [INFO] ============================================================
2025-11-13 03:58:29,289 [INFO] ðŸ’° Current balance: $18.76
2025-11-13 03:58:29,289 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 03:58:29,372 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 03:58:29,590 [ERROR] Signal generation error for BTCUSDT: 'Logger' object has no attribute 'debug'
2025-11-13 03:58:29,974 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:29,977 [ERROR] Traceback (most recent call last):
  File "/home/farmaster/farmaster/trading/signal_generator.py", line 125, in generate_signal
    logger.debug(f"   ML predictions:")
AttributeError: 'Logger' object has no attribute 'debug'

2025-11-13 03:58:30,356 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:30,358 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 03:58:30,359 [INFO]    âšª No signal - HOLD
2025-11-13 03:58:30,859 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 03:58:30,945 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 03:58:31,148 [ERROR] Signal generation error for ETHUSDT: 'Logger' object has no attribute 'debug'
2025-11-13 03:58:34,733 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:34,736 [ERROR] Traceback (most recent call last):
  File "/home/farmaster/farmaster/trading/signal_generator.py", line 125, in generate_signal
    logger.debug(f"   ML predictions:")
AttributeError: 'Logger' object has no attribute 'debug'

2025-11-13 03:58:35,119 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:35,120 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 03:58:35,120 [INFO]    âšª No signal - HOLD
2025-11-13 03:58:35,621 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 03:58:35,710 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 03:58:35,911 [ERROR] Signal generation error for SOLUSDT: 'Logger' object has no attribute 'debug'
2025-11-13 03:58:36,300 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:36,303 [ERROR] Traceback (most recent call last):
  File "/home/farmaster/farmaster/trading/signal_generator.py", line 125, in generate_signal
    logger.debug(f"   ML predictions:")
AttributeError: 'Logger' object has no attribute 'debug'

2025-11-13 03:58:36,689 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:36,691 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 03:58:36,691 [INFO]    âšª No signal - HOLD
2025-11-13 03:58:37,192 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 03:58:37,274 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 03:58:37,609 [ERROR] Signal generation error for LTCUSDT: 'Logger' object has no attribute 'debug'
2025-11-13 03:58:38,007 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:38,009 [ERROR] Traceback (most recent call last):
  File "/home/farmaster/farmaster/trading/signal_generator.py", line 125, in generate_signal
    logger.debug(f"   ML predictions:")
AttributeError: 'Logger' object has no attribute 'debug'

2025-11-13 03:58:41,590 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:41,595 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 03:58:41,595 [INFO]    âšª No signal - HOLD
2025-11-13 03:58:42,096 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 03:58:42,183 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 03:58:42,386 [ERROR] Signal generation error for AVAXUSDT: 'Logger' object has no attribute 'debug'
2025-11-13 03:58:42,919 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:42,922 [ERROR] Traceback (most recent call last):
  File "/home/farmaster/farmaster/trading/signal_generator.py", line 125, in generate_signal
    logger.debug(f"   ML predictions:")
AttributeError: 'Logger' object has no attribute 'debug'

2025-11-13 03:58:43,358 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:43,360 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 03:58:43,360 [INFO]    âšª No signal - HOLD
2025-11-13 03:58:43,861 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 03:58:43,944 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 03:58:44,159 [ERROR] Signal generation error for XRPUSDT: 'Logger' object has no attribute 'debug'
2025-11-13 03:58:47,740 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:47,742 [ERROR] Traceback (most recent call last):
  File "/home/farmaster/farmaster/trading/signal_generator.py", line 125, in generate_signal
    logger.debug(f"   ML predictions:")
AttributeError: 'Logger' object has no attribute 'debug'

2025-11-13 03:58:48,122 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:58:48,124 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 03:58:48,124 [INFO]    âšª No signal - HOLD
2025-11-13 03:58:48,124 [INFO] 
ðŸ’¤ Sleeping 60s...
2025-11-13 03:59:48,179 [INFO] 
============================================================
2025-11-13 03:59:48,179 [INFO] ðŸ”„ LOOP #2 - 2025-11-13 03:59:48
2025-11-13 03:59:48,179 [INFO] ============================================================
2025-11-13 03:59:48,300 [INFO] ðŸ’° Current balance: $18.76
2025-11-13 03:59:48,300 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-11-13 03:59:48,386 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-11-13 03:59:48,582 [ERROR] Signal generation error for BTCUSDT: 'Logger' object has no attribute 'debug'
2025-11-13 03:59:49,425 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:59:49,427 [ERROR] Traceback (most recent call last):
  File "/home/farmaster/farmaster/trading/signal_generator.py", line 125, in generate_signal
    logger.debug(f"   ML predictions:")
AttributeError: 'Logger' object has no attribute 'debug'

2025-11-13 03:59:49,838 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:59:49,840 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 03:59:49,840 [INFO]    âšª No signal - HOLD
2025-11-13 03:59:50,341 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-11-13 03:59:50,427 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-11-13 03:59:50,622 [ERROR] Signal generation error for ETHUSDT: 'Logger' object has no attribute 'debug'
2025-11-13 03:59:51,046 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:59:51,050 [ERROR] Traceback (most recent call last):
  File "/home/farmaster/farmaster/trading/signal_generator.py", line 125, in generate_signal
    logger.debug(f"   ML predictions:")
AttributeError: 'Logger' object has no attribute 'debug'

2025-11-13 03:59:51,504 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:59:51,507 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 03:59:51,508 [INFO]    âšª No signal - HOLD
2025-11-13 03:59:52,008 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-11-13 03:59:52,094 [INFO]    ðŸ” Analyzing SOLUSDT for entry signal...
2025-11-13 03:59:52,287 [ERROR] Signal generation error for SOLUSDT: 'Logger' object has no attribute 'debug'
2025-11-13 03:59:52,787 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:59:52,789 [ERROR] Traceback (most recent call last):
  File "/home/farmaster/farmaster/trading/signal_generator.py", line 125, in generate_signal
    logger.debug(f"   ML predictions:")
AttributeError: 'Logger' object has no attribute 'debug'

2025-11-13 03:59:56,580 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:59:56,583 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 03:59:56,583 [INFO]    âšª No signal - HOLD
2025-11-13 03:59:57,084 [INFO] 
ðŸ“Š Processing LTCUSDT...
2025-11-13 03:59:57,173 [INFO]    ðŸ” Analyzing LTCUSDT for entry signal...
2025-11-13 03:59:57,366 [ERROR] Signal generation error for LTCUSDT: 'Logger' object has no attribute 'debug'
2025-11-13 03:59:57,791 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:59:57,795 [ERROR] Traceback (most recent call last):
  File "/home/farmaster/farmaster/trading/signal_generator.py", line 125, in generate_signal
    logger.debug(f"   ML predictions:")
AttributeError: 'Logger' object has no attribute 'debug'

2025-11-13 03:59:58,234 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:59:58,236 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 03:59:58,236 [INFO]    âšª No signal - HOLD
2025-11-13 03:59:58,737 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-11-13 03:59:58,824 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-11-13 03:59:59,031 [ERROR] Signal generation error for AVAXUSDT: 'Logger' object has no attribute 'debug'
2025-11-13 03:59:59,442 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:59:59,444 [ERROR] Traceback (most recent call last):
  File "/home/farmaster/farmaster/trading/signal_generator.py", line 125, in generate_signal
    logger.debug(f"   ML predictions:")
AttributeError: 'Logger' object has no attribute 'debug'

2025-11-13 03:59:59,877 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 03:59:59,879 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 03:59:59,879 [INFO]    âšª No signal - HOLD
2025-11-13 04:00:00,380 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-11-13 04:00:00,475 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-11-13 04:00:00,701 [ERROR] Signal generation error for XRPUSDT: 'Logger' object has no attribute 'debug'
2025-11-13 04:00:04,395 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:00:04,417 [ERROR] Traceback (most recent call last):
  File "/home/farmaster/farmaster/trading/signal_generator.py", line 125, in generate_signal
    logger.debug(f"   ML predictions:")
AttributeError: 'Logger' object has no attribute 'debug'

2025-11-13 04:00:04,935 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-11-13 04:00:04,957 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-11-13 04:00:04,960 [INFO]    âšª No signal - HOLD
2025-11-13 04:00:04,960 [INFO] 
ðŸ’¤ Sleeping 60s...
