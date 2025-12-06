2025-12-06 07:04:48,546 [INFO] 
ðŸ›‘ Shutdown signal received...
2025-12-06 07:06:19,393 [INFO] âœ… Telegram bot initialized
2025-12-06 07:06:27,514 [INFO] ============================================================
2025-12-06 07:06:27,515 [INFO] ðŸš€ ASTERDEX PERP FARM BOT - INITIALIZING
2025-12-06 07:06:27,515 [INFO] ============================================================
2025-12-06 07:06:27,677 [INFO] ðŸ”Œ AsterDEX Client initialized (MAINNET)
2025-12-06 07:06:27,678 [INFO]    URL: https://fapi.asterdex.com/fapi
2025-12-06 07:06:27,679 [INFO] ðŸ“‚ Loaded 2 position timestamps
2025-12-06 07:06:27,679 [INFO] ðŸ“ˆ Trailing Stop enabled (PnL-based): Activation=2.5% PnL, Trail=2.2% PnL
2025-12-06 07:06:27,679 [INFO] ðŸŽ­ Loading Ensemble models...
2025-12-06 07:06:27,680 [INFO] ðŸ’¡ LightGBM Trainer initialized with 23 features
2025-12-06 07:06:27,680 [INFO] ðŸ± CatBoost Trainer initialized with 23 features
2025-12-06 07:06:27,680 [INFO] ðŸŽ­ Ensemble initialized with 3 models
2025-12-06 07:06:27,680 [INFO]    Models: ['xgboost', 'lightgbm', 'catboost']
2025-12-06 07:06:27,680 [INFO]    Weights: [0.4  0.35 0.25]
2025-12-06 07:06:27,749 [INFO] âœ… XGBoost model loaded from models/xgboost_model.json
2025-12-06 07:06:27,749 [INFO] âœ… XGBoost loaded
2025-12-06 07:06:27,788 [INFO] âœ… LightGBM loaded from models/lightgbm_model.txt
2025-12-06 07:06:27,788 [INFO] âœ… LightGBM loaded
2025-12-06 07:06:27,798 [INFO] âœ… CatBoost loaded from models/catboost_model.cbm
2025-12-06 07:06:27,798 [INFO] âœ… CatBoost loaded
2025-12-06 07:06:27,798 [INFO] âœ… Ensemble loaded: 3/3 models
2025-12-06 07:06:27,798 [INFO] ðŸŽ­ Using Ensemble predictor: ['xgboost', 'lightgbm', 'catboost']
2025-12-06 07:06:27,798 [INFO]    Weights: [0.4, 0.35, 0.25]
2025-12-06 07:06:27,798 [INFO] ðŸŽ¯ SmartEntrySystemV2 enabled (min score: 6, min R:R: 0.0:1)
2025-12-06 07:06:27,799 [INFO] ðŸš« Signal Cooldown enabled: 60m signal, 15m post-trade
2025-12-06 07:06:27,799 [INFO] ðŸŽ¯ Entry Quality Checker enabled
2025-12-06 07:06:27,799 [INFO] ðŸŽ­ Entry Pipeline received 3 ML models: ['xgboost', 'lightgbm', 'catboost']
2025-12-06 07:06:27,799 [INFO] ðŸŽ­ MLEnsembleSignal initialized
2025-12-06 07:06:27,799 [INFO]    Models: ['xgboost', 'lightgbm', 'catboost']
2025-12-06 07:06:27,799 [INFO]    Weights: {'xgboost': 0.4, 'lightgbm': 0.35, 'catboost': 0.25}
2025-12-06 07:06:27,799 [INFO]    Confidence threshold: 0.65
2025-12-06 07:06:27,799 [INFO] ðŸŽ¯ SmartEntryScoring initialized (min score: 6)
2025-12-06 07:06:27,799 [INFO] ðŸŽ¨ PriceActionValidator initialized (min score: 6/8)
2025-12-06 07:06:27,799 [INFO] ðŸ“ˆ HTFTrendAligner initialized (TF: 4h)
2025-12-06 07:06:27,799 [WARNING] âš ï¸ AI Check enabled but claude client not available
2025-12-06 07:06:28,516 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-12-06 07:06:28,517 [INFO] ðŸš€ EntryPipeline initialized
2025-12-06 07:06:28,518 [INFO]    Stages enabled: ML=True, SmartEntry=True, PA=True, HTF=True, AI=True
2025-12-06 07:06:28,518 [INFO] ðŸš€ Entry Pipeline enabled (5-stage validation)
2025-12-06 07:06:28,518 [INFO] âœ… Bot initialized successfully!
2025-12-06 07:06:28,518 [INFO]    Symbols: ['ADAUSDT', 'BNBUSDT', 'DOGEUSDT', 'UNIUSDT', 'LINKUSDT', 'BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'XRPUSDT', 'DOTUSDT', 'AVAXUSDT', 'NEARUSDT']
2025-12-06 07:06:28,518 [INFO]    Leverage: 10x
2025-12-06 07:06:28,518 [INFO]    Position Size: 20.0%
2025-12-06 07:06:28,518 [INFO]    TP/SL: 10.00% / Disabled
2025-12-06 07:06:28,518 [INFO]    Position Timeout: 72.0h
2025-12-06 07:06:28,518 [INFO]    ðŸ“Š Timeframe: PRIMARY=1h, HIGHER=4h
2025-12-06 07:06:28,518 [INFO]    ðŸ”„ Loop Sleep: 180s
2025-12-06 07:06:28,518 [INFO] ============================================================
2025-12-06 07:06:28,518 [INFO] ðŸ BOT STARTED!
2025-12-06 07:06:28,883 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-12-06 07:06:29,076 [INFO] ðŸ“Š Daily start balance: $29.10
2025-12-06 07:06:29,076 [INFO] ðŸ’° Starting balance: $29.10
2025-12-06 07:06:29,451 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-12-06 07:06:29,453 [INFO] 
============================================================
2025-12-06 07:06:29,453 [INFO] ðŸ”„ LOOP #1 - 2025-12-06 07:06:29
2025-12-06 07:06:29,453 [INFO] ============================================================
2025-12-06 07:06:29,540 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:06:29,541 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:06:29,627 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:06:30,325 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:06:30,325 [INFO]    âšª No signal - HOLD
2025-12-06 07:06:30,826 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:06:30,916 [INFO]    Current position: LONG 0.11
2025-12-06 07:06:30,916 [INFO]    Entry: $924.70 | Mark: $885.98
2025-12-06 07:06:30,916 [INFO]    PnL: -41.88% ($-4.26)
2025-12-06 07:06:30,916 [INFO]    Age: 52.6h / 72.0h
2025-12-06 07:06:31,417 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:06:31,503 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:06:32,206 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 10/15
2025-12-06 07:06:32,206 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:06:32,206 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:06:32,206 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:06:32,207 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:06:32,207 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:06:32,207 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:06:32,224 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:06:32,224 [INFO]    âšª No signal - HOLD
2025-12-06 07:06:32,725 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:06:32,809 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:06:33,500 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:06:33,500 [INFO]    âšª No signal - HOLD
2025-12-06 07:06:34,001 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:06:34,083 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:06:34,854 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:06:34,855 [INFO]    âšª No signal - HOLD
2025-12-06 07:06:35,355 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:06:35,442 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:06:36,204 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:06:36,204 [INFO]    âšª No signal - HOLD
2025-12-06 07:06:36,705 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:06:36,793 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:06:37,496 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:06:37,496 [INFO]    âšª No signal - HOLD
2025-12-06 07:06:37,997 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:06:38,082 [INFO]    Current position: LONG 0.69
2025-12-06 07:06:38,082 [INFO]    Entry: $145.48 | Mark: $132.94
2025-12-06 07:06:38,082 [INFO]    PnL: -86.23% ($-8.66)
2025-12-06 07:06:38,082 [INFO]    Age: 53.5h / 72.0h
2025-12-06 07:06:38,583 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:06:38,670 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:06:39,323 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:06:39,324 [INFO]    âšª No signal - HOLD
2025-12-06 07:06:39,824 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:06:39,909 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:06:40,683 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 9/15
2025-12-06 07:06:40,683 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:06:40,683 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:06:40,683 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:06:40,683 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:06:40,683 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:06:40,694 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:06:40,694 [INFO]    âšª No signal - HOLD
2025-12-06 07:06:41,195 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:06:41,278 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:06:41,958 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 10/15
2025-12-06 07:06:41,958 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:06:41,958 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:06:41,958 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:06:41,958 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:06:41,958 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:06:41,958 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:06:41,972 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:06:41,972 [INFO]    âšª No signal - HOLD
2025-12-06 07:06:42,473 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:06:42,560 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:06:43,198 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 07:06:43,199 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:06:43,199 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:06:43,199 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:06:43,199 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:06:43,199 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:06:43,209 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:06:43,209 [INFO]    âšª No signal - HOLD
2025-12-06 07:06:43,210 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:09:43,281 [INFO] 
============================================================
2025-12-06 07:09:43,282 [INFO] ðŸ”„ LOOP #2 - 2025-12-06 07:09:43
2025-12-06 07:09:43,282 [INFO] ============================================================
2025-12-06 07:09:43,369 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:09:43,369 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:09:43,457 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:09:44,147 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:09:44,147 [INFO]    âšª No signal - HOLD
2025-12-06 07:09:44,648 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:09:44,732 [INFO]    Current position: LONG 0.11
2025-12-06 07:09:44,732 [INFO]    Entry: $924.70 | Mark: $886.40
2025-12-06 07:09:44,732 [INFO]    PnL: -41.42% ($-4.21)
2025-12-06 07:09:44,732 [INFO]    Age: 52.7h / 72.0h
2025-12-06 07:09:45,233 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:09:45,321 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:09:45,982 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 10/15
2025-12-06 07:09:45,982 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:09:45,982 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:09:45,982 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:09:45,982 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:09:45,983 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:09:45,983 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:09:45,988 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:09:45,989 [INFO]    âšª No signal - HOLD
2025-12-06 07:09:46,489 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:09:46,571 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:09:47,268 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:09:47,268 [INFO]    âšª No signal - HOLD
2025-12-06 07:09:47,769 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:09:47,851 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:09:48,492 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:09:48,493 [INFO]    âšª No signal - HOLD
2025-12-06 07:09:48,993 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:09:49,079 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:09:49,776 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:09:49,776 [INFO]    âšª No signal - HOLD
2025-12-06 07:09:50,277 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:09:50,361 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:09:51,012 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:09:51,012 [INFO]    âšª No signal - HOLD
2025-12-06 07:09:51,513 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:09:51,595 [INFO]    Current position: LONG 0.69
2025-12-06 07:09:51,595 [INFO]    Entry: $145.48 | Mark: $133.03
2025-12-06 07:09:51,595 [INFO]    PnL: -85.61% ($-8.59)
2025-12-06 07:09:51,595 [INFO]    Age: 53.6h / 72.0h
2025-12-06 07:09:52,096 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:09:52,179 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:09:52,859 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:09:52,859 [INFO]    âšª No signal - HOLD
2025-12-06 07:09:53,360 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:09:53,444 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:09:54,082 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 9/15
2025-12-06 07:09:54,083 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:09:54,083 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:09:54,083 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:09:54,083 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:09:54,083 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:09:54,087 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:09:54,088 [INFO]    âšª No signal - HOLD
2025-12-06 07:09:54,588 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:09:54,675 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:09:55,462 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 10/15
2025-12-06 07:09:55,463 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:09:55,463 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:09:55,463 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:09:55,463 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:09:55,463 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:09:55,463 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:09:55,467 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:09:55,468 [INFO]    âšª No signal - HOLD
2025-12-06 07:09:55,968 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:09:56,058 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:09:56,679 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 07:09:56,679 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:09:56,679 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:09:56,679 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:09:56,679 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:09:56,679 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:09:56,683 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:09:56,684 [INFO]    âšª No signal - HOLD
2025-12-06 07:09:56,684 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:12:56,705 [INFO] 
============================================================
2025-12-06 07:12:56,706 [INFO] ðŸ”„ LOOP #3 - 2025-12-06 07:12:56
2025-12-06 07:12:56,706 [INFO] ============================================================
2025-12-06 07:12:56,791 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:12:56,791 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:12:56,876 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:12:57,549 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:12:57,550 [INFO]    âšª No signal - HOLD
2025-12-06 07:12:58,050 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:12:58,137 [INFO]    Current position: LONG 0.11
2025-12-06 07:12:58,137 [INFO]    Entry: $924.70 | Mark: $885.71
2025-12-06 07:12:58,137 [INFO]    PnL: -42.16% ($-4.29)
2025-12-06 07:12:58,137 [INFO]    Age: 52.8h / 72.0h
2025-12-06 07:12:58,638 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:12:58,724 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:12:59,416 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 10/15
2025-12-06 07:12:59,416 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:12:59,417 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:12:59,417 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:12:59,417 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:12:59,417 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:12:59,417 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:12:59,422 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:12:59,423 [INFO]    âšª No signal - HOLD
2025-12-06 07:12:59,923 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:13:00,010 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:13:00,679 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 9/15
2025-12-06 07:13:00,679 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 07:13:00,679 [INFO]    âš ï¸ Near EMA21
2025-12-06 07:13:00,679 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:13:00,679 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:13:00,679 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:13:00,679 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:13:00,691 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:13:00,692 [INFO]    âšª No signal - HOLD
2025-12-06 07:13:01,192 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:13:01,412 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:13:02,099 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:13:02,099 [INFO]    âšª No signal - HOLD
2025-12-06 07:13:02,600 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:13:02,685 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:13:03,509 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:13:03,509 [INFO]    âšª No signal - HOLD
2025-12-06 07:13:04,010 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:13:04,101 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:13:04,805 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:13:04,805 [INFO]    âšª No signal - HOLD
2025-12-06 07:13:05,306 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:13:05,391 [INFO]    Current position: LONG 0.69
2025-12-06 07:13:05,392 [INFO]    Entry: $145.48 | Mark: $133.01
2025-12-06 07:13:05,392 [INFO]    PnL: -85.68% ($-8.60)
2025-12-06 07:13:05,392 [INFO]    Age: 53.6h / 72.0h
2025-12-06 07:13:05,893 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:13:05,976 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:13:06,718 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:13:06,718 [INFO]    âšª No signal - HOLD
2025-12-06 07:13:07,219 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:13:07,305 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:13:07,980 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 9/15
2025-12-06 07:13:07,980 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:13:07,981 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:13:07,981 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:13:07,981 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:13:07,981 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:13:07,987 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:13:07,987 [INFO]    âšª No signal - HOLD
2025-12-06 07:13:08,488 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:13:08,573 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:13:09,269 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 10/15
2025-12-06 07:13:09,270 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:13:09,270 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:13:09,270 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:13:09,270 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:13:09,270 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:13:09,270 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:13:09,276 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:13:09,276 [INFO]    âšª No signal - HOLD
2025-12-06 07:13:09,777 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:13:09,862 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:13:10,524 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 07:13:10,524 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:13:10,524 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:13:10,524 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:13:10,524 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:13:10,524 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:13:10,530 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:13:10,530 [INFO]    âšª No signal - HOLD
2025-12-06 07:13:10,530 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:16:10,629 [INFO] 
============================================================
2025-12-06 07:16:10,630 [INFO] ðŸ”„ LOOP #4 - 2025-12-06 07:16:10
2025-12-06 07:16:10,630 [INFO] ============================================================
2025-12-06 07:16:10,714 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:16:10,715 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:16:10,801 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:16:11,428 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:16:11,428 [INFO]    âšª No signal - HOLD
2025-12-06 07:16:11,929 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:16:12,015 [INFO]    Current position: LONG 0.11
2025-12-06 07:16:12,015 [INFO]    Entry: $924.70 | Mark: $886.25
2025-12-06 07:16:12,015 [INFO]    PnL: -41.58% ($-4.23)
2025-12-06 07:16:12,015 [INFO]    Age: 52.8h / 72.0h
2025-12-06 07:16:12,516 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:16:12,600 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:16:13,230 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 10/15
2025-12-06 07:16:13,230 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:16:13,230 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:16:13,230 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:16:13,230 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:16:13,230 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:16:13,231 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:16:13,235 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:16:13,235 [INFO]    âšª No signal - HOLD
2025-12-06 07:16:13,736 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:16:13,825 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:16:14,473 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 9/15
2025-12-06 07:16:14,473 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 07:16:14,473 [INFO]    âš ï¸ Near EMA21
2025-12-06 07:16:14,473 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:16:14,474 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:16:14,474 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:16:14,474 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:16:14,478 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:16:14,478 [INFO]    âšª No signal - HOLD
2025-12-06 07:16:14,979 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:16:15,063 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:16:15,694 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:16:15,694 [INFO]    âšª No signal - HOLD
2025-12-06 07:16:16,195 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:16:16,279 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:16:16,968 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:16:16,968 [INFO]    âšª No signal - HOLD
2025-12-06 07:16:17,469 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:16:17,562 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:16:18,228 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:16:18,228 [INFO]    âšª No signal - HOLD
2025-12-06 07:16:18,729 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:16:18,815 [INFO]    Current position: LONG 0.69
2025-12-06 07:16:18,815 [INFO]    Entry: $145.48 | Mark: $133.05
2025-12-06 07:16:18,816 [INFO]    PnL: -85.44% ($-8.58)
2025-12-06 07:16:18,816 [INFO]    Age: 53.7h / 72.0h
2025-12-06 07:16:19,316 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:16:19,400 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:16:20,040 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:16:20,041 [INFO]    âšª No signal - HOLD
2025-12-06 07:16:20,541 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:16:20,630 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:16:21,472 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 9/15
2025-12-06 07:16:21,472 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:16:21,473 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:16:21,473 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:16:21,473 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:16:21,473 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:16:21,479 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:16:21,479 [INFO]    âšª No signal - HOLD
2025-12-06 07:16:21,980 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:16:22,063 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:16:22,855 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 10/15
2025-12-06 07:16:22,855 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:16:22,855 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:16:22,855 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:16:22,855 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:16:22,855 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:16:22,856 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:16:22,860 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:16:22,861 [INFO]    âšª No signal - HOLD
2025-12-06 07:16:23,361 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:16:23,445 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:16:24,107 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 07:16:24,107 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:16:24,107 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:16:24,107 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:16:24,107 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:16:24,108 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:16:24,113 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:16:24,114 [INFO]    âšª No signal - HOLD
2025-12-06 07:16:24,114 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:19:24,137 [INFO] 
============================================================
2025-12-06 07:19:24,138 [INFO] ðŸ”„ LOOP #5 - 2025-12-06 07:19:24
2025-12-06 07:19:24,138 [INFO] ============================================================
2025-12-06 07:19:25,322 [INFO] ðŸ’“ Bot alive - Loop #5 - Active positions: 2
2025-12-06 07:19:25,407 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:19:25,407 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:19:25,488 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:19:26,102 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:19:26,102 [INFO]    âšª No signal - HOLD
2025-12-06 07:19:26,603 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:19:26,688 [INFO]    Current position: LONG 0.11
2025-12-06 07:19:26,688 [INFO]    Entry: $924.70 | Mark: $886.13
2025-12-06 07:19:26,688 [INFO]    PnL: -41.71% ($-4.24)
2025-12-06 07:19:26,688 [INFO]    Age: 52.9h / 72.0h
2025-12-06 07:19:27,189 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:19:27,276 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:19:27,923 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 10/15
2025-12-06 07:19:27,924 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:19:27,924 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:19:27,924 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:19:27,924 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:19:27,924 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:19:27,924 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:19:27,928 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:19:27,928 [INFO]    âšª No signal - HOLD
2025-12-06 07:19:28,429 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:19:28,516 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:19:29,122 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 9/15
2025-12-06 07:19:29,122 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 07:19:29,122 [INFO]    âš ï¸ Near EMA21
2025-12-06 07:19:29,122 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:19:29,122 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:19:29,122 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:19:29,122 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:19:29,126 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:19:29,126 [INFO]    âšª No signal - HOLD
2025-12-06 07:19:29,627 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:19:29,712 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:19:30,336 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:19:30,336 [INFO]    âšª No signal - HOLD
2025-12-06 07:19:30,837 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:19:30,920 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:19:31,554 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:19:31,554 [INFO]    âšª No signal - HOLD
2025-12-06 07:19:32,055 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:19:32,140 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:19:32,752 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:19:32,752 [INFO]    âšª No signal - HOLD
2025-12-06 07:19:33,253 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:19:33,339 [INFO]    Current position: LONG 0.69
2025-12-06 07:19:33,339 [INFO]    Entry: $145.48 | Mark: $133.10
2025-12-06 07:19:33,339 [INFO]    PnL: -85.10% ($-8.54)
2025-12-06 07:19:33,339 [INFO]    Age: 53.7h / 72.0h
2025-12-06 07:19:33,840 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:19:33,926 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:19:34,694 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:19:34,694 [INFO]    âšª No signal - HOLD
2025-12-06 07:19:35,195 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:19:35,283 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:19:35,930 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 9/15
2025-12-06 07:19:35,931 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:19:35,931 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:19:35,931 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:19:35,931 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:19:35,931 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:19:35,940 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:19:35,940 [INFO]    âšª No signal - HOLD
2025-12-06 07:19:36,441 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:19:36,525 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:19:37,218 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 10/15
2025-12-06 07:19:37,218 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:19:37,219 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:19:37,219 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:19:37,219 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:19:37,219 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:19:37,219 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:19:37,223 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:19:37,223 [INFO]    âšª No signal - HOLD
2025-12-06 07:19:37,724 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:19:37,810 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:19:38,407 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 07:19:38,407 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:19:38,407 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:19:38,408 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:19:38,408 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:19:38,408 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:19:38,412 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:19:38,412 [INFO]    âšª No signal - HOLD
2025-12-06 07:19:38,412 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:22:38,512 [INFO] 
============================================================
2025-12-06 07:22:38,512 [INFO] ðŸ”„ LOOP #6 - 2025-12-06 07:22:38
2025-12-06 07:22:38,512 [INFO] ============================================================
2025-12-06 07:22:38,599 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:22:38,599 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:22:38,685 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:22:40,056 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:22:40,056 [INFO]    âšª No signal - HOLD
2025-12-06 07:22:40,557 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:22:40,643 [INFO]    Current position: LONG 0.11
2025-12-06 07:22:40,643 [INFO]    Entry: $924.70 | Mark: $885.65
2025-12-06 07:22:40,643 [INFO]    PnL: -42.23% ($-4.30)
2025-12-06 07:22:40,643 [INFO]    Age: 52.9h / 72.0h
2025-12-06 07:22:41,144 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:22:41,233 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:22:42,241 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 10/15
2025-12-06 07:22:42,241 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:22:42,241 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:22:42,241 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:22:42,241 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:22:42,241 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:22:42,241 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:22:42,265 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:22:42,283 [INFO]    âšª No signal - HOLD
2025-12-06 07:22:42,784 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:22:42,865 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:22:43,836 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 9/15
2025-12-06 07:22:43,836 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 07:22:43,836 [INFO]    âš ï¸ Near EMA21
2025-12-06 07:22:43,836 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:22:43,836 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:22:43,836 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:22:43,836 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:22:43,845 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:22:43,845 [INFO]    âšª No signal - HOLD
2025-12-06 07:22:44,345 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:22:44,430 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:22:45,434 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:22:45,435 [INFO]    âšª No signal - HOLD
2025-12-06 07:22:45,935 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:22:46,023 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:22:47,110 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:22:47,110 [INFO]    âšª No signal - HOLD
2025-12-06 07:22:47,611 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:22:47,702 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:22:48,733 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:22:48,734 [INFO]    âšª No signal - HOLD
2025-12-06 07:22:49,235 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:22:49,323 [INFO]    Current position: LONG 0.69
2025-12-06 07:22:49,323 [INFO]    Entry: $145.48 | Mark: $133.01
2025-12-06 07:22:49,323 [INFO]    PnL: -85.73% ($-8.61)
2025-12-06 07:22:49,323 [INFO]    Age: 53.8h / 72.0h
2025-12-06 07:22:49,824 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:22:49,908 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:22:50,612 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:22:50,613 [INFO]    âšª No signal - HOLD
2025-12-06 07:22:51,113 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:22:51,200 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:22:51,900 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 9/15
2025-12-06 07:22:51,900 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:22:51,901 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:22:51,901 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:22:51,901 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:22:51,901 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:22:51,906 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:22:51,907 [INFO]    âšª No signal - HOLD
2025-12-06 07:22:52,407 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:22:52,496 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:22:53,179 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 10/15
2025-12-06 07:22:53,179 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:22:53,179 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:22:53,179 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:22:53,179 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:22:53,179 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:22:53,179 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:22:53,183 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:22:53,184 [INFO]    âšª No signal - HOLD
2025-12-06 07:22:53,684 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:22:53,775 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:22:54,457 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 07:22:54,458 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:22:54,458 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:22:54,458 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:22:54,458 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:22:54,458 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:22:54,464 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:22:54,464 [INFO]    âšª No signal - HOLD
2025-12-06 07:22:54,464 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:25:54,543 [INFO] 
============================================================
2025-12-06 07:25:54,544 [INFO] ðŸ”„ LOOP #7 - 2025-12-06 07:25:54
2025-12-06 07:25:54,544 [INFO] ============================================================
2025-12-06 07:25:54,629 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:25:54,630 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:25:54,712 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:25:55,415 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:25:55,416 [INFO]    âšª No signal - HOLD
2025-12-06 07:25:55,917 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:25:56,003 [INFO]    Current position: LONG 0.11
2025-12-06 07:25:56,003 [INFO]    Entry: $924.70 | Mark: $886.05
2025-12-06 07:25:56,003 [INFO]    PnL: -41.80% ($-4.25)
2025-12-06 07:25:56,003 [INFO]    Age: 53.0h / 72.0h
2025-12-06 07:25:56,504 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:25:56,587 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:25:57,280 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 10/15
2025-12-06 07:25:57,280 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:25:57,280 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:25:57,280 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:25:57,280 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:25:57,281 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:25:57,281 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:25:57,285 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:25:57,285 [INFO]    âšª No signal - HOLD
2025-12-06 07:25:57,786 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:25:57,870 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:25:58,703 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:25:58,703 [INFO]    âšª No signal - HOLD
2025-12-06 07:25:59,204 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:25:59,289 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:25:59,983 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:25:59,984 [INFO]    âšª No signal - HOLD
2025-12-06 07:26:00,485 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:26:00,568 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:26:01,242 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:26:01,242 [INFO]    âšª No signal - HOLD
2025-12-06 07:26:01,743 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:26:01,825 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:26:02,586 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:26:02,586 [INFO]    âšª No signal - HOLD
2025-12-06 07:26:03,087 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:26:03,172 [INFO]    Current position: LONG 0.69
2025-12-06 07:26:03,173 [INFO]    Entry: $145.48 | Mark: $132.94
2025-12-06 07:26:03,173 [INFO]    PnL: -86.19% ($-8.65)
2025-12-06 07:26:03,173 [INFO]    Age: 53.8h / 72.0h
2025-12-06 07:26:03,674 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:26:03,758 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:26:04,433 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:26:04,433 [INFO]    âšª No signal - HOLD
2025-12-06 07:26:04,934 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:26:05,020 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:26:05,672 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:26:05,672 [INFO]    âšª No signal - HOLD
2025-12-06 07:26:06,173 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:26:06,271 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:26:06,966 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 10/15
2025-12-06 07:26:06,967 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:26:06,967 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:26:06,967 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:26:06,967 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:26:06,967 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:26:06,967 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:26:06,973 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:26:06,973 [INFO]    âšª No signal - HOLD
2025-12-06 07:26:07,474 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:26:07,563 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:26:08,257 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 07:26:08,257 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:26:08,257 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:26:08,257 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:26:08,257 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:26:08,257 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:26:08,263 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:26:08,263 [INFO]    âšª No signal - HOLD
2025-12-06 07:26:08,263 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:29:08,301 [INFO] 
============================================================
2025-12-06 07:29:08,302 [INFO] ðŸ”„ LOOP #8 - 2025-12-06 07:29:08
2025-12-06 07:29:08,302 [INFO] ============================================================
2025-12-06 07:29:08,397 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:29:08,397 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:29:08,493 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:29:09,117 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:29:09,117 [INFO]    âšª No signal - HOLD
2025-12-06 07:29:09,617 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:29:09,706 [INFO]    Current position: LONG 0.11
2025-12-06 07:29:09,707 [INFO]    Entry: $924.70 | Mark: $885.11
2025-12-06 07:29:09,707 [INFO]    PnL: -42.82% ($-4.36)
2025-12-06 07:29:09,707 [INFO]    Age: 53.0h / 72.0h
2025-12-06 07:29:10,208 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:29:10,294 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:29:10,920 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:29:10,920 [INFO]    âšª No signal - HOLD
2025-12-06 07:29:11,421 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:29:11,510 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:29:12,128 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:29:12,129 [INFO]    âšª No signal - HOLD
2025-12-06 07:29:12,629 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:29:12,715 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:29:13,394 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:29:13,394 [INFO]    âšª No signal - HOLD
2025-12-06 07:29:13,895 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:29:13,976 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:29:14,625 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:29:14,625 [INFO]    âšª No signal - HOLD
2025-12-06 07:29:15,130 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:29:15,219 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:29:15,850 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:29:15,850 [INFO]    âšª No signal - HOLD
2025-12-06 07:29:16,351 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:29:16,434 [INFO]    Current position: LONG 0.69
2025-12-06 07:29:16,435 [INFO]    Entry: $145.48 | Mark: $132.79
2025-12-06 07:29:16,435 [INFO]    PnL: -87.24% ($-8.76)
2025-12-06 07:29:16,435 [INFO]    Age: 53.9h / 72.0h
2025-12-06 07:29:16,935 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:29:17,030 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:29:17,646 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:29:17,646 [INFO]    âšª No signal - HOLD
2025-12-06 07:29:18,147 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:29:18,232 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:29:18,839 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:29:18,840 [INFO]    âšª No signal - HOLD
2025-12-06 07:29:19,340 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:29:19,422 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:29:20,363 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 10/15
2025-12-06 07:29:20,363 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:29:20,363 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:29:20,363 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:29:20,363 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:29:20,364 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:29:20,364 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:29:20,369 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:29:20,369 [INFO]    âšª No signal - HOLD
2025-12-06 07:29:20,870 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:29:20,953 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:29:21,742 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 07:29:21,742 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:29:21,742 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:29:21,743 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:29:21,743 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:29:21,743 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:29:21,747 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:29:21,747 [INFO]    âšª No signal - HOLD
2025-12-06 07:29:21,747 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:32:21,834 [INFO] 
============================================================
2025-12-06 07:32:21,834 [INFO] ðŸ”„ LOOP #9 - 2025-12-06 07:32:21
2025-12-06 07:32:21,834 [INFO] ============================================================
2025-12-06 07:32:21,928 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:32:21,928 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:32:22,020 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:32:22,675 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:32:22,675 [INFO]    âšª No signal - HOLD
2025-12-06 07:32:23,176 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:32:23,265 [INFO]    Current position: LONG 0.11
2025-12-06 07:32:23,265 [INFO]    Entry: $924.70 | Mark: $883.63
2025-12-06 07:32:23,265 [INFO]    PnL: -44.41% ($-4.52)
2025-12-06 07:32:23,265 [INFO]    Age: 53.1h / 72.0h
2025-12-06 07:32:23,766 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:32:23,862 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:32:24,525 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 10/15
2025-12-06 07:32:24,525 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:32:24,525 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:32:24,525 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:32:24,525 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:32:24,525 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:32:24,525 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:32:24,536 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:32:24,536 [INFO]    âšª No signal - HOLD
2025-12-06 07:32:25,037 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:32:25,129 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:32:25,809 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 10/15
2025-12-06 07:32:25,809 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 07:32:25,810 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:32:25,810 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:32:25,810 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:32:25,810 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:32:25,810 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:32:25,814 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:32:25,815 [INFO]    âšª No signal - HOLD
2025-12-06 07:32:26,315 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:32:26,404 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:32:27,063 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:32:27,063 [INFO]    âšª No signal - HOLD
2025-12-06 07:32:27,564 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:32:27,650 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:32:28,312 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:32:28,312 [INFO]    âšª No signal - HOLD
2025-12-06 07:32:28,813 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:32:28,904 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:32:29,672 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:32:29,672 [INFO]    âšª No signal - HOLD
2025-12-06 07:32:30,173 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:32:30,258 [INFO]    Current position: LONG 0.69
2025-12-06 07:32:30,258 [INFO]    Entry: $145.48 | Mark: $132.65
2025-12-06 07:32:30,258 [INFO]    PnL: -88.23% ($-8.86)
2025-12-06 07:32:30,258 [INFO]    Age: 53.9h / 72.0h
2025-12-06 07:32:30,759 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:32:30,851 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:32:31,532 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:32:31,533 [INFO]    âšª No signal - HOLD
2025-12-06 07:32:32,033 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:32:32,119 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:32:32,770 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 9/15
2025-12-06 07:32:32,771 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:32:32,771 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:32:32,771 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:32:32,771 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:32:32,771 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:32:32,776 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:32:32,776 [INFO]    âšª No signal - HOLD
2025-12-06 07:32:33,277 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:32:33,365 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:32:34,036 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:32:34,036 [INFO]    âšª No signal - HOLD
2025-12-06 07:32:34,537 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:32:34,624 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:32:35,306 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 07:32:35,307 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:32:35,307 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:32:35,307 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:32:35,307 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:32:35,307 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:32:35,312 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:32:35,312 [INFO]    âšª No signal - HOLD
2025-12-06 07:32:35,313 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:35:35,404 [INFO] 
============================================================
2025-12-06 07:35:35,404 [INFO] ðŸ”„ LOOP #10 - 2025-12-06 07:35:35
2025-12-06 07:35:35,404 [INFO] ============================================================
2025-12-06 07:35:36,419 [INFO] ðŸ’“ Bot alive - Loop #10 - Active positions: 2
2025-12-06 07:35:36,504 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:35:36,504 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:35:36,589 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:35:37,288 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:35:37,288 [INFO]    âšª No signal - HOLD
2025-12-06 07:35:37,789 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:35:37,877 [INFO]    Current position: LONG 0.11
2025-12-06 07:35:37,878 [INFO]    Entry: $924.70 | Mark: $883.91
2025-12-06 07:35:37,878 [INFO]    PnL: -44.11% ($-4.49)
2025-12-06 07:35:37,878 [INFO]    Age: 53.1h / 72.0h
2025-12-06 07:35:38,378 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:35:38,465 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:35:39,104 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 11/15
2025-12-06 07:35:39,104 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:35:39,104 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:35:39,104 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:35:39,104 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:35:39,104 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:35:39,104 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:35:39,109 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:35:39,110 [INFO]    âšª No signal - HOLD
2025-12-06 07:35:39,610 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:35:39,694 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:35:40,351 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 10/15
2025-12-06 07:35:40,352 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 07:35:40,352 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:35:40,352 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:35:40,352 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:35:40,352 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:35:40,352 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:35:40,358 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:35:40,358 [INFO]    âšª No signal - HOLD
2025-12-06 07:35:40,859 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:35:40,944 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:35:41,608 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:35:41,608 [INFO]    âšª No signal - HOLD
2025-12-06 07:35:42,109 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:35:42,192 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:35:42,873 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:35:42,873 [INFO]    âšª No signal - HOLD
2025-12-06 07:35:43,374 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:35:43,592 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:35:44,217 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:35:44,217 [INFO]    âšª No signal - HOLD
2025-12-06 07:35:44,718 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:35:44,806 [INFO]    Current position: LONG 0.69
2025-12-06 07:35:44,806 [INFO]    Entry: $145.48 | Mark: $132.82
2025-12-06 07:35:44,806 [INFO]    PnL: -87.02% ($-8.74)
2025-12-06 07:35:44,806 [INFO]    Age: 54.0h / 72.0h
2025-12-06 07:35:45,307 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:35:45,391 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:35:46,010 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:35:46,010 [INFO]    âšª No signal - HOLD
2025-12-06 07:35:46,511 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:35:46,599 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:35:47,272 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 9/15
2025-12-06 07:35:47,272 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:35:47,272 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:35:47,273 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:35:47,273 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:35:47,273 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:35:47,277 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:35:47,277 [INFO]    âšª No signal - HOLD
2025-12-06 07:35:47,778 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:35:47,863 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:35:48,664 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 9/15
2025-12-06 07:35:48,664 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:35:48,664 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:35:48,665 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:35:48,665 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:35:48,665 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:35:48,669 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:35:48,669 [INFO]    âšª No signal - HOLD
2025-12-06 07:35:49,170 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:35:49,257 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:35:50,191 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 07:35:50,191 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:35:50,191 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:35:50,191 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:35:50,191 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:35:50,191 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:35:50,196 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:35:50,196 [INFO]    âšª No signal - HOLD
2025-12-06 07:35:51,745 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:38:51,805 [INFO] 
============================================================
2025-12-06 07:38:51,806 [INFO] ðŸ”„ LOOP #11 - 2025-12-06 07:38:51
2025-12-06 07:38:51,806 [INFO] ============================================================
2025-12-06 07:38:51,891 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:38:51,891 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:38:51,973 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:38:52,645 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:38:52,646 [INFO]    âšª No signal - HOLD
2025-12-06 07:38:53,146 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:38:53,232 [INFO]    Current position: LONG 0.11
2025-12-06 07:38:53,232 [INFO]    Entry: $924.70 | Mark: $884.15
2025-12-06 07:38:53,233 [INFO]    PnL: -43.85% ($-4.46)
2025-12-06 07:38:53,233 [INFO]    Age: 53.2h / 72.0h
2025-12-06 07:38:53,733 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:38:53,818 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:38:54,509 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 11/15
2025-12-06 07:38:54,510 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:38:54,510 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:38:54,510 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:38:54,510 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:38:54,510 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:38:54,510 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:38:54,515 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:38:54,516 [INFO]    âšª No signal - HOLD
2025-12-06 07:38:55,016 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:38:55,100 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:38:55,776 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 10/15
2025-12-06 07:38:55,776 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 07:38:55,776 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:38:55,776 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:38:55,777 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:38:55,777 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:38:55,777 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:38:55,782 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:38:55,782 [INFO]    âšª No signal - HOLD
2025-12-06 07:38:56,283 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:38:56,371 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:38:57,055 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:38:57,056 [INFO]    âšª No signal - HOLD
2025-12-06 07:38:57,557 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:38:57,642 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:38:58,295 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:38:58,295 [INFO]    âšª No signal - HOLD
2025-12-06 07:38:58,796 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:38:58,880 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:38:59,590 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:38:59,591 [INFO]    âšª No signal - HOLD
2025-12-06 07:39:00,091 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:39:00,175 [INFO]    Current position: LONG 0.69
2025-12-06 07:39:00,175 [INFO]    Entry: $145.48 | Mark: $132.82
2025-12-06 07:39:00,175 [INFO]    PnL: -86.99% ($-8.73)
2025-12-06 07:39:00,175 [INFO]    Age: 54.0h / 72.0h
2025-12-06 07:39:00,676 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:39:00,762 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:39:01,564 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:39:01,565 [INFO]    âšª No signal - HOLD
2025-12-06 07:39:02,065 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:39:02,154 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:39:02,822 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 9/15
2025-12-06 07:39:02,822 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:39:02,822 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:39:02,822 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:39:02,822 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:39:02,822 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:39:02,828 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:39:02,829 [INFO]    âšª No signal - HOLD
2025-12-06 07:39:03,330 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:39:03,415 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:39:04,074 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 9/15
2025-12-06 07:39:04,075 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:39:04,075 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:39:04,075 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:39:04,075 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:39:04,075 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:39:04,080 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:39:04,081 [INFO]    âšª No signal - HOLD
2025-12-06 07:39:04,581 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:39:04,668 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:39:05,370 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 10/15
2025-12-06 07:39:05,370 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:39:05,370 [INFO]    âš ï¸ Near EMA21
2025-12-06 07:39:05,370 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:39:05,370 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:39:05,370 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:39:05,371 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:39:05,377 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:39:05,377 [INFO]    âšª No signal - HOLD
2025-12-06 07:39:05,378 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:41:46,222 [INFO] 
ðŸ›‘ Shutdown signal received...
2025-12-06 07:42:05,397 [INFO] 
============================================================
2025-12-06 07:42:05,397 [INFO] ðŸ›‘ SHUTTING DOWN BOT
2025-12-06 07:42:05,398 [INFO] ============================================================
2025-12-06 07:42:05,398 [INFO] ðŸ“Š <b>DAILY STATS</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
Trades: 0
Volume: $0.00M
PnL: 0.00%

<b>Overall</b>
Total Trades: 0
Win Rate: 0.0%
W/L: 0/0
2025-12-06 07:42:06,147 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-12-06 07:42:06,149 [INFO] ðŸ‘‹ Bot stopped!
2025-12-06 07:42:06,523 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
âœ… Using fixed position size: $10.0 USDT per trade
âœ… Config validation passed!
2025-12-06 07:42:09,734 [INFO] âœ… Telegram bot initialized
2025-12-06 07:42:19,215 [INFO] ============================================================
2025-12-06 07:42:19,216 [INFO] ðŸš€ ASTERDEX PERP FARM BOT - INITIALIZING
2025-12-06 07:42:19,217 [INFO] ============================================================
2025-12-06 07:42:19,381 [INFO] ðŸ”Œ AsterDEX Client initialized (MAINNET)
2025-12-06 07:42:19,381 [INFO]    URL: https://fapi.asterdex.com/fapi
2025-12-06 07:42:19,382 [INFO] ðŸ“‚ Loaded 2 position timestamps
2025-12-06 07:42:19,382 [INFO] ðŸ“ˆ Trailing Stop enabled (PnL-based): Activation=2.5% PnL, Trail=2.2% PnL
2025-12-06 07:42:19,382 [INFO] ðŸŽ­ Loading Ensemble models...
2025-12-06 07:42:19,387 [INFO] ðŸ’¡ LightGBM Trainer initialized with 23 features
2025-12-06 07:42:19,388 [INFO] ðŸ± CatBoost Trainer initialized with 23 features
2025-12-06 07:42:19,388 [INFO] ðŸŽ­ Ensemble initialized with 3 models
2025-12-06 07:42:19,388 [INFO]    Models: ['xgboost', 'lightgbm', 'catboost']
2025-12-06 07:42:19,390 [INFO]    Weights: [0.4  0.35 0.25]
2025-12-06 07:42:19,484 [INFO] âœ… XGBoost model loaded from models/xgboost_model.json
2025-12-06 07:42:19,485 [INFO] âœ… XGBoost loaded
2025-12-06 07:42:19,520 [INFO] âœ… LightGBM loaded from models/lightgbm_model.txt
2025-12-06 07:42:19,521 [INFO] âœ… LightGBM loaded
2025-12-06 07:42:19,528 [INFO] âœ… CatBoost loaded from models/catboost_model.cbm
2025-12-06 07:42:19,529 [INFO] âœ… CatBoost loaded
2025-12-06 07:42:19,529 [INFO] âœ… Ensemble loaded: 3/3 models
2025-12-06 07:42:19,529 [INFO] ðŸŽ­ Using Ensemble predictor: ['xgboost', 'lightgbm', 'catboost']
2025-12-06 07:42:19,529 [INFO]    Weights: [0.4, 0.35, 0.25]
2025-12-06 07:42:19,529 [INFO] ðŸŽ¯ SmartEntrySystemV2 enabled (min score: 6, min R:R: 0.0:1)
2025-12-06 07:42:19,530 [INFO] ðŸš« Signal Cooldown enabled: 60m signal, 15m post-trade
2025-12-06 07:42:19,530 [INFO] ðŸŽ¯ Entry Quality Checker enabled
2025-12-06 07:42:19,530 [INFO] ðŸŽ­ Entry Pipeline received 3 ML models: ['xgboost', 'lightgbm', 'catboost']
2025-12-06 07:42:19,530 [INFO] ðŸŽ­ MLEnsembleSignal initialized
2025-12-06 07:42:19,530 [INFO]    Models: ['xgboost', 'lightgbm', 'catboost']
2025-12-06 07:42:19,530 [INFO]    Weights: {'xgboost': 0.4, 'lightgbm': 0.35, 'catboost': 0.25}
2025-12-06 07:42:19,530 [INFO]    Confidence threshold: 0.65
2025-12-06 07:42:19,530 [INFO] ðŸŽ¯ SmartEntryScoring initialized (min score: 6)
2025-12-06 07:42:19,531 [INFO] ðŸŽ¨ PriceActionValidator initialized (min score: 6/8)
2025-12-06 07:42:19,531 [INFO] ðŸ“ˆ HTFTrendAligner initialized (TF: 4h)
2025-12-06 07:42:19,608 [INFO] ðŸ¤– AIEntryAnalyzer initialized (provider: claude)
2025-12-06 07:42:19,608 [INFO] ðŸš€ EntryPipeline initialized
2025-12-06 07:42:19,609 [INFO]    Stages enabled: ML=True, SmartEntry=True, PA=True, HTF=True, AI=True
2025-12-06 07:42:19,609 [INFO] ðŸš€ Entry Pipeline enabled (5-stage validation)
2025-12-06 07:42:19,609 [INFO] âœ… Bot initialized successfully!
2025-12-06 07:42:19,609 [INFO]    Symbols: ['ADAUSDT', 'BNBUSDT', 'DOGEUSDT', 'UNIUSDT', 'LINKUSDT', 'BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'XRPUSDT', 'DOTUSDT', 'AVAXUSDT', 'NEARUSDT']
2025-12-06 07:42:19,609 [INFO]    Leverage: 10x
2025-12-06 07:42:19,609 [INFO]    Position Size: 20.0%
2025-12-06 07:42:19,609 [INFO]    TP/SL: 10.00% / Disabled
2025-12-06 07:42:19,609 [INFO]    Position Timeout: 72.0h
2025-12-06 07:42:19,609 [INFO]    ðŸ“Š Timeframe: PRIMARY=1h, HIGHER=4h
2025-12-06 07:42:19,609 [INFO]    ðŸ”„ Loop Sleep: 180s
2025-12-06 07:42:19,609 [INFO] ============================================================
2025-12-06 07:42:19,609 [INFO] ðŸ BOT STARTED!
2025-12-06 07:42:20,323 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-12-06 07:42:20,502 [INFO] ðŸ“Š Daily start balance: $29.10
2025-12-06 07:42:20,502 [INFO] ðŸ’° Starting balance: $29.10
2025-12-06 07:42:20,868 [INFO] HTTP Request: POST https://api.telegram.org/bot8291644636:AAFoVcH-LQdjcWlIdcdYV8oa067WxVQk2Ko/sendMessage "HTTP/1.1 200 OK"
2025-12-06 07:42:20,869 [INFO] 
============================================================
2025-12-06 07:42:20,871 [INFO] ðŸ”„ LOOP #1 - 2025-12-06 07:42:20
2025-12-06 07:42:20,871 [INFO] ============================================================
2025-12-06 07:42:20,960 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:42:20,960 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:42:21,046 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:42:21,790 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:42:21,790 [INFO]    âšª No signal - HOLD
2025-12-06 07:42:22,291 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:42:22,376 [INFO]    Current position: LONG 0.11
2025-12-06 07:42:22,377 [INFO]    Entry: $924.70 | Mark: $885.24
2025-12-06 07:42:22,377 [INFO]    PnL: -42.67% ($-4.34)
2025-12-06 07:42:22,377 [INFO]    Age: 53.2h / 72.0h
2025-12-06 07:42:22,878 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:42:22,962 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:42:23,632 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:42:23,632 [INFO]    âšª No signal - HOLD
2025-12-06 07:42:24,133 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:42:24,218 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:42:24,882 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 10/15
2025-12-06 07:42:24,882 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 07:42:24,882 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:42:24,882 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:42:24,882 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:42:24,882 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:42:24,882 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:42:24,898 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:42:24,898 [INFO]    âšª No signal - HOLD
2025-12-06 07:42:25,399 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:42:25,483 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:42:26,140 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:42:26,141 [INFO]    âšª No signal - HOLD
2025-12-06 07:42:26,641 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:42:26,725 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:42:27,361 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:42:27,362 [INFO]    âšª No signal - HOLD
2025-12-06 07:42:27,862 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:42:27,949 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:42:28,593 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:42:28,593 [INFO]    âšª No signal - HOLD
2025-12-06 07:42:29,094 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:42:29,186 [INFO]    Current position: LONG 0.69
2025-12-06 07:42:29,186 [INFO]    Entry: $145.48 | Mark: $132.93
2025-12-06 07:42:29,186 [INFO]    PnL: -86.26% ($-8.66)
2025-12-06 07:42:29,186 [INFO]    Age: 54.1h / 72.0h
2025-12-06 07:42:29,687 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:42:29,768 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:42:30,401 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:42:30,401 [INFO]    âšª No signal - HOLD
2025-12-06 07:42:30,902 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:42:30,988 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:42:31,848 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:42:31,848 [INFO]    âšª No signal - HOLD
2025-12-06 07:42:32,349 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:42:32,439 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:42:33,086 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 9/15
2025-12-06 07:42:33,086 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:42:33,086 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:42:33,087 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:42:33,087 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:42:33,087 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:42:33,098 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:42:33,098 [INFO]    âšª No signal - HOLD
2025-12-06 07:42:33,599 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:42:33,684 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:42:34,351 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 10/15
2025-12-06 07:42:34,351 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:42:34,351 [INFO]    âš ï¸ Near EMA21
2025-12-06 07:42:34,351 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:42:34,351 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:42:34,351 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:42:34,351 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:42:34,361 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:42:34,361 [INFO]    âšª No signal - HOLD
2025-12-06 07:42:34,362 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:45:34,452 [INFO] 
============================================================
2025-12-06 07:45:34,453 [INFO] ðŸ”„ LOOP #2 - 2025-12-06 07:45:34
2025-12-06 07:45:34,453 [INFO] ============================================================
2025-12-06 07:45:34,541 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:45:34,541 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:45:34,627 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:45:35,300 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:45:35,300 [INFO]    âšª No signal - HOLD
2025-12-06 07:45:35,801 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:45:35,892 [INFO]    Current position: LONG 0.11
2025-12-06 07:45:35,892 [INFO]    Entry: $924.70 | Mark: $885.43
2025-12-06 07:45:35,892 [INFO]    PnL: -42.46% ($-4.32)
2025-12-06 07:45:35,892 [INFO]    Age: 53.3h / 72.0h
2025-12-06 07:45:36,393 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:45:36,486 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:45:37,163 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 10/15
2025-12-06 07:45:37,163 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:45:37,163 [INFO]    âš ï¸ Near EMA21
2025-12-06 07:45:37,163 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:45:37,164 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:45:37,164 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:45:37,164 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:45:37,177 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:45:37,177 [INFO]    âšª No signal - HOLD
2025-12-06 07:45:37,677 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:45:37,763 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:45:38,413 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 11/15
2025-12-06 07:45:38,413 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:45:38,414 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:45:38,414 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:45:38,414 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:45:38,414 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:45:38,414 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:45:38,419 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:45:38,419 [INFO]    âšª No signal - HOLD
2025-12-06 07:45:38,920 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:45:39,001 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:45:39,643 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:45:39,644 [INFO]    âšª No signal - HOLD
2025-12-06 07:45:40,144 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:45:40,229 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:45:40,908 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:45:40,908 [INFO]    âšª No signal - HOLD
2025-12-06 07:45:41,409 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:45:41,493 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:45:42,155 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:45:42,156 [INFO]    âšª No signal - HOLD
2025-12-06 07:45:42,656 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:45:42,743 [INFO]    Current position: LONG 0.69
2025-12-06 07:45:42,743 [INFO]    Entry: $145.48 | Mark: $132.91
2025-12-06 07:45:42,743 [INFO]    PnL: -86.44% ($-8.68)
2025-12-06 07:45:42,744 [INFO]    Age: 54.2h / 72.0h
2025-12-06 07:45:43,244 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:45:43,331 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:45:44,004 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:45:44,005 [INFO]    âšª No signal - HOLD
2025-12-06 07:45:44,506 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:45:44,593 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:45:45,287 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 10/15
2025-12-06 07:45:45,287 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:45:45,287 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:45:45,287 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:45:45,288 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:45:45,288 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:45:45,288 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:45:45,297 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:45:45,298 [INFO]    âšª No signal - HOLD
2025-12-06 07:45:45,799 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:45:45,883 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:45:46,660 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 10/15
2025-12-06 07:45:46,661 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:45:46,661 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:45:46,661 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:45:46,661 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:45:46,661 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:45:46,661 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:45:46,666 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:45:46,666 [INFO]    âšª No signal - HOLD
2025-12-06 07:45:47,167 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:45:47,389 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:45:48,215 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 8/15
2025-12-06 07:45:48,215 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:45:48,216 [INFO]    âš ï¸ Near EMA21
2025-12-06 07:45:48,216 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:45:48,216 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:45:48,216 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:45:48,243 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:45:48,243 [INFO]    âšª No signal - HOLD
2025-12-06 07:45:48,243 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:48:48,269 [INFO] 
============================================================
2025-12-06 07:48:48,270 [INFO] ðŸ”„ LOOP #3 - 2025-12-06 07:48:48
2025-12-06 07:48:48,270 [INFO] ============================================================
2025-12-06 07:48:48,354 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:48:48,354 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:48:48,435 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:48:49,083 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:48:49,084 [INFO]    âšª No signal - HOLD
2025-12-06 07:48:49,584 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:48:49,671 [INFO]    Current position: LONG 0.11
2025-12-06 07:48:49,671 [INFO]    Entry: $924.70 | Mark: $885.97
2025-12-06 07:48:49,671 [INFO]    PnL: -41.88% ($-4.26)
2025-12-06 07:48:49,671 [INFO]    Age: 53.4h / 72.0h
2025-12-06 07:48:50,172 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:48:50,256 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:48:50,907 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 10/15
2025-12-06 07:48:50,907 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:48:50,907 [INFO]    âš ï¸ Near EMA21
2025-12-06 07:48:50,907 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:48:50,907 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:48:50,908 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:48:50,908 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:48:50,913 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:48:50,913 [INFO]    âšª No signal - HOLD
2025-12-06 07:48:51,414 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:48:51,498 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:48:52,173 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 11/15
2025-12-06 07:48:52,173 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:48:52,173 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:48:52,173 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:48:52,173 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:48:52,173 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:48:52,173 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:48:52,178 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:48:52,178 [INFO]    âšª No signal - HOLD
2025-12-06 07:48:52,679 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:48:52,764 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:48:53,435 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:48:53,436 [INFO]    âšª No signal - HOLD
2025-12-06 07:48:53,936 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:48:54,023 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:48:54,683 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:48:54,683 [INFO]    âšª No signal - HOLD
2025-12-06 07:48:55,184 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:48:55,264 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:48:55,956 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:48:55,956 [INFO]    âšª No signal - HOLD
2025-12-06 07:48:56,457 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:48:56,542 [INFO]    Current position: LONG 0.69
2025-12-06 07:48:56,542 [INFO]    Entry: $145.48 | Mark: $132.92
2025-12-06 07:48:56,542 [INFO]    PnL: -86.36% ($-8.67)
2025-12-06 07:48:56,542 [INFO]    Age: 54.2h / 72.0h
2025-12-06 07:48:57,043 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:48:57,127 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:48:57,767 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:48:57,767 [INFO]    âšª No signal - HOLD
2025-12-06 07:48:58,268 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:48:58,349 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:48:58,995 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 10/15
2025-12-06 07:48:58,995 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:48:58,995 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:48:58,995 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:48:58,995 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:48:58,995 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:48:58,995 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:48:59,000 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:48:59,001 [INFO]    âšª No signal - HOLD
2025-12-06 07:48:59,502 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:48:59,585 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:49:00,258 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 10/15
2025-12-06 07:49:00,259 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:49:00,259 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:49:00,259 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:49:00,259 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:49:00,259 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:49:00,259 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:49:00,264 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:49:00,264 [INFO]    âšª No signal - HOLD
2025-12-06 07:49:00,765 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:49:00,847 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:49:01,499 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 8/15
2025-12-06 07:49:01,500 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:49:01,500 [INFO]    âš ï¸ Near EMA21
2025-12-06 07:49:01,500 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:49:01,500 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:49:01,500 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:49:01,504 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:49:01,505 [INFO]    âšª No signal - HOLD
2025-12-06 07:49:01,505 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:52:01,607 [INFO] 
============================================================
2025-12-06 07:52:01,607 [INFO] ðŸ”„ LOOP #4 - 2025-12-06 07:52:01
2025-12-06 07:52:01,607 [INFO] ============================================================
2025-12-06 07:52:01,700 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:52:01,700 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:52:01,785 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:52:02,471 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:52:02,471 [INFO]    âšª No signal - HOLD
2025-12-06 07:52:02,972 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:52:03,062 [INFO]    Current position: LONG 0.11
2025-12-06 07:52:03,062 [INFO]    Entry: $924.70 | Mark: $885.25
2025-12-06 07:52:03,062 [INFO]    PnL: -42.66% ($-4.34)
2025-12-06 07:52:03,062 [INFO]    Age: 53.4h / 72.0h
2025-12-06 07:52:03,563 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:52:03,649 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:52:04,301 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 11/15
2025-12-06 07:52:04,302 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:52:04,302 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:52:04,302 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:52:04,302 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:52:04,302 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:52:04,302 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:52:04,306 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:52:04,306 [INFO]    âšª No signal - HOLD
2025-12-06 07:52:04,807 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:52:04,891 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:52:05,527 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 11/15
2025-12-06 07:52:05,527 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:52:05,527 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:52:05,527 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:52:05,527 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:52:05,527 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:52:05,527 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:52:05,532 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:52:05,532 [INFO]    âšª No signal - HOLD
2025-12-06 07:52:06,033 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:52:06,124 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:52:06,797 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:52:06,797 [INFO]    âšª No signal - HOLD
2025-12-06 07:52:07,297 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:52:07,387 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:52:08,066 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:52:08,066 [INFO]    âšª No signal - HOLD
2025-12-06 07:52:08,567 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:52:08,653 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:52:09,304 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:52:09,304 [INFO]    âšª No signal - HOLD
2025-12-06 07:52:09,805 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:52:09,893 [INFO]    Current position: LONG 0.69
2025-12-06 07:52:09,894 [INFO]    Entry: $145.48 | Mark: $132.80
2025-12-06 07:52:09,894 [INFO]    PnL: -87.17% ($-8.75)
2025-12-06 07:52:09,894 [INFO]    Age: 54.3h / 72.0h
2025-12-06 07:52:10,395 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:52:10,481 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:52:11,179 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:52:11,179 [INFO]    âšª No signal - HOLD
2025-12-06 07:52:11,680 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:52:11,767 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:52:12,441 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 10/15
2025-12-06 07:52:12,441 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:52:12,441 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:52:12,441 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:52:12,441 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:52:12,441 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:52:12,442 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:52:12,446 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:52:12,447 [INFO]    âšª No signal - HOLD
2025-12-06 07:52:12,947 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:52:13,036 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:52:13,821 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 10/15
2025-12-06 07:52:13,822 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:52:13,822 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:52:13,822 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:52:13,822 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:52:13,822 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:52:13,822 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:52:13,828 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:52:13,828 [INFO]    âšª No signal - HOLD
2025-12-06 07:52:14,329 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:52:14,416 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:52:15,050 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 8/15
2025-12-06 07:52:15,051 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:52:15,051 [INFO]    âš ï¸ Near EMA21
2025-12-06 07:52:15,051 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:52:15,051 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:52:15,051 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:52:15,056 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:52:15,056 [INFO]    âšª No signal - HOLD
2025-12-06 07:52:15,057 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:55:15,153 [INFO] 
============================================================
2025-12-06 07:55:15,154 [INFO] ðŸ”„ LOOP #5 - 2025-12-06 07:55:15
2025-12-06 07:55:15,154 [INFO] ============================================================
2025-12-06 07:55:16,178 [INFO] ðŸ’“ Bot alive - Loop #5 - Active positions: 2
2025-12-06 07:55:16,267 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:55:16,267 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:55:16,354 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:55:17,057 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:55:17,057 [INFO]    âšª No signal - HOLD
2025-12-06 07:55:17,558 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:55:17,652 [INFO]    Current position: LONG 0.11
2025-12-06 07:55:17,652 [INFO]    Entry: $924.70 | Mark: $884.96
2025-12-06 07:55:17,652 [INFO]    PnL: -42.98% ($-4.37)
2025-12-06 07:55:17,652 [INFO]    Age: 53.5h / 72.0h
2025-12-06 07:55:18,153 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:55:18,238 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:55:18,931 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 11/15
2025-12-06 07:55:18,931 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:55:18,931 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:55:18,931 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:55:18,931 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:55:18,931 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:55:18,931 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:55:18,937 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:55:18,937 [INFO]    âšª No signal - HOLD
2025-12-06 07:55:19,438 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:55:19,657 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:55:20,327 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 11/15
2025-12-06 07:55:20,327 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:55:20,327 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:55:20,327 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:55:20,327 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:55:20,327 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:55:20,328 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:55:20,334 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:55:20,334 [INFO]    âšª No signal - HOLD
2025-12-06 07:55:20,835 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:55:20,924 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:55:21,624 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:55:21,624 [INFO]    âšª No signal - HOLD
2025-12-06 07:55:22,125 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:55:22,212 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:55:23,053 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:55:23,053 [INFO]    âšª No signal - HOLD
2025-12-06 07:55:23,554 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:55:23,642 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:55:24,318 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:55:24,319 [INFO]    âšª No signal - HOLD
2025-12-06 07:55:24,819 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:55:24,904 [INFO]    Current position: LONG 0.69
2025-12-06 07:55:24,904 [INFO]    Entry: $145.48 | Mark: $132.74
2025-12-06 07:55:24,904 [INFO]    PnL: -87.60% ($-8.79)
2025-12-06 07:55:24,904 [INFO]    Age: 54.3h / 72.0h
2025-12-06 07:55:25,405 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:55:25,490 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:55:26,298 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:55:26,299 [INFO]    âšª No signal - HOLD
2025-12-06 07:55:26,800 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:55:26,885 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:55:27,536 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 10/15
2025-12-06 07:55:27,536 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:55:27,536 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:55:27,536 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:55:27,536 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:55:27,536 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:55:27,536 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:55:27,542 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:55:27,542 [INFO]    âšª No signal - HOLD
2025-12-06 07:55:28,043 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:55:28,132 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:55:28,999 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 10/15
2025-12-06 07:55:28,999 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:55:28,999 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:55:29,000 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:55:29,000 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:55:29,000 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:55:29,000 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:55:29,004 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:55:29,005 [INFO]    âšª No signal - HOLD
2025-12-06 07:55:29,505 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:55:29,588 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:55:30,416 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 8/15
2025-12-06 07:55:30,416 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:55:30,416 [INFO]    âš ï¸ Near EMA21
2025-12-06 07:55:30,417 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:55:30,417 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:55:30,417 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:55:30,422 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:55:30,422 [INFO]    âšª No signal - HOLD
2025-12-06 07:55:30,422 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 07:58:30,486 [INFO] 
============================================================
2025-12-06 07:58:30,486 [INFO] ðŸ”„ LOOP #6 - 2025-12-06 07:58:30
2025-12-06 07:58:30,486 [INFO] ============================================================
2025-12-06 07:58:30,579 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 07:58:30,579 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 07:58:30,668 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 07:58:31,328 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:58:31,329 [INFO]    âšª No signal - HOLD
2025-12-06 07:58:31,829 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 07:58:31,915 [INFO]    Current position: LONG 0.11
2025-12-06 07:58:31,915 [INFO]    Entry: $924.70 | Mark: $884.92
2025-12-06 07:58:31,915 [INFO]    PnL: -43.02% ($-4.38)
2025-12-06 07:58:31,916 [INFO]    Age: 53.5h / 72.0h
2025-12-06 07:58:32,416 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 07:58:32,501 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 07:58:33,182 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 11/15
2025-12-06 07:58:33,182 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:58:33,182 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:58:33,182 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:58:33,182 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:58:33,182 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:58:33,182 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:58:33,188 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:58:33,188 [INFO]    âšª No signal - HOLD
2025-12-06 07:58:33,689 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 07:58:33,784 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 07:58:34,432 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 11/15
2025-12-06 07:58:34,433 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:58:34,433 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:58:34,433 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:58:34,433 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 07:58:34,433 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:58:34,433 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:58:34,439 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:58:34,439 [INFO]    âšª No signal - HOLD
2025-12-06 07:58:34,940 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 07:58:35,026 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 07:58:36,178 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:58:36,179 [INFO]    âšª No signal - HOLD
2025-12-06 07:58:36,679 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 07:58:36,777 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 07:58:37,501 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:58:37,501 [INFO]    âšª No signal - HOLD
2025-12-06 07:58:38,001 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 07:58:38,085 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 07:58:38,851 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:58:38,852 [INFO]    âšª No signal - HOLD
2025-12-06 07:58:39,352 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 07:58:39,436 [INFO]    Current position: LONG 0.69
2025-12-06 07:58:39,436 [INFO]    Entry: $145.48 | Mark: $132.70
2025-12-06 07:58:39,436 [INFO]    PnL: -87.88% ($-8.82)
2025-12-06 07:58:39,437 [INFO]    Age: 54.4h / 72.0h
2025-12-06 07:58:39,937 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 07:58:40,022 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 07:58:40,671 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:58:40,671 [INFO]    âšª No signal - HOLD
2025-12-06 07:58:41,172 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 07:58:41,257 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 07:58:41,928 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 10/15
2025-12-06 07:58:41,928 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:58:41,928 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:58:41,928 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:58:41,928 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:58:41,928 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:58:41,928 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:58:41,934 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:58:41,934 [INFO]    âšª No signal - HOLD
2025-12-06 07:58:42,435 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 07:58:42,526 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 07:58:43,353 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 10/15
2025-12-06 07:58:43,353 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:58:43,353 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 07:58:43,353 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:58:43,353 [INFO]    âš¡ RSI acceptable range
2025-12-06 07:58:43,353 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:58:43,353 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:58:43,359 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:58:43,360 [INFO]    âšª No signal - HOLD
2025-12-06 07:58:43,861 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 07:58:44,081 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 07:58:44,807 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 8/15
2025-12-06 07:58:44,807 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 07:58:44,807 [INFO]    âš ï¸ Near EMA21
2025-12-06 07:58:44,807 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 07:58:44,807 [INFO]    ðŸ’¤ Off-peak hours
2025-12-06 07:58:44,807 [INFO]    âœ… R:R = 2.0:1
2025-12-06 07:58:44,813 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 07:58:44,813 [INFO]    âšª No signal - HOLD
2025-12-06 07:58:44,814 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:01:44,901 [INFO] 
============================================================
2025-12-06 08:01:44,902 [INFO] ðŸ”„ LOOP #7 - 2025-12-06 08:01:44
2025-12-06 08:01:44,902 [INFO] ============================================================
2025-12-06 08:01:44,993 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:01:44,993 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:01:45,081 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:01:45,792 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:01:45,792 [INFO]    âšª No signal - HOLD
2025-12-06 08:01:46,293 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:01:46,381 [INFO]    Current position: LONG 0.11
2025-12-06 08:01:46,382 [INFO]    Entry: $924.70 | Mark: $883.86
2025-12-06 08:01:46,382 [INFO]    PnL: -44.17% ($-4.49)
2025-12-06 08:01:46,382 [INFO]    Age: 53.6h / 72.0h
2025-12-06 08:01:46,882 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:01:46,970 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:01:47,640 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 13/15
2025-12-06 08:01:47,640 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:01:47,640 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:01:47,640 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:01:47,640 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 08:01:47,641 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:01:47,641 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:01:47,650 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:01:47,651 [INFO]    âšª No signal - HOLD
2025-12-06 08:01:48,151 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:01:48,239 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:01:48,865 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:01:48,865 [INFO]    âšª No signal - HOLD
2025-12-06 08:01:49,366 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:01:49,452 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:01:50,102 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:01:50,103 [INFO]    âšª No signal - HOLD
2025-12-06 08:01:50,603 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:01:50,692 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:01:51,484 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:01:51,485 [INFO]    âšª No signal - HOLD
2025-12-06 08:01:51,985 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:01:52,074 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:01:52,743 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:01:52,744 [INFO]    âšª No signal - HOLD
2025-12-06 08:01:53,244 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:01:53,330 [INFO]    Current position: LONG 0.69
2025-12-06 08:01:53,330 [INFO]    Entry: $145.48 | Mark: $132.62
2025-12-06 08:01:53,330 [INFO]    PnL: -88.43% ($-8.88)
2025-12-06 08:01:53,330 [INFO]    Age: 54.4h / 72.0h
2025-12-06 08:01:53,831 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:01:53,918 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:01:54,588 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:01:54,589 [INFO]    âšª No signal - HOLD
2025-12-06 08:01:55,089 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:01:55,177 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:01:55,956 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:01:55,957 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:01:55,957 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:01:55,957 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:01:55,957 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:01:55,957 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:01:55,957 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:01:55,962 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:01:55,963 [INFO]    âšª No signal - HOLD
2025-12-06 08:01:56,464 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:01:56,549 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:01:57,239 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 13/15
2025-12-06 08:01:57,239 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:01:57,239 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:01:57,239 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:01:57,239 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 08:01:57,239 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:01:57,239 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:01:57,245 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:01:57,245 [INFO]    âšª No signal - HOLD
2025-12-06 08:01:57,746 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:01:57,832 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:01:58,628 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 10/15
2025-12-06 08:01:58,629 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:01:58,629 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:01:58,629 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:01:58,629 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:01:58,629 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:01:58,634 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:01:58,635 [INFO]    âšª No signal - HOLD
2025-12-06 08:01:58,635 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:04:58,724 [INFO] 
============================================================
2025-12-06 08:04:58,724 [INFO] ðŸ”„ LOOP #8 - 2025-12-06 08:04:58
2025-12-06 08:04:58,725 [INFO] ============================================================
2025-12-06 08:04:58,816 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:04:58,816 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:04:58,902 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:04:59,559 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:04:59,560 [INFO]    âšª No signal - HOLD
2025-12-06 08:05:00,060 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:05:00,143 [INFO]    Current position: LONG 0.11
2025-12-06 08:05:00,143 [INFO]    Entry: $924.70 | Mark: $883.43
2025-12-06 08:05:00,143 [INFO]    PnL: -44.63% ($-4.54)
2025-12-06 08:05:00,143 [INFO]    Age: 53.6h / 72.0h
2025-12-06 08:05:00,644 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:05:00,728 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:05:01,654 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 13/15
2025-12-06 08:05:01,654 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:05:01,654 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:05:01,654 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:05:01,655 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 08:05:01,655 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:05:01,655 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:05:01,660 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:05:01,660 [INFO]    âšª No signal - HOLD
2025-12-06 08:05:02,161 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:05:02,252 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:05:02,951 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:05:02,952 [INFO]    âšª No signal - HOLD
2025-12-06 08:05:03,452 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:05:03,537 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:05:04,196 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:05:04,196 [INFO]    âšª No signal - HOLD
2025-12-06 08:05:04,697 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:05:04,785 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:05:05,499 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:05:05,499 [INFO]    âšª No signal - HOLD
2025-12-06 08:05:06,000 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:05:06,085 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:05:06,783 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:05:06,784 [INFO]    âšª No signal - HOLD
2025-12-06 08:05:07,285 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:05:07,368 [INFO]    Current position: LONG 0.69
2025-12-06 08:05:07,368 [INFO]    Entry: $145.48 | Mark: $132.64
2025-12-06 08:05:07,368 [INFO]    PnL: -88.26% ($-8.86)
2025-12-06 08:05:07,368 [INFO]    Age: 54.5h / 72.0h
2025-12-06 08:05:07,869 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:05:07,957 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:05:08,643 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:05:08,643 [INFO]    âšª No signal - HOLD
2025-12-06 08:05:09,144 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:05:09,230 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:05:09,872 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:05:09,872 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:05:09,873 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:05:09,873 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:05:09,873 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:05:09,873 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:05:09,873 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:05:09,878 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:05:09,878 [INFO]    âšª No signal - HOLD
2025-12-06 08:05:10,379 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:05:10,463 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:05:11,175 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 13/15
2025-12-06 08:05:11,175 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:05:11,175 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:05:11,176 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:05:11,176 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 08:05:11,176 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:05:11,176 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:05:11,182 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:05:11,183 [INFO]    âšª No signal - HOLD
2025-12-06 08:05:11,685 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:05:11,767 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:05:12,439 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 10/15
2025-12-06 08:05:12,439 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:05:12,439 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:05:12,439 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:05:12,439 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:05:12,439 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:05:12,445 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:05:12,445 [INFO]    âšª No signal - HOLD
2025-12-06 08:05:12,445 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:08:12,482 [INFO] 
============================================================
2025-12-06 08:08:12,482 [INFO] ðŸ”„ LOOP #9 - 2025-12-06 08:08:12
2025-12-06 08:08:12,482 [INFO] ============================================================
2025-12-06 08:08:12,568 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:08:12,569 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:08:12,658 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:08:13,326 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:08:13,326 [INFO]    âšª No signal - HOLD
2025-12-06 08:08:13,827 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:08:13,911 [INFO]    Current position: LONG 0.11
2025-12-06 08:08:13,911 [INFO]    Entry: $924.70 | Mark: $883.10
2025-12-06 08:08:13,911 [INFO]    PnL: -44.99% ($-4.58)
2025-12-06 08:08:13,912 [INFO]    Age: 53.7h / 72.0h
2025-12-06 08:08:14,412 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:08:14,498 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:08:15,205 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 13/15
2025-12-06 08:08:15,206 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:08:15,206 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:08:15,206 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:08:15,206 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 08:08:15,206 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:08:15,206 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:08:15,211 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:08:15,212 [INFO]    âšª No signal - HOLD
2025-12-06 08:08:15,713 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:08:15,796 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:08:16,460 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:08:16,460 [INFO]    âšª No signal - HOLD
2025-12-06 08:08:16,961 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:08:17,044 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:08:17,697 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:08:17,698 [INFO]    âšª No signal - HOLD
2025-12-06 08:08:18,199 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:08:18,286 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:08:18,988 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:08:18,989 [INFO]    âšª No signal - HOLD
2025-12-06 08:08:19,490 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:08:19,578 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:08:20,276 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:08:20,276 [INFO]    âšª No signal - HOLD
2025-12-06 08:08:20,777 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:08:20,862 [INFO]    Current position: LONG 0.69
2025-12-06 08:08:20,863 [INFO]    Entry: $145.48 | Mark: $132.66
2025-12-06 08:08:20,863 [INFO]    PnL: -88.14% ($-8.85)
2025-12-06 08:08:20,863 [INFO]    Age: 54.5h / 72.0h
2025-12-06 08:08:21,364 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:08:21,447 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:08:22,255 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:08:22,255 [INFO]    âšª No signal - HOLD
2025-12-06 08:08:22,756 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:08:22,838 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:08:23,496 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:08:23,496 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:08:23,496 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:08:23,497 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:08:23,497 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:08:23,497 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:08:23,497 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:08:23,503 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:08:23,503 [INFO]    âšª No signal - HOLD
2025-12-06 08:08:24,004 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:08:24,091 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:08:24,740 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 13/15
2025-12-06 08:08:24,740 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:08:24,740 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:08:24,740 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:08:24,740 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 08:08:24,740 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:08:24,740 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:08:24,758 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:08:24,758 [INFO]    âšª No signal - HOLD
2025-12-06 08:08:25,259 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:08:25,347 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:08:26,058 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 10/15
2025-12-06 08:08:26,059 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:08:26,059 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:08:26,059 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:08:26,059 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:08:26,059 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:08:26,065 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:08:26,065 [INFO]    âšª No signal - HOLD
2025-12-06 08:08:26,066 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:11:26,135 [INFO] 
============================================================
2025-12-06 08:11:26,136 [INFO] ðŸ”„ LOOP #10 - 2025-12-06 08:11:26
2025-12-06 08:11:26,136 [INFO] ============================================================
2025-12-06 08:11:27,151 [INFO] ðŸ’“ Bot alive - Loop #10 - Active positions: 2
2025-12-06 08:11:27,240 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:11:27,240 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:11:27,326 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:11:28,026 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:11:28,027 [INFO]    âšª No signal - HOLD
2025-12-06 08:11:28,528 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:11:28,613 [INFO]    Current position: LONG 0.11
2025-12-06 08:11:28,613 [INFO]    Entry: $924.70 | Mark: $883.02
2025-12-06 08:11:28,614 [INFO]    PnL: -45.07% ($-4.58)
2025-12-06 08:11:28,614 [INFO]    Age: 53.7h / 72.0h
2025-12-06 08:11:29,114 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:11:29,200 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:11:29,881 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 13/15
2025-12-06 08:11:29,881 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:11:29,881 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:11:29,881 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:11:29,881 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 08:11:29,881 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:11:29,881 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:11:29,887 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:11:29,887 [INFO]    âšª No signal - HOLD
2025-12-06 08:11:30,388 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:11:30,473 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:11:31,207 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:11:31,207 [INFO]    âšª No signal - HOLD
2025-12-06 08:11:31,708 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:11:31,793 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:11:32,662 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:11:32,662 [INFO]    âšª No signal - HOLD
2025-12-06 08:11:33,163 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:11:33,245 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:11:33,926 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:11:33,926 [INFO]    âšª No signal - HOLD
2025-12-06 08:11:34,427 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:11:34,510 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:11:35,239 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:11:35,239 [INFO]    âšª No signal - HOLD
2025-12-06 08:11:35,740 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:11:35,825 [INFO]    Current position: LONG 0.69
2025-12-06 08:11:35,825 [INFO]    Entry: $145.48 | Mark: $132.63
2025-12-06 08:11:35,825 [INFO]    PnL: -88.34% ($-8.87)
2025-12-06 08:11:35,825 [INFO]    Age: 54.6h / 72.0h
2025-12-06 08:11:36,326 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:11:36,407 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:11:37,033 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:11:37,033 [INFO]    âšª No signal - HOLD
2025-12-06 08:11:37,534 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:11:37,618 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:11:38,267 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:11:38,267 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:11:38,268 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:11:38,268 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:11:38,268 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:11:38,268 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:11:38,268 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:11:38,283 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:11:38,283 [INFO]    âšª No signal - HOLD
2025-12-06 08:11:38,784 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:11:38,868 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:11:39,654 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 13/15
2025-12-06 08:11:39,654 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:11:39,654 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:11:39,654 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:11:39,654 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 08:11:39,654 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:11:39,654 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:11:39,659 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:11:39,659 [INFO]    âšª No signal - HOLD
2025-12-06 08:11:40,160 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:11:40,378 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:11:41,071 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 10/15
2025-12-06 08:11:41,071 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:11:41,071 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:11:41,071 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:11:41,071 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:11:41,071 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:11:41,076 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:11:41,076 [INFO]    âšª No signal - HOLD
2025-12-06 08:11:42,708 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:14:42,760 [INFO] 
============================================================
2025-12-06 08:14:42,761 [INFO] ðŸ”„ LOOP #11 - 2025-12-06 08:14:42
2025-12-06 08:14:42,761 [INFO] ============================================================
2025-12-06 08:14:42,850 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:14:42,850 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:14:42,936 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:14:43,652 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:14:43,652 [INFO]    âšª No signal - HOLD
2025-12-06 08:14:44,155 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:14:44,242 [INFO]    Current position: LONG 0.11
2025-12-06 08:14:44,242 [INFO]    Entry: $924.70 | Mark: $882.73
2025-12-06 08:14:44,242 [INFO]    PnL: -45.39% ($-4.62)
2025-12-06 08:14:44,242 [INFO]    Age: 53.8h / 72.0h
2025-12-06 08:14:44,743 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:14:44,839 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:14:45,569 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:14:45,569 [INFO]    âšª No signal - HOLD
2025-12-06 08:14:46,070 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:14:46,153 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:14:46,866 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:14:46,866 [INFO]    âšª No signal - HOLD
2025-12-06 08:14:47,367 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:14:47,452 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:14:48,144 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:14:48,144 [INFO]    âšª No signal - HOLD
2025-12-06 08:14:48,645 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:14:48,730 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:14:49,416 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:14:49,416 [INFO]    âšª No signal - HOLD
2025-12-06 08:14:49,917 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:14:50,003 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:14:50,881 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:14:50,882 [INFO]    âšª No signal - HOLD
2025-12-06 08:14:51,382 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:14:51,464 [INFO]    Current position: LONG 0.69
2025-12-06 08:14:51,465 [INFO]    Entry: $145.48 | Mark: $132.53
2025-12-06 08:14:51,465 [INFO]    PnL: -88.98% ($-8.93)
2025-12-06 08:14:51,465 [INFO]    Age: 54.6h / 72.0h
2025-12-06 08:14:51,966 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:14:52,055 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:14:52,786 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:14:52,787 [INFO]    âšª No signal - HOLD
2025-12-06 08:14:53,288 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:14:53,380 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:14:54,117 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:14:54,117 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:14:54,117 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:14:54,118 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:14:54,118 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:14:54,118 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:14:54,118 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:14:54,123 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:14:54,123 [INFO]    âšª No signal - HOLD
2025-12-06 08:14:54,624 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:14:54,710 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:14:55,676 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 12/15
2025-12-06 08:14:55,677 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:14:55,677 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:14:55,677 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:14:55,677 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:14:55,677 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:14:55,677 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:14:55,683 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:14:55,683 [INFO]    âšª No signal - HOLD
2025-12-06 08:14:56,184 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:14:56,268 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:14:56,980 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 10/15
2025-12-06 08:14:56,980 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:14:56,980 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:14:56,980 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:14:56,980 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:14:56,980 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:14:56,986 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:14:56,986 [INFO]    âšª No signal - HOLD
2025-12-06 08:14:56,986 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:17:57,029 [INFO] 
============================================================
2025-12-06 08:17:57,030 [INFO] ðŸ”„ LOOP #12 - 2025-12-06 08:17:57
2025-12-06 08:17:57,030 [INFO] ============================================================
2025-12-06 08:17:57,115 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:17:57,115 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:17:57,202 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:17:57,843 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:17:57,843 [INFO]    âšª No signal - HOLD
2025-12-06 08:17:58,344 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:17:58,429 [INFO]    Current position: LONG 0.11
2025-12-06 08:17:58,430 [INFO]    Entry: $924.70 | Mark: $882.75
2025-12-06 08:17:58,430 [INFO]    PnL: -45.37% ($-4.61)
2025-12-06 08:17:58,430 [INFO]    Age: 53.8h / 72.0h
2025-12-06 08:17:58,931 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:17:59,013 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:17:59,663 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 13/15
2025-12-06 08:17:59,664 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:17:59,664 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:17:59,664 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:17:59,664 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 08:17:59,664 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:17:59,664 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:17:59,668 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:17:59,668 [INFO]    âšª No signal - HOLD
2025-12-06 08:18:00,169 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:18:00,254 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:18:00,927 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:18:00,927 [INFO]    âšª No signal - HOLD
2025-12-06 08:18:01,428 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:18:01,514 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:18:02,222 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:18:02,222 [INFO]    âšª No signal - HOLD
2025-12-06 08:18:02,723 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:18:02,817 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:18:03,578 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:18:03,578 [INFO]    âšª No signal - HOLD
2025-12-06 08:18:04,079 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:18:04,163 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:18:04,835 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:18:04,835 [INFO]    âšª No signal - HOLD
2025-12-06 08:18:05,336 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:18:05,420 [INFO]    Current position: LONG 0.69
2025-12-06 08:18:05,420 [INFO]    Entry: $145.48 | Mark: $132.64
2025-12-06 08:18:05,421 [INFO]    PnL: -88.29% ($-8.86)
2025-12-06 08:18:05,421 [INFO]    Age: 54.7h / 72.0h
2025-12-06 08:18:05,922 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:18:06,012 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:18:06,806 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:18:06,806 [INFO]    âšª No signal - HOLD
2025-12-06 08:18:07,307 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:18:07,395 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:18:08,073 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:18:08,073 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:18:08,074 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:18:08,074 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:18:08,074 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:18:08,074 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:18:08,074 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:18:08,079 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:18:08,079 [INFO]    âšª No signal - HOLD
2025-12-06 08:18:08,580 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:18:08,666 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:18:09,337 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:18:09,337 [INFO]    âšª No signal - HOLD
2025-12-06 08:18:09,838 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:18:09,922 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:18:10,688 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 08:18:10,688 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 08:18:10,688 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:18:10,688 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:18:10,688 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:18:10,688 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:18:10,694 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:18:10,694 [INFO]    âšª No signal - HOLD
2025-12-06 08:18:10,695 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:21:10,754 [INFO] 
============================================================
2025-12-06 08:21:10,754 [INFO] ðŸ”„ LOOP #13 - 2025-12-06 08:21:10
2025-12-06 08:21:10,754 [INFO] ============================================================
2025-12-06 08:21:10,844 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:21:10,845 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:21:10,929 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:21:11,631 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:21:11,632 [INFO]    âšª No signal - HOLD
2025-12-06 08:21:12,132 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:21:12,218 [INFO]    Current position: LONG 0.11
2025-12-06 08:21:12,218 [INFO]    Entry: $924.70 | Mark: $881.50
2025-12-06 08:21:12,218 [INFO]    PnL: -46.72% ($-4.75)
2025-12-06 08:21:12,218 [INFO]    Age: 53.9h / 72.0h
2025-12-06 08:21:12,719 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:21:12,805 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:21:13,519 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 12/15
2025-12-06 08:21:13,520 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:21:13,520 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:21:13,520 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:21:13,520 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:21:13,520 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:21:13,520 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:21:13,526 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:21:13,526 [INFO]    âšª No signal - HOLD
2025-12-06 08:21:14,027 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:21:14,116 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:21:14,839 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:21:14,839 [INFO]    âšª No signal - HOLD
2025-12-06 08:21:15,340 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:21:15,427 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:21:16,146 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:21:16,146 [INFO]    âšª No signal - HOLD
2025-12-06 08:21:16,647 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:21:16,732 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:21:17,446 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:21:17,446 [INFO]    âšª No signal - HOLD
2025-12-06 08:21:17,947 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:21:18,042 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:21:18,720 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:21:18,720 [INFO]    âšª No signal - HOLD
2025-12-06 08:21:19,221 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:21:19,308 [INFO]    Current position: LONG 0.69
2025-12-06 08:21:19,308 [INFO]    Entry: $145.48 | Mark: $132.44
2025-12-06 08:21:19,308 [INFO]    PnL: -89.60% ($-8.99)
2025-12-06 08:21:19,308 [INFO]    Age: 54.8h / 72.0h
2025-12-06 08:21:19,809 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:21:19,893 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:21:20,753 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:21:20,753 [INFO]    âšª No signal - HOLD
2025-12-06 08:21:21,254 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:21:21,340 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:21:21,979 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:21:21,979 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:21:21,980 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:21:21,980 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:21:21,980 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:21:21,980 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:21:21,980 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:21:21,985 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:21:21,986 [INFO]    âšª No signal - HOLD
2025-12-06 08:21:22,486 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:21:22,579 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:21:23,224 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:21:23,225 [INFO]    âšª No signal - HOLD
2025-12-06 08:21:23,726 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:21:23,810 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:21:24,471 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 08:21:24,472 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 08:21:24,472 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:21:24,472 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:21:24,472 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:21:24,472 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:21:24,476 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:21:24,476 [INFO]    âšª No signal - HOLD
2025-12-06 08:21:24,477 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:24:24,577 [INFO] 
============================================================
2025-12-06 08:24:24,578 [INFO] ðŸ”„ LOOP #14 - 2025-12-06 08:24:24
2025-12-06 08:24:24,578 [INFO] ============================================================
2025-12-06 08:24:24,672 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:24:24,672 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:24:24,757 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:24:25,430 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:24:25,430 [INFO]    âšª No signal - HOLD
2025-12-06 08:24:25,931 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:24:26,016 [INFO]    Current position: LONG 0.11
2025-12-06 08:24:26,017 [INFO]    Entry: $924.70 | Mark: $880.55
2025-12-06 08:24:26,017 [INFO]    PnL: -47.75% ($-4.86)
2025-12-06 08:24:26,017 [INFO]    Age: 53.9h / 72.0h
2025-12-06 08:24:26,518 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:24:26,608 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:24:27,273 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 12/15
2025-12-06 08:24:27,274 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:24:27,274 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:24:27,274 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:24:27,274 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:24:27,274 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:24:27,274 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:24:27,279 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:24:27,279 [INFO]    âšª No signal - HOLD
2025-12-06 08:24:27,780 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:24:27,868 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:24:28,581 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:24:28,581 [INFO]    âšª No signal - HOLD
2025-12-06 08:24:29,081 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:24:29,169 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:24:29,875 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:24:29,875 [INFO]    âšª No signal - HOLD
2025-12-06 08:24:30,376 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:24:30,496 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:24:31,213 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:24:31,213 [INFO]    âšª No signal - HOLD
2025-12-06 08:24:31,714 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:24:31,800 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:24:32,473 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:24:32,473 [INFO]    âšª No signal - HOLD
2025-12-06 08:24:32,974 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:24:33,056 [INFO]    Current position: LONG 0.69
2025-12-06 08:24:33,057 [INFO]    Entry: $145.48 | Mark: $132.31
2025-12-06 08:24:33,057 [INFO]    PnL: -90.53% ($-9.09)
2025-12-06 08:24:33,057 [INFO]    Age: 54.8h / 72.0h
2025-12-06 08:24:33,558 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:24:33,642 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:24:34,291 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:24:34,291 [INFO]    âšª No signal - HOLD
2025-12-06 08:24:34,792 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:24:34,879 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:24:35,520 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:24:35,520 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:24:35,520 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:24:35,520 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:24:35,520 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:24:35,520 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:24:35,520 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:24:35,525 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:24:35,525 [INFO]    âšª No signal - HOLD
2025-12-06 08:24:36,026 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:24:36,110 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:24:36,871 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:24:36,872 [INFO]    âšª No signal - HOLD
2025-12-06 08:24:37,373 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:24:37,457 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:24:38,089 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 08:24:38,089 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 08:24:38,090 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:24:38,090 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:24:38,090 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:24:38,090 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:24:38,095 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:24:38,095 [INFO]    âšª No signal - HOLD
2025-12-06 08:24:38,095 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:27:38,193 [INFO] 
============================================================
2025-12-06 08:27:38,194 [INFO] ðŸ”„ LOOP #15 - 2025-12-06 08:27:38
2025-12-06 08:27:38,194 [INFO] ============================================================
2025-12-06 08:27:39,197 [INFO] ðŸ’“ Bot alive - Loop #15 - Active positions: 2
2025-12-06 08:27:39,285 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:27:39,285 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:27:39,370 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:27:40,058 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:27:40,058 [INFO]    âšª No signal - HOLD
2025-12-06 08:27:40,559 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:27:40,645 [INFO]    Current position: LONG 0.11
2025-12-06 08:27:40,645 [INFO]    Entry: $924.70 | Mark: $880.95
2025-12-06 08:27:40,645 [INFO]    PnL: -47.31% ($-4.81)
2025-12-06 08:27:40,645 [INFO]    Age: 54.0h / 72.0h
2025-12-06 08:27:41,146 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:27:41,230 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:27:41,998 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:27:41,999 [INFO]    âšª No signal - HOLD
2025-12-06 08:27:42,499 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:27:42,583 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:27:43,233 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:27:43,234 [INFO]    âšª No signal - HOLD
2025-12-06 08:27:43,734 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:27:43,820 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:27:44,478 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:27:44,478 [INFO]    âšª No signal - HOLD
2025-12-06 08:27:44,979 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:27:45,064 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:27:45,694 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:27:45,694 [INFO]    âšª No signal - HOLD
2025-12-06 08:27:46,195 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:27:46,277 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:27:46,943 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:27:46,943 [INFO]    âšª No signal - HOLD
2025-12-06 08:27:47,444 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:27:47,525 [INFO]    Current position: LONG 0.69
2025-12-06 08:27:47,525 [INFO]    Entry: $145.48 | Mark: $132.37
2025-12-06 08:27:47,525 [INFO]    PnL: -90.15% ($-9.05)
2025-12-06 08:27:47,525 [INFO]    Age: 54.9h / 72.0h
2025-12-06 08:27:48,026 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:27:48,110 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:27:48,747 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:27:48,747 [INFO]    âšª No signal - HOLD
2025-12-06 08:27:49,248 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:27:49,469 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:27:50,143 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:27:50,144 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:27:50,145 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:27:50,145 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:27:50,145 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:27:50,145 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:27:50,145 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:27:50,150 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:27:50,151 [INFO]    âšª No signal - HOLD
2025-12-06 08:27:50,651 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:27:50,736 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:27:51,455 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:27:51,455 [INFO]    âšª No signal - HOLD
2025-12-06 08:27:51,956 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:27:52,042 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:27:52,863 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 08:27:52,863 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 08:27:52,863 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:27:52,863 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:27:52,863 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:27:52,863 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:27:52,868 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:27:52,869 [INFO]    âšª No signal - HOLD
2025-12-06 08:27:52,869 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:30:52,954 [INFO] 
============================================================
2025-12-06 08:30:52,954 [INFO] ðŸ”„ LOOP #16 - 2025-12-06 08:30:52
2025-12-06 08:30:52,955 [INFO] ============================================================
2025-12-06 08:30:53,043 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:30:53,044 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:30:53,129 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:30:53,894 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:30:53,894 [INFO]    âšª No signal - HOLD
2025-12-06 08:30:54,395 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:30:54,485 [INFO]    Current position: LONG 0.11
2025-12-06 08:30:54,485 [INFO]    Entry: $924.70 | Mark: $879.75
2025-12-06 08:30:54,485 [INFO]    PnL: -48.61% ($-4.94)
2025-12-06 08:30:54,485 [INFO]    Age: 54.1h / 72.0h
2025-12-06 08:30:54,985 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:30:55,070 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:30:55,872 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 12/15
2025-12-06 08:30:55,872 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:30:55,872 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:30:55,872 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:30:55,873 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:30:55,873 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:30:55,873 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:30:55,886 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:30:55,886 [INFO]    âšª No signal - HOLD
2025-12-06 08:30:56,387 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:30:56,475 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:30:57,239 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:30:57,239 [INFO]    âšª No signal - HOLD
2025-12-06 08:30:57,740 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:30:57,828 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:30:58,567 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:30:58,568 [INFO]    âšª No signal - HOLD
2025-12-06 08:30:59,068 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:30:59,153 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:31:00,322 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:31:00,322 [INFO]    âšª No signal - HOLD
2025-12-06 08:31:00,823 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:31:00,914 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:31:01,933 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:31:01,933 [INFO]    âšª No signal - HOLD
2025-12-06 08:31:02,434 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:31:02,775 [INFO]    Current position: LONG 0.69
2025-12-06 08:31:02,775 [INFO]    Entry: $145.48 | Mark: $132.36
2025-12-06 08:31:02,775 [INFO]    PnL: -90.20% ($-9.05)
2025-12-06 08:31:02,775 [INFO]    Age: 54.9h / 72.0h
2025-12-06 08:31:03,276 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:31:03,362 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:31:04,074 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:31:04,074 [INFO]    âšª No signal - HOLD
2025-12-06 08:31:04,581 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:31:04,669 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:31:05,363 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:31:05,364 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:31:05,364 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:31:05,364 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:31:05,364 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:31:05,364 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:31:05,364 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:31:05,369 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:31:05,369 [INFO]    âšª No signal - HOLD
2025-12-06 08:31:05,870 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:31:05,953 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:31:07,362 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:31:07,362 [INFO]    âšª No signal - HOLD
2025-12-06 08:31:07,863 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:31:07,948 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:31:08,796 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 08:31:08,796 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 08:31:08,796 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:31:08,796 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:31:08,796 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:31:08,796 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:31:08,801 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:31:08,801 [INFO]    âšª No signal - HOLD
2025-12-06 08:31:08,802 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:34:08,876 [INFO] 
============================================================
2025-12-06 08:34:08,876 [INFO] ðŸ”„ LOOP #17 - 2025-12-06 08:34:08
2025-12-06 08:34:08,877 [INFO] ============================================================
2025-12-06 08:34:08,962 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:34:08,963 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:34:09,052 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:34:09,715 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:34:09,716 [INFO]    âšª No signal - HOLD
2025-12-06 08:34:10,217 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:34:10,303 [INFO]    Current position: LONG 0.11
2025-12-06 08:34:10,303 [INFO]    Entry: $924.70 | Mark: $879.05
2025-12-06 08:34:10,304 [INFO]    PnL: -49.37% ($-5.02)
2025-12-06 08:34:10,304 [INFO]    Age: 54.1h / 72.0h
2025-12-06 08:34:10,804 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:34:10,884 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:34:11,558 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 11/15
2025-12-06 08:34:11,558 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:34:11,558 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:34:11,558 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:34:11,559 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:34:11,559 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:34:11,564 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:34:11,564 [INFO]    âšª No signal - HOLD
2025-12-06 08:34:12,065 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:34:12,179 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:34:12,873 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:34:12,873 [INFO]    âšª No signal - HOLD
2025-12-06 08:34:13,374 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:34:13,461 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:34:14,122 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:34:14,122 [INFO]    âšª No signal - HOLD
2025-12-06 08:34:14,623 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:34:14,848 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:34:15,545 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:34:15,545 [INFO]    âšª No signal - HOLD
2025-12-06 08:34:16,045 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:34:16,134 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:34:16,781 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:34:16,781 [INFO]    âšª No signal - HOLD
2025-12-06 08:34:17,282 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:34:17,365 [INFO]    Current position: LONG 0.69
2025-12-06 08:34:17,365 [INFO]    Entry: $145.48 | Mark: $132.16
2025-12-06 08:34:17,365 [INFO]    PnL: -91.57% ($-9.19)
2025-12-06 08:34:17,365 [INFO]    Age: 55.0h / 72.0h
2025-12-06 08:34:17,866 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:34:17,952 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:34:18,592 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:34:18,592 [INFO]    âšª No signal - HOLD
2025-12-06 08:34:19,093 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:34:19,183 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:34:19,974 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:34:19,975 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:34:19,975 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:34:19,975 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:34:19,975 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:34:19,975 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:34:19,975 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:34:19,981 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:34:19,981 [INFO]    âšª No signal - HOLD
2025-12-06 08:34:20,482 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:34:20,569 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:34:21,250 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:34:21,251 [INFO]    âšª No signal - HOLD
2025-12-06 08:34:21,751 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:34:21,842 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:34:22,513 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 08:34:22,513 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 08:34:22,513 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:34:22,513 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:34:22,513 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:34:22,513 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:34:22,520 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:34:22,520 [INFO]    âšª No signal - HOLD
2025-12-06 08:34:22,520 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:37:22,618 [INFO] 
============================================================
2025-12-06 08:37:22,618 [INFO] ðŸ”„ LOOP #18 - 2025-12-06 08:37:22
2025-12-06 08:37:22,619 [INFO] ============================================================
2025-12-06 08:37:22,702 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:37:22,703 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:37:22,786 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:37:23,423 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:37:23,423 [INFO]    âšª No signal - HOLD
2025-12-06 08:37:23,924 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:37:24,006 [INFO]    Current position: LONG 0.11
2025-12-06 08:37:24,006 [INFO]    Entry: $924.70 | Mark: $879.60
2025-12-06 08:37:24,006 [INFO]    PnL: -48.77% ($-4.96)
2025-12-06 08:37:24,006 [INFO]    Age: 54.2h / 72.0h
2025-12-06 08:37:24,507 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:37:24,590 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:37:25,262 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 12/15
2025-12-06 08:37:25,262 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:37:25,262 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:37:25,262 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:37:25,263 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:37:25,263 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:37:25,263 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:37:25,267 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:37:25,268 [INFO]    âšª No signal - HOLD
2025-12-06 08:37:25,768 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:37:25,857 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:37:26,485 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:37:26,485 [INFO]    âšª No signal - HOLD
2025-12-06 08:37:26,986 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:37:27,211 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:37:27,855 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:37:27,855 [INFO]    âšª No signal - HOLD
2025-12-06 08:37:28,356 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:37:28,441 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:37:29,107 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:37:29,108 [INFO]    âšª No signal - HOLD
2025-12-06 08:37:29,608 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:37:29,692 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:37:30,348 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:37:30,348 [INFO]    âšª No signal - HOLD
2025-12-06 08:37:30,849 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:37:30,932 [INFO]    Current position: LONG 0.69
2025-12-06 08:37:30,933 [INFO]    Entry: $145.48 | Mark: $132.22
2025-12-06 08:37:30,933 [INFO]    PnL: -91.13% ($-9.15)
2025-12-06 08:37:30,933 [INFO]    Age: 55.0h / 72.0h
2025-12-06 08:37:31,434 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:37:31,521 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:37:32,159 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:37:32,159 [INFO]    âšª No signal - HOLD
2025-12-06 08:37:32,660 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:37:32,748 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:37:33,408 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:37:33,408 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:37:33,408 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:37:33,408 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:37:33,408 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:37:33,408 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:37:33,408 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:37:33,414 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:37:33,414 [INFO]    âšª No signal - HOLD
2025-12-06 08:37:33,915 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:37:34,004 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:37:34,626 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:37:34,626 [INFO]    âšª No signal - HOLD
2025-12-06 08:37:35,127 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:37:35,212 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:37:35,860 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 08:37:35,861 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 08:37:35,861 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:37:35,861 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:37:35,861 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:37:35,861 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:37:35,866 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:37:35,866 [INFO]    âšª No signal - HOLD
2025-12-06 08:37:35,866 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:40:35,906 [INFO] 
============================================================
2025-12-06 08:40:35,906 [INFO] ðŸ”„ LOOP #19 - 2025-12-06 08:40:35
2025-12-06 08:40:35,906 [INFO] ============================================================
2025-12-06 08:40:35,994 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:40:35,994 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:40:36,078 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:40:36,773 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:40:36,774 [INFO]    âšª No signal - HOLD
2025-12-06 08:40:37,275 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:40:37,360 [INFO]    Current position: LONG 0.11
2025-12-06 08:40:37,360 [INFO]    Entry: $924.70 | Mark: $880.08
2025-12-06 08:40:37,360 [INFO]    PnL: -48.25% ($-4.91)
2025-12-06 08:40:37,360 [INFO]    Age: 54.2h / 72.0h
2025-12-06 08:40:37,861 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:40:37,943 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:40:38,612 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 12/15
2025-12-06 08:40:38,612 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:40:38,612 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:40:38,612 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:40:38,612 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:40:38,612 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:40:38,612 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:40:38,618 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:40:38,618 [INFO]    âšª No signal - HOLD
2025-12-06 08:40:39,119 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:40:39,201 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:40:39,867 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:40:39,867 [INFO]    âšª No signal - HOLD
2025-12-06 08:40:40,368 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:40:40,451 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:40:41,077 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:40:41,077 [INFO]    âšª No signal - HOLD
2025-12-06 08:40:41,578 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:40:41,659 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:40:42,336 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:40:42,336 [INFO]    âšª No signal - HOLD
2025-12-06 08:40:42,837 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:40:42,922 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:40:43,721 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:40:43,721 [INFO]    âšª No signal - HOLD
2025-12-06 08:40:44,222 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:40:44,306 [INFO]    Current position: LONG 0.69
2025-12-06 08:40:44,306 [INFO]    Entry: $145.48 | Mark: $132.11
2025-12-06 08:40:44,307 [INFO]    PnL: -91.94% ($-9.23)
2025-12-06 08:40:44,307 [INFO]    Age: 55.1h / 72.0h
2025-12-06 08:40:44,807 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:40:44,899 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:40:45,600 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:40:45,600 [INFO]    âšª No signal - HOLD
2025-12-06 08:40:46,101 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:40:46,191 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:40:46,873 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:40:46,874 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:40:46,874 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:40:46,874 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:40:46,874 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:40:46,874 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:40:46,874 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:40:46,879 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:40:46,879 [INFO]    âšª No signal - HOLD
2025-12-06 08:40:47,380 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:40:47,465 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:40:48,122 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:40:48,122 [INFO]    âšª No signal - HOLD
2025-12-06 08:40:48,623 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:40:48,704 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:40:49,375 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 08:40:49,375 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 08:40:49,375 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:40:49,375 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:40:49,375 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:40:49,375 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:40:49,381 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:40:49,381 [INFO]    âšª No signal - HOLD
2025-12-06 08:40:49,381 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:43:49,481 [INFO] 
============================================================
2025-12-06 08:43:49,482 [INFO] ðŸ”„ LOOP #20 - 2025-12-06 08:43:49
2025-12-06 08:43:49,482 [INFO] ============================================================
2025-12-06 08:43:50,494 [INFO] ðŸ’“ Bot alive - Loop #20 - Active positions: 2
2025-12-06 08:43:50,580 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:43:50,581 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:43:50,663 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:43:51,329 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:43:51,329 [INFO]    âšª No signal - HOLD
2025-12-06 08:43:51,829 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:43:51,916 [INFO]    Current position: LONG 0.11
2025-12-06 08:43:51,916 [INFO]    Entry: $924.70 | Mark: $880.84
2025-12-06 08:43:51,916 [INFO]    PnL: -47.43% ($-4.82)
2025-12-06 08:43:51,916 [INFO]    Age: 54.3h / 72.0h
2025-12-06 08:43:52,417 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:43:52,502 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:43:53,201 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 12/15
2025-12-06 08:43:53,201 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:43:53,201 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:43:53,201 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:43:53,201 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:43:53,201 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:43:53,201 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:43:53,207 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:43:53,207 [INFO]    âšª No signal - HOLD
2025-12-06 08:43:53,708 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:43:53,794 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:43:54,593 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:43:54,593 [INFO]    âšª No signal - HOLD
2025-12-06 08:43:55,093 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:43:55,182 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:43:55,869 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:43:55,870 [INFO]    âšª No signal - HOLD
2025-12-06 08:43:56,370 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:43:56,454 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:43:57,297 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:43:57,297 [INFO]    âšª No signal - HOLD
2025-12-06 08:43:57,797 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:43:57,882 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:43:58,586 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:43:58,590 [INFO]    âšª No signal - HOLD
2025-12-06 08:43:59,091 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:43:59,178 [INFO]    Current position: LONG 0.69
2025-12-06 08:43:59,178 [INFO]    Entry: $145.48 | Mark: $132.22
2025-12-06 08:43:59,178 [INFO]    PnL: -91.11% ($-9.15)
2025-12-06 08:43:59,178 [INFO]    Age: 55.1h / 72.0h
2025-12-06 08:43:59,679 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:43:59,764 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:44:00,422 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:44:00,422 [INFO]    âšª No signal - HOLD
2025-12-06 08:44:00,923 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:44:01,008 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:44:01,836 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:44:01,836 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:44:01,836 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:44:01,836 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:44:01,836 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:44:01,836 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:44:01,836 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:44:01,842 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:44:01,842 [INFO]    âšª No signal - HOLD
2025-12-06 08:44:02,343 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:44:02,430 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:44:03,144 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:44:03,144 [INFO]    âšª No signal - HOLD
2025-12-06 08:44:03,645 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:44:03,733 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:44:04,580 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 08:44:04,581 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 08:44:04,581 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:44:04,581 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:44:04,581 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:44:04,581 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:44:04,585 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:44:04,586 [INFO]    âšª No signal - HOLD
2025-12-06 08:44:06,136 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:47:06,235 [INFO] 
============================================================
2025-12-06 08:47:06,235 [INFO] ðŸ”„ LOOP #21 - 2025-12-06 08:47:06
2025-12-06 08:47:06,235 [INFO] ============================================================
2025-12-06 08:47:06,322 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:47:06,322 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:47:06,405 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:47:07,100 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:47:07,100 [INFO]    âšª No signal - HOLD
2025-12-06 08:47:07,601 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:47:07,687 [INFO]    Current position: LONG 0.11
2025-12-06 08:47:07,687 [INFO]    Entry: $924.70 | Mark: $880.22
2025-12-06 08:47:07,688 [INFO]    PnL: -48.11% ($-4.89)
2025-12-06 08:47:07,688 [INFO]    Age: 54.3h / 72.0h
2025-12-06 08:47:08,188 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:47:08,273 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:47:08,958 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 12/15
2025-12-06 08:47:08,958 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:47:08,958 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:47:08,958 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:47:08,958 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:47:08,958 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:47:08,958 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:47:08,963 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:47:08,964 [INFO]    âšª No signal - HOLD
2025-12-06 08:47:09,465 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:47:09,561 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:47:10,245 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:47:10,246 [INFO]    âšª No signal - HOLD
2025-12-06 08:47:10,746 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:47:10,831 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:47:11,547 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:47:11,547 [INFO]    âšª No signal - HOLD
2025-12-06 08:47:12,048 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:47:12,136 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:47:12,815 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:47:12,816 [INFO]    âšª No signal - HOLD
2025-12-06 08:47:13,316 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:47:13,406 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:47:14,031 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:47:14,031 [INFO]    âšª No signal - HOLD
2025-12-06 08:47:14,532 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:47:14,616 [INFO]    Current position: LONG 0.69
2025-12-06 08:47:14,616 [INFO]    Entry: $145.48 | Mark: $132.22
2025-12-06 08:47:14,616 [INFO]    PnL: -91.11% ($-9.15)
2025-12-06 08:47:14,616 [INFO]    Age: 55.2h / 72.0h
2025-12-06 08:47:15,118 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:47:15,211 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:47:15,890 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:47:15,891 [INFO]    âšª No signal - HOLD
2025-12-06 08:47:16,392 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:47:16,479 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:47:17,129 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:47:17,130 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:47:17,130 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:47:17,130 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:47:17,130 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:47:17,130 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:47:17,130 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:47:17,136 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:47:17,136 [INFO]    âšª No signal - HOLD
2025-12-06 08:47:17,637 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:47:17,722 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:47:18,535 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:47:18,535 [INFO]    âšª No signal - HOLD
2025-12-06 08:47:19,036 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:47:19,121 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:47:19,794 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 08:47:19,794 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 08:47:19,794 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:47:19,794 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:47:19,794 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:47:19,794 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:47:19,800 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:47:19,800 [INFO]    âšª No signal - HOLD
2025-12-06 08:47:19,800 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:50:19,874 [INFO] 
============================================================
2025-12-06 08:50:19,874 [INFO] ðŸ”„ LOOP #22 - 2025-12-06 08:50:19
2025-12-06 08:50:19,874 [INFO] ============================================================
2025-12-06 08:50:19,961 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:50:19,961 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:50:20,048 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:50:20,796 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:50:20,796 [INFO]    âšª No signal - HOLD
2025-12-06 08:50:21,297 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:50:21,386 [INFO]    Current position: LONG 0.11
2025-12-06 08:50:21,386 [INFO]    Entry: $924.70 | Mark: $879.84
2025-12-06 08:50:21,387 [INFO]    PnL: -48.51% ($-4.93)
2025-12-06 08:50:21,387 [INFO]    Age: 54.4h / 72.0h
2025-12-06 08:50:21,887 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:50:21,974 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:50:22,722 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 12/15
2025-12-06 08:50:22,722 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:50:22,723 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:50:22,723 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:50:22,723 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:50:22,723 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:50:22,723 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:50:22,730 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:50:22,730 [INFO]    âšª No signal - HOLD
2025-12-06 08:50:23,231 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:50:23,320 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:50:24,020 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:50:24,020 [INFO]    âšª No signal - HOLD
2025-12-06 08:50:24,521 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:50:24,606 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:50:25,409 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:50:25,409 [INFO]    âšª No signal - HOLD
2025-12-06 08:50:25,910 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:50:25,995 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:50:26,683 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:50:26,684 [INFO]    âšª No signal - HOLD
2025-12-06 08:50:27,184 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:50:27,270 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:50:27,931 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:50:27,931 [INFO]    âšª No signal - HOLD
2025-12-06 08:50:28,432 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:50:28,520 [INFO]    Current position: LONG 0.69
2025-12-06 08:50:28,520 [INFO]    Entry: $145.48 | Mark: $132.16
2025-12-06 08:50:28,520 [INFO]    PnL: -91.52% ($-9.19)
2025-12-06 08:50:28,520 [INFO]    Age: 55.2h / 72.0h
2025-12-06 08:50:29,021 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:50:29,110 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:50:29,869 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:50:29,869 [INFO]    âšª No signal - HOLD
2025-12-06 08:50:30,370 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:50:30,460 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:50:31,185 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:50:31,186 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:50:31,187 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:50:31,187 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:50:31,187 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:50:31,187 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:50:31,187 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:50:31,194 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:50:31,194 [INFO]    âšª No signal - HOLD
2025-12-06 08:50:31,695 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:50:31,779 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:50:32,480 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:50:32,480 [INFO]    âšª No signal - HOLD
2025-12-06 08:50:32,981 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:50:33,065 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:50:34,002 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 08:50:34,002 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 08:50:34,002 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:50:34,002 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:50:34,002 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:50:34,002 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:50:34,007 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:50:34,008 [INFO]    âšª No signal - HOLD
2025-12-06 08:50:34,008 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:53:34,082 [INFO] 
============================================================
2025-12-06 08:53:34,083 [INFO] ðŸ”„ LOOP #23 - 2025-12-06 08:53:34
2025-12-06 08:53:34,083 [INFO] ============================================================
2025-12-06 08:53:34,173 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:53:34,173 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:53:34,255 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:53:34,946 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:53:34,946 [INFO]    âšª No signal - HOLD
2025-12-06 08:53:35,447 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:53:35,531 [INFO]    Current position: LONG 0.11
2025-12-06 08:53:35,531 [INFO]    Entry: $924.70 | Mark: $879.35
2025-12-06 08:53:35,531 [INFO]    PnL: -49.04% ($-4.99)
2025-12-06 08:53:35,531 [INFO]    Age: 54.4h / 72.0h
2025-12-06 08:53:36,032 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:53:36,120 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:53:36,791 [INFO] ðŸŽ¯ DOGEUSDT SHORT Signal | Score: 12/15
2025-12-06 08:53:36,792 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:53:36,792 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:53:36,792 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:53:36,792 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:53:36,792 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:53:36,792 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:53:36,798 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:53:36,798 [INFO]    âšª No signal - HOLD
2025-12-06 08:53:37,299 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:53:37,383 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:53:38,043 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:53:38,043 [INFO]    âšª No signal - HOLD
2025-12-06 08:53:38,544 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:53:38,626 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:53:39,269 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:53:39,270 [INFO]    âšª No signal - HOLD
2025-12-06 08:53:39,770 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:53:39,856 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:53:40,560 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:53:40,560 [INFO]    âšª No signal - HOLD
2025-12-06 08:53:41,061 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:53:41,145 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:53:41,944 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:53:41,945 [INFO]    âšª No signal - HOLD
2025-12-06 08:53:42,445 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:53:42,531 [INFO]    Current position: LONG 0.69
2025-12-06 08:53:42,531 [INFO]    Entry: $145.48 | Mark: $132.01
2025-12-06 08:53:42,531 [INFO]    PnL: -92.61% ($-9.30)
2025-12-06 08:53:42,531 [INFO]    Age: 55.3h / 72.0h
2025-12-06 08:53:43,032 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:53:43,115 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:53:43,949 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:53:43,950 [INFO]    âšª No signal - HOLD
2025-12-06 08:53:44,451 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:53:44,538 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:53:45,349 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 12/15
2025-12-06 08:53:45,349 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 08:53:45,349 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 08:53:45,349 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:53:45,349 [INFO]    âš¡ RSI acceptable range
2025-12-06 08:53:45,349 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:53:45,349 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:53:45,354 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:53:45,354 [INFO]    âšª No signal - HOLD
2025-12-06 08:53:45,855 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:53:45,948 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:53:46,627 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:53:46,627 [INFO]    âšª No signal - HOLD
2025-12-06 08:53:47,128 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:53:47,211 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:53:48,008 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 08:53:48,008 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 08:53:48,008 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:53:48,008 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:53:48,009 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:53:48,009 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:53:48,013 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:53:48,013 [INFO]    âšª No signal - HOLD
2025-12-06 08:53:48,013 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 08:56:48,098 [INFO] 
============================================================
2025-12-06 08:56:48,098 [INFO] ðŸ”„ LOOP #24 - 2025-12-06 08:56:48
2025-12-06 08:56:48,098 [INFO] ============================================================
2025-12-06 08:56:48,182 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 08:56:48,182 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 08:56:48,264 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 08:56:48,945 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:56:48,946 [INFO]    âšª No signal - HOLD
2025-12-06 08:56:49,447 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 08:56:49,532 [INFO]    Current position: LONG 0.11
2025-12-06 08:56:49,533 [INFO]    Entry: $924.70 | Mark: $878.55
2025-12-06 08:56:49,533 [INFO]    PnL: -49.91% ($-5.08)
2025-12-06 08:56:49,533 [INFO]    Age: 54.5h / 72.0h
2025-12-06 08:56:50,034 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 08:56:50,117 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 08:56:50,798 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:56:50,798 [INFO]    âšª No signal - HOLD
2025-12-06 08:56:51,299 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 08:56:51,385 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 08:56:52,040 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:56:52,040 [INFO]    âšª No signal - HOLD
2025-12-06 08:56:52,541 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 08:56:52,628 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 08:56:53,288 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:56:53,288 [INFO]    âšª No signal - HOLD
2025-12-06 08:56:53,789 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 08:56:53,871 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 08:56:54,528 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:56:54,528 [INFO]    âšª No signal - HOLD
2025-12-06 08:56:55,029 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 08:56:55,115 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 08:56:55,813 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:56:55,814 [INFO]    âšª No signal - HOLD
2025-12-06 08:56:56,315 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 08:56:56,399 [INFO]    Current position: LONG 0.69
2025-12-06 08:56:56,400 [INFO]    Entry: $145.48 | Mark: $131.83
2025-12-06 08:56:56,400 [INFO]    PnL: -93.85% ($-9.42)
2025-12-06 08:56:56,400 [INFO]    Age: 55.3h / 72.0h
2025-12-06 08:56:56,901 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 08:56:56,985 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 08:56:57,633 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:56:57,635 [INFO]    âšª No signal - HOLD
2025-12-06 08:56:58,135 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 08:56:58,353 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 08:56:59,022 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:56:59,022 [INFO]    âšª No signal - HOLD
2025-12-06 08:56:59,523 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 08:56:59,608 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 08:57:00,244 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:57:00,244 [INFO]    âšª No signal - HOLD
2025-12-06 08:57:00,745 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 08:57:00,831 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 08:57:01,621 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 08:57:01,622 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 08:57:01,622 [INFO]    âš ï¸ Near EMA21
2025-12-06 08:57:01,622 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 08:57:01,622 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 08:57:01,622 [INFO]    âœ… R:R = 2.0:1
2025-12-06 08:57:01,628 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 08:57:01,629 [INFO]    âšª No signal - HOLD
2025-12-06 08:57:01,629 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:00:01,725 [INFO] 
============================================================
2025-12-06 09:00:01,726 [INFO] ðŸ”„ LOOP #25 - 2025-12-06 09:00:01
2025-12-06 09:00:01,726 [INFO] ============================================================
2025-12-06 09:00:02,843 [INFO] ðŸ’“ Bot alive - Loop #25 - Active positions: 2
2025-12-06 09:00:02,939 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:00:02,939 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:00:03,031 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:00:04,430 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:00:04,430 [INFO]    âšª No signal - HOLD
2025-12-06 09:00:04,931 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:00:05,019 [INFO]    Current position: LONG 0.11
2025-12-06 09:00:05,019 [INFO]    Entry: $924.70 | Mark: $878.63
2025-12-06 09:00:05,019 [INFO]    PnL: -49.82% ($-5.07)
2025-12-06 09:00:05,019 [INFO]    Age: 54.5h / 72.0h
2025-12-06 09:00:05,520 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:00:05,606 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:00:07,264 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:00:07,265 [INFO]    âšª No signal - HOLD
2025-12-06 09:00:07,768 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:00:07,856 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:00:09,336 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:00:09,336 [INFO]    âšª No signal - HOLD
2025-12-06 09:00:09,837 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:00:09,924 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:00:11,293 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:00:11,297 [INFO]    âšª No signal - HOLD
2025-12-06 09:00:11,798 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:00:11,885 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:00:13,291 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:00:13,291 [INFO]    âšª No signal - HOLD
2025-12-06 09:00:13,793 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:00:13,880 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:00:15,441 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:00:15,441 [INFO]    âšª No signal - HOLD
2025-12-06 09:00:15,941 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:00:16,025 [INFO]    Current position: LONG 0.69
2025-12-06 09:00:16,026 [INFO]    Entry: $145.48 | Mark: $131.94
2025-12-06 09:00:16,026 [INFO]    PnL: -93.11% ($-9.35)
2025-12-06 09:00:16,026 [INFO]    Age: 55.4h / 72.0h
2025-12-06 09:00:16,528 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:00:16,616 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:00:18,173 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:00:18,178 [INFO]    âšª No signal - HOLD
2025-12-06 09:00:18,678 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:00:18,764 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:00:20,249 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:00:20,249 [INFO]    âšª No signal - HOLD
2025-12-06 09:00:20,749 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:00:20,836 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:00:21,689 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 11/15
2025-12-06 09:00:21,689 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:00:21,689 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 09:00:21,690 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:00:21,690 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:00:21,690 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:00:21,696 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:00:21,696 [INFO]    âšª No signal - HOLD
2025-12-06 09:00:22,197 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:00:22,283 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:00:22,967 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 09:00:22,968 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 09:00:22,968 [INFO]    âš ï¸ Near EMA21
2025-12-06 09:00:22,969 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:00:22,969 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:00:22,969 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:00:22,974 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:00:22,974 [INFO]    âšª No signal - HOLD
2025-12-06 09:00:22,974 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:03:23,073 [INFO] 
============================================================
2025-12-06 09:03:23,074 [INFO] ðŸ”„ LOOP #26 - 2025-12-06 09:03:23
2025-12-06 09:03:23,074 [INFO] ============================================================
2025-12-06 09:03:23,160 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:03:23,161 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:03:23,242 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:03:23,878 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:03:23,878 [INFO]    âšª No signal - HOLD
2025-12-06 09:03:24,379 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:03:24,464 [INFO]    Current position: LONG 0.11
2025-12-06 09:03:24,464 [INFO]    Entry: $924.70 | Mark: $880.23
2025-12-06 09:03:24,464 [INFO]    PnL: -48.10% ($-4.89)
2025-12-06 09:03:24,464 [INFO]    Age: 54.6h / 72.0h
2025-12-06 09:03:24,965 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:03:25,067 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:03:25,760 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:03:25,760 [INFO]    âšª No signal - HOLD
2025-12-06 09:03:26,261 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:03:26,350 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:03:26,984 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:03:26,984 [INFO]    âšª No signal - HOLD
2025-12-06 09:03:27,485 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:03:27,570 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:03:28,191 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:03:28,191 [INFO]    âšª No signal - HOLD
2025-12-06 09:03:28,692 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:03:28,780 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:03:29,392 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:03:29,393 [INFO]    âšª No signal - HOLD
2025-12-06 09:03:29,893 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:03:29,978 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:03:30,599 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:03:30,599 [INFO]    âšª No signal - HOLD
2025-12-06 09:03:31,100 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:03:31,186 [INFO]    Current position: LONG 0.69
2025-12-06 09:03:31,186 [INFO]    Entry: $145.48 | Mark: $132.11
2025-12-06 09:03:31,186 [INFO]    PnL: -91.91% ($-9.23)
2025-12-06 09:03:31,186 [INFO]    Age: 55.5h / 72.0h
2025-12-06 09:03:31,687 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:03:31,775 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:03:32,592 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:03:32,592 [INFO]    âšª No signal - HOLD
2025-12-06 09:03:33,092 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:03:33,179 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:03:33,844 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:03:33,844 [INFO]    âšª No signal - HOLD
2025-12-06 09:03:34,344 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:03:34,430 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:03:35,224 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 11/15
2025-12-06 09:03:35,225 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:03:35,225 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 09:03:35,225 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:03:35,225 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:03:35,225 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:03:35,230 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:03:35,230 [INFO]    âšª No signal - HOLD
2025-12-06 09:03:35,731 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:03:35,817 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:03:36,443 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 09:03:36,443 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 09:03:36,443 [INFO]    âš ï¸ Near EMA21
2025-12-06 09:03:36,443 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:03:36,444 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:03:36,444 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:03:36,449 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:03:36,449 [INFO]    âšª No signal - HOLD
2025-12-06 09:03:36,449 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:06:36,549 [INFO] 
============================================================
2025-12-06 09:06:36,550 [INFO] ðŸ”„ LOOP #27 - 2025-12-06 09:06:36
2025-12-06 09:06:36,550 [INFO] ============================================================
2025-12-06 09:06:36,635 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:06:36,635 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:06:36,722 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:06:37,447 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:06:37,447 [INFO]    âšª No signal - HOLD
2025-12-06 09:06:37,948 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:06:38,036 [INFO]    Current position: LONG 0.11
2025-12-06 09:06:38,037 [INFO]    Entry: $924.70 | Mark: $879.61
2025-12-06 09:06:38,037 [INFO]    PnL: -48.76% ($-4.96)
2025-12-06 09:06:38,037 [INFO]    Age: 54.6h / 72.0h
2025-12-06 09:06:38,538 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:06:38,624 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:06:39,316 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:06:39,316 [INFO]    âšª No signal - HOLD
2025-12-06 09:06:39,817 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:06:39,902 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:06:40,579 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:06:40,580 [INFO]    âšª No signal - HOLD
2025-12-06 09:06:41,080 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:06:41,164 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:06:41,829 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:06:41,830 [INFO]    âšª No signal - HOLD
2025-12-06 09:06:42,331 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:06:42,417 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:06:43,093 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:06:43,094 [INFO]    âšª No signal - HOLD
2025-12-06 09:06:43,595 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:06:43,683 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:06:44,387 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:06:44,388 [INFO]    âšª No signal - HOLD
2025-12-06 09:06:44,888 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:06:44,976 [INFO]    Current position: LONG 0.69
2025-12-06 09:06:44,976 [INFO]    Entry: $145.48 | Mark: $132.01
2025-12-06 09:06:44,977 [INFO]    PnL: -92.56% ($-9.29)
2025-12-06 09:06:44,977 [INFO]    Age: 55.5h / 72.0h
2025-12-06 09:06:45,477 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:06:45,567 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:06:46,263 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:06:46,263 [INFO]    âšª No signal - HOLD
2025-12-06 09:06:46,764 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:06:46,848 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:06:47,550 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:06:47,550 [INFO]    âšª No signal - HOLD
2025-12-06 09:06:48,051 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:06:48,134 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:06:48,786 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 11/15
2025-12-06 09:06:48,786 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:06:48,786 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 09:06:48,786 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:06:48,786 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:06:48,786 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:06:48,796 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:06:48,796 [INFO]    âšª No signal - HOLD
2025-12-06 09:06:49,297 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:06:49,380 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:06:50,225 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 09:06:50,225 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 09:06:50,225 [INFO]    âš ï¸ Near EMA21
2025-12-06 09:06:50,225 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:06:50,225 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:06:50,225 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:06:50,231 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:06:50,231 [INFO]    âšª No signal - HOLD
2025-12-06 09:06:50,231 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:09:50,332 [INFO] 
============================================================
2025-12-06 09:09:50,332 [INFO] ðŸ”„ LOOP #28 - 2025-12-06 09:09:50
2025-12-06 09:09:50,332 [INFO] ============================================================
2025-12-06 09:09:50,419 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:09:50,419 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:09:50,502 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:09:51,168 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:09:51,168 [INFO]    âšª No signal - HOLD
2025-12-06 09:09:51,669 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:09:51,751 [INFO]    Current position: LONG 0.11
2025-12-06 09:09:51,752 [INFO]    Entry: $924.70 | Mark: $881.40
2025-12-06 09:09:51,752 [INFO]    PnL: -46.83% ($-4.76)
2025-12-06 09:09:51,752 [INFO]    Age: 54.7h / 72.0h
2025-12-06 09:09:52,253 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:09:52,338 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:09:53,043 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:09:53,043 [INFO]    âšª No signal - HOLD
2025-12-06 09:09:53,544 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:09:53,628 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:09:54,268 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:09:54,268 [INFO]    âšª No signal - HOLD
2025-12-06 09:09:54,769 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:09:54,854 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:09:55,523 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:09:55,523 [INFO]    âšª No signal - HOLD
2025-12-06 09:09:56,024 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:09:56,108 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:09:56,858 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:09:56,858 [INFO]    âšª No signal - HOLD
2025-12-06 09:09:57,359 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:09:57,441 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:09:58,232 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:09:58,232 [INFO]    âšª No signal - HOLD
2025-12-06 09:09:58,733 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:09:58,818 [INFO]    Current position: LONG 0.69
2025-12-06 09:09:58,818 [INFO]    Entry: $145.48 | Mark: $132.22
2025-12-06 09:09:58,818 [INFO]    PnL: -91.18% ($-9.15)
2025-12-06 09:09:58,818 [INFO]    Age: 55.6h / 72.0h
2025-12-06 09:09:59,319 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:09:59,402 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:10:00,153 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:10:00,154 [INFO]    âšª No signal - HOLD
2025-12-06 09:10:00,654 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:10:00,742 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:10:01,408 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:10:01,409 [INFO]    âšª No signal - HOLD
2025-12-06 09:10:01,910 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:10:02,129 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:10:02,823 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 11/15
2025-12-06 09:10:02,824 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:10:02,824 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 09:10:02,824 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:10:02,824 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:10:02,824 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:10:02,829 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:10:02,829 [INFO]    âšª No signal - HOLD
2025-12-06 09:10:03,330 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:10:03,417 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:10:04,066 [INFO] ðŸŽ¯ NEARUSDT SHORT Signal | Score: 9/15
2025-12-06 09:10:04,066 [INFO]    âš ï¸ HTF aligned (DOWN), LTF diverging
2025-12-06 09:10:04,066 [INFO]    âš ï¸ Near EMA21
2025-12-06 09:10:04,066 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:10:04,066 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:10:04,066 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:10:04,072 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:10:04,072 [INFO]    âšª No signal - HOLD
2025-12-06 09:10:04,072 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:13:04,131 [INFO] 
============================================================
2025-12-06 09:13:04,131 [INFO] ðŸ”„ LOOP #29 - 2025-12-06 09:13:04
2025-12-06 09:13:04,132 [INFO] ============================================================
2025-12-06 09:13:04,220 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:13:04,221 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:13:04,304 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:13:04,952 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:13:04,953 [INFO]    âšª No signal - HOLD
2025-12-06 09:13:05,453 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:13:05,538 [INFO]    Current position: LONG 0.11
2025-12-06 09:13:05,538 [INFO]    Entry: $924.70 | Mark: $882.93
2025-12-06 09:13:05,538 [INFO]    PnL: -45.18% ($-4.60)
2025-12-06 09:13:05,538 [INFO]    Age: 54.8h / 72.0h
2025-12-06 09:13:06,039 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:13:06,126 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:13:06,788 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:13:06,789 [INFO]    âšª No signal - HOLD
2025-12-06 09:13:07,289 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:13:07,374 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:13:07,984 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:13:07,984 [INFO]    âšª No signal - HOLD
2025-12-06 09:13:08,485 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:13:08,566 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:13:09,179 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:13:09,179 [INFO]    âšª No signal - HOLD
2025-12-06 09:13:09,680 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:13:09,765 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:13:10,425 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:13:10,425 [INFO]    âšª No signal - HOLD
2025-12-06 09:13:10,926 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:13:11,011 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:13:11,714 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:13:11,715 [INFO]    âšª No signal - HOLD
2025-12-06 09:13:12,215 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:13:12,296 [INFO]    Current position: LONG 0.69
2025-12-06 09:13:12,297 [INFO]    Entry: $145.48 | Mark: $132.32
2025-12-06 09:13:12,297 [INFO]    PnL: -90.49% ($-9.08)
2025-12-06 09:13:12,297 [INFO]    Age: 55.6h / 72.0h
2025-12-06 09:13:12,798 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:13:12,882 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:13:13,550 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:13:13,550 [INFO]    âšª No signal - HOLD
2025-12-06 09:13:14,051 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:13:14,139 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:13:14,825 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:13:14,826 [INFO]    âšª No signal - HOLD
2025-12-06 09:13:15,326 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:13:15,408 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:13:16,058 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 11/15
2025-12-06 09:13:16,058 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:13:16,058 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 09:13:16,058 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:13:16,059 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:13:16,059 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:13:16,063 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:13:16,064 [INFO]    âšª No signal - HOLD
2025-12-06 09:13:16,565 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:13:16,651 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:13:17,276 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:13:17,277 [INFO]    âšª No signal - HOLD
2025-12-06 09:13:17,277 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:16:17,373 [INFO] 
============================================================
2025-12-06 09:16:17,374 [INFO] ðŸ”„ LOOP #30 - 2025-12-06 09:16:17
2025-12-06 09:16:17,374 [INFO] ============================================================
2025-12-06 09:16:18,388 [INFO] ðŸ’“ Bot alive - Loop #30 - Active positions: 2
2025-12-06 09:16:18,475 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:16:18,476 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:16:18,563 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:16:19,274 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:16:19,274 [INFO]    âšª No signal - HOLD
2025-12-06 09:16:19,775 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:16:19,861 [INFO]    Current position: LONG 0.11
2025-12-06 09:16:19,861 [INFO]    Entry: $924.70 | Mark: $883.06
2025-12-06 09:16:19,861 [INFO]    PnL: -45.03% ($-4.58)
2025-12-06 09:16:19,861 [INFO]    Age: 54.8h / 72.0h
2025-12-06 09:16:20,362 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:16:20,445 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:16:21,129 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:16:21,130 [INFO]    âšª No signal - HOLD
2025-12-06 09:16:21,630 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:16:21,715 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:16:22,525 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:16:22,526 [INFO]    âšª No signal - HOLD
2025-12-06 09:16:23,026 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:16:23,109 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:16:23,770 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:16:23,770 [INFO]    âšª No signal - HOLD
2025-12-06 09:16:24,271 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:16:24,357 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:16:25,039 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:16:25,039 [INFO]    âšª No signal - HOLD
2025-12-06 09:16:25,540 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:16:25,622 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:16:26,618 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:16:26,619 [INFO]    âšª No signal - HOLD
2025-12-06 09:16:27,119 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:16:27,204 [INFO]    Current position: LONG 0.69
2025-12-06 09:16:27,204 [INFO]    Entry: $145.48 | Mark: $132.27
2025-12-06 09:16:27,204 [INFO]    PnL: -90.77% ($-9.11)
2025-12-06 09:16:27,204 [INFO]    Age: 55.7h / 72.0h
2025-12-06 09:16:27,705 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:16:27,791 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:16:28,464 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:16:28,465 [INFO]    âšª No signal - HOLD
2025-12-06 09:16:28,965 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:16:29,053 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:16:29,857 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:16:29,857 [INFO]    âšª No signal - HOLD
2025-12-06 09:16:30,358 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:16:30,442 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:16:31,156 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 11/15
2025-12-06 09:16:31,156 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:16:31,156 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 09:16:31,157 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:16:31,157 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:16:31,157 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:16:31,162 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:16:31,162 [INFO]    âšª No signal - HOLD
2025-12-06 09:16:31,663 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:16:31,746 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:16:32,452 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:16:32,453 [INFO]    âšª No signal - HOLD
2025-12-06 09:16:33,878 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:19:33,979 [INFO] 
============================================================
2025-12-06 09:19:33,979 [INFO] ðŸ”„ LOOP #31 - 2025-12-06 09:19:33
2025-12-06 09:19:33,979 [INFO] ============================================================
2025-12-06 09:19:34,066 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:19:34,066 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:19:34,150 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:19:34,833 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:19:34,834 [INFO]    âšª No signal - HOLD
2025-12-06 09:19:35,334 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:19:35,435 [INFO]    Current position: LONG 0.11
2025-12-06 09:19:35,435 [INFO]    Entry: $924.70 | Mark: $883.55
2025-12-06 09:19:35,436 [INFO]    PnL: -44.50% ($-4.53)
2025-12-06 09:19:35,436 [INFO]    Age: 54.9h / 72.0h
2025-12-06 09:19:35,937 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:19:36,026 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:19:36,725 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:19:36,726 [INFO]    âšª No signal - HOLD
2025-12-06 09:19:37,227 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:19:37,314 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:19:38,088 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:19:38,089 [INFO]    âšª No signal - HOLD
2025-12-06 09:19:38,589 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:19:38,676 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:19:39,351 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:19:39,352 [INFO]    âšª No signal - HOLD
2025-12-06 09:19:39,852 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:19:39,944 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:19:40,721 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:19:40,721 [INFO]    âšª No signal - HOLD
2025-12-06 09:19:41,222 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:19:41,309 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:19:41,975 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:19:41,975 [INFO]    âšª No signal - HOLD
2025-12-06 09:19:42,476 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:19:42,561 [INFO]    Current position: LONG 0.69
2025-12-06 09:19:42,562 [INFO]    Entry: $145.48 | Mark: $132.30
2025-12-06 09:19:42,562 [INFO]    PnL: -90.59% ($-9.09)
2025-12-06 09:19:42,562 [INFO]    Age: 55.7h / 72.0h
2025-12-06 09:19:43,063 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:19:43,152 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:19:43,786 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:19:43,786 [INFO]    âšª No signal - HOLD
2025-12-06 09:19:44,287 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:19:44,372 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:19:45,041 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:19:45,041 [INFO]    âšª No signal - HOLD
2025-12-06 09:19:45,542 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:19:45,629 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:19:46,673 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 11/15
2025-12-06 09:19:46,673 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:19:46,673 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 09:19:46,673 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:19:46,674 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:19:46,674 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:19:46,680 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:19:46,681 [INFO]    âšª No signal - HOLD
2025-12-06 09:19:47,181 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:19:47,401 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:19:48,074 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:19:48,074 [INFO]    âšª No signal - HOLD
2025-12-06 09:19:48,074 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:22:48,174 [INFO] 
============================================================
2025-12-06 09:22:48,174 [INFO] ðŸ”„ LOOP #32 - 2025-12-06 09:22:48
2025-12-06 09:22:48,174 [INFO] ============================================================
2025-12-06 09:22:48,261 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:22:48,261 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:22:48,344 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:22:48,991 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:22:48,992 [INFO]    âšª No signal - HOLD
2025-12-06 09:22:49,492 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:22:49,577 [INFO]    Current position: LONG 0.11
2025-12-06 09:22:49,577 [INFO]    Entry: $924.70 | Mark: $882.90
2025-12-06 09:22:49,577 [INFO]    PnL: -45.20% ($-4.60)
2025-12-06 09:22:49,577 [INFO]    Age: 54.9h / 72.0h
2025-12-06 09:22:50,078 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:22:50,164 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:22:50,828 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:22:50,828 [INFO]    âšª No signal - HOLD
2025-12-06 09:22:51,329 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:22:51,413 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:22:52,068 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:22:52,068 [INFO]    âšª No signal - HOLD
2025-12-06 09:22:52,569 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:22:52,652 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:22:53,305 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:22:53,305 [INFO]    âšª No signal - HOLD
2025-12-06 09:22:53,806 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:22:53,896 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:22:54,578 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:22:54,578 [INFO]    âšª No signal - HOLD
2025-12-06 09:22:55,079 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:22:55,166 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:22:55,873 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:22:55,873 [INFO]    âšª No signal - HOLD
2025-12-06 09:22:56,374 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:22:56,457 [INFO]    Current position: LONG 0.69
2025-12-06 09:22:56,458 [INFO]    Entry: $145.48 | Mark: $132.25
2025-12-06 09:22:56,458 [INFO]    PnL: -90.95% ($-9.13)
2025-12-06 09:22:56,458 [INFO]    Age: 55.8h / 72.0h
2025-12-06 09:22:56,959 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:22:57,043 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:22:57,669 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:22:57,669 [INFO]    âšª No signal - HOLD
2025-12-06 09:22:58,170 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:22:58,255 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:22:59,064 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:22:59,064 [INFO]    âšª No signal - HOLD
2025-12-06 09:22:59,565 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:22:59,649 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:23:00,458 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 11/15
2025-12-06 09:23:00,458 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:23:00,458 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 09:23:00,458 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:23:00,458 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:23:00,458 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:23:00,463 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:23:00,463 [INFO]    âšª No signal - HOLD
2025-12-06 09:23:00,964 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:23:01,050 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:23:01,883 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:23:01,884 [INFO]    âšª No signal - HOLD
2025-12-06 09:23:01,884 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:26:01,967 [INFO] 
============================================================
2025-12-06 09:26:01,967 [INFO] ðŸ”„ LOOP #33 - 2025-12-06 09:26:01
2025-12-06 09:26:01,967 [INFO] ============================================================
2025-12-06 09:26:02,053 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:26:02,053 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:26:02,138 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:26:02,829 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:26:02,830 [INFO]    âšª No signal - HOLD
2025-12-06 09:26:03,330 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:26:03,420 [INFO]    Current position: LONG 0.11
2025-12-06 09:26:03,420 [INFO]    Entry: $924.70 | Mark: $882.80
2025-12-06 09:26:03,421 [INFO]    PnL: -45.31% ($-4.61)
2025-12-06 09:26:03,421 [INFO]    Age: 55.0h / 72.0h
2025-12-06 09:26:03,921 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:26:04,012 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:26:04,755 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:26:04,755 [INFO]    âšª No signal - HOLD
2025-12-06 09:26:05,256 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:26:05,340 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:26:06,063 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:26:06,063 [INFO]    âšª No signal - HOLD
2025-12-06 09:26:06,566 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:26:06,659 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:26:07,333 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:26:07,334 [INFO]    âšª No signal - HOLD
2025-12-06 09:26:07,835 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:26:07,921 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:26:08,643 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:26:08,643 [INFO]    âšª No signal - HOLD
2025-12-06 09:26:09,144 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:26:09,226 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:26:09,923 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:26:09,924 [INFO]    âšª No signal - HOLD
2025-12-06 09:26:10,424 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:26:10,533 [INFO]    Current position: LONG 0.69
2025-12-06 09:26:10,533 [INFO]    Entry: $145.48 | Mark: $132.31
2025-12-06 09:26:10,533 [INFO]    PnL: -90.53% ($-9.09)
2025-12-06 09:26:10,534 [INFO]    Age: 55.8h / 72.0h
2025-12-06 09:26:11,034 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:26:11,120 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:26:11,793 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:26:11,793 [INFO]    âšª No signal - HOLD
2025-12-06 09:26:12,294 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:26:12,377 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:26:13,065 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:26:13,065 [INFO]    âšª No signal - HOLD
2025-12-06 09:26:13,566 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:26:13,651 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:26:14,316 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 11/15
2025-12-06 09:26:14,317 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:26:14,317 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 09:26:14,317 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:26:14,317 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:26:14,317 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:26:14,322 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:26:14,322 [INFO]    âšª No signal - HOLD
2025-12-06 09:26:14,823 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:26:14,910 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:26:15,554 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:26:15,554 [INFO]    âšª No signal - HOLD
2025-12-06 09:26:15,554 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:29:15,614 [INFO] 
============================================================
2025-12-06 09:29:15,615 [INFO] ðŸ”„ LOOP #34 - 2025-12-06 09:29:15
2025-12-06 09:29:15,615 [INFO] ============================================================
2025-12-06 09:29:15,699 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:29:15,699 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:29:15,781 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:29:16,488 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:29:16,489 [INFO]    âšª No signal - HOLD
2025-12-06 09:29:16,989 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:29:17,073 [INFO]    Current position: LONG 0.11
2025-12-06 09:29:17,073 [INFO]    Entry: $924.70 | Mark: $882.93
2025-12-06 09:29:17,073 [INFO]    PnL: -45.17% ($-4.59)
2025-12-06 09:29:17,073 [INFO]    Age: 55.0h / 72.0h
2025-12-06 09:29:17,574 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:29:17,658 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:29:18,307 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:29:18,307 [INFO]    âšª No signal - HOLD
2025-12-06 09:29:18,808 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:29:18,895 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:29:19,535 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:29:19,535 [INFO]    âšª No signal - HOLD
2025-12-06 09:29:20,036 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:29:20,120 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:29:20,747 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:29:20,747 [INFO]    âšª No signal - HOLD
2025-12-06 09:29:21,248 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:29:21,334 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:29:22,032 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:29:22,032 [INFO]    âšª No signal - HOLD
2025-12-06 09:29:22,533 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:29:22,616 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:29:23,254 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:29:23,254 [INFO]    âšª No signal - HOLD
2025-12-06 09:29:23,755 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:29:23,843 [INFO]    Current position: LONG 0.69
2025-12-06 09:29:23,843 [INFO]    Entry: $145.48 | Mark: $132.43
2025-12-06 09:29:23,843 [INFO]    PnL: -89.71% ($-9.00)
2025-12-06 09:29:23,843 [INFO]    Age: 55.9h / 72.0h
2025-12-06 09:29:24,344 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:29:24,432 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:29:25,113 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:29:25,113 [INFO]    âšª No signal - HOLD
2025-12-06 09:29:25,614 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:29:25,701 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:29:26,373 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:29:26,374 [INFO]    âšª No signal - HOLD
2025-12-06 09:29:26,874 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:29:26,958 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:29:27,647 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 11/15
2025-12-06 09:29:27,647 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:29:27,647 [INFO]    âš ï¸ Near EMA21
2025-12-06 09:29:27,647 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:29:27,647 [INFO]    âš¡ RSI acceptable range
2025-12-06 09:29:27,647 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:29:27,647 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:29:27,652 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:29:27,652 [INFO]    âšª No signal - HOLD
2025-12-06 09:29:28,153 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:29:28,241 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:29:29,042 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:29:29,042 [INFO]    âšª No signal - HOLD
2025-12-06 09:29:29,042 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:32:29,136 [INFO] 
============================================================
2025-12-06 09:32:29,137 [INFO] ðŸ”„ LOOP #35 - 2025-12-06 09:32:29
2025-12-06 09:32:29,137 [INFO] ============================================================
2025-12-06 09:32:30,167 [INFO] ðŸ’“ Bot alive - Loop #35 - Active positions: 2
2025-12-06 09:32:30,256 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:32:30,256 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:32:30,341 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:32:31,200 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:32:31,200 [INFO]    âšª No signal - HOLD
2025-12-06 09:32:31,701 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:32:31,784 [INFO]    Current position: LONG 0.11
2025-12-06 09:32:31,784 [INFO]    Entry: $924.70 | Mark: $882.43
2025-12-06 09:32:31,784 [INFO]    PnL: -45.71% ($-4.65)
2025-12-06 09:32:31,784 [INFO]    Age: 55.1h / 72.0h
2025-12-06 09:32:32,285 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:32:32,368 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:32:33,033 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:32:33,034 [INFO]    âšª No signal - HOLD
2025-12-06 09:32:33,535 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:32:33,621 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:32:34,254 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:32:34,255 [INFO]    âšª No signal - HOLD
2025-12-06 09:32:34,755 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:32:34,843 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:32:35,511 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:32:35,511 [INFO]    âšª No signal - HOLD
2025-12-06 09:32:36,012 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:32:36,096 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:32:36,892 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:32:36,892 [INFO]    âšª No signal - HOLD
2025-12-06 09:32:37,393 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:32:37,611 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:32:38,267 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:32:38,268 [INFO]    âšª No signal - HOLD
2025-12-06 09:32:38,768 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:32:38,851 [INFO]    Current position: LONG 0.69
2025-12-06 09:32:38,851 [INFO]    Entry: $145.48 | Mark: $132.47
2025-12-06 09:32:38,852 [INFO]    PnL: -89.39% ($-8.97)
2025-12-06 09:32:38,852 [INFO]    Age: 55.9h / 72.0h
2025-12-06 09:32:39,352 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:32:39,434 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:32:40,068 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:32:40,069 [INFO]    âšª No signal - HOLD
2025-12-06 09:32:40,569 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:32:40,659 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:32:41,416 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:32:41,416 [INFO]    âšª No signal - HOLD
2025-12-06 09:32:41,917 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:32:42,003 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:32:42,659 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 12/15
2025-12-06 09:32:42,659 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:32:42,659 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 09:32:42,659 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:32:42,660 [INFO]    âš¡ RSI acceptable range
2025-12-06 09:32:42,660 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:32:42,660 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:32:42,664 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:32:42,664 [INFO]    âšª No signal - HOLD
2025-12-06 09:32:43,165 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:32:43,249 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:32:44,174 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:32:44,175 [INFO]    âšª No signal - HOLD
2025-12-06 09:32:44,175 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:35:44,259 [INFO] 
============================================================
2025-12-06 09:35:44,259 [INFO] ðŸ”„ LOOP #36 - 2025-12-06 09:35:44
2025-12-06 09:35:44,259 [INFO] ============================================================
2025-12-06 09:35:44,346 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:35:44,346 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:35:44,427 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:35:45,052 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:35:45,053 [INFO]    âšª No signal - HOLD
2025-12-06 09:35:45,553 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:35:45,637 [INFO]    Current position: LONG 0.11
2025-12-06 09:35:45,637 [INFO]    Entry: $924.70 | Mark: $882.34
2025-12-06 09:35:45,637 [INFO]    PnL: -45.81% ($-4.66)
2025-12-06 09:35:45,637 [INFO]    Age: 55.1h / 72.0h
2025-12-06 09:35:46,138 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:35:46,220 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:35:46,857 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:35:46,857 [INFO]    âšª No signal - HOLD
2025-12-06 09:35:47,358 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:35:47,445 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:35:48,057 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:35:48,057 [INFO]    âšª No signal - HOLD
2025-12-06 09:35:48,558 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:35:48,644 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:35:49,413 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:35:49,414 [INFO]    âšª No signal - HOLD
2025-12-06 09:35:49,914 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:35:49,997 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:35:50,665 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:35:50,665 [INFO]    âšª No signal - HOLD
2025-12-06 09:35:51,166 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:35:51,258 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:35:51,905 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:35:51,905 [INFO]    âšª No signal - HOLD
2025-12-06 09:35:52,406 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:35:52,490 [INFO]    Current position: LONG 0.69
2025-12-06 09:35:52,490 [INFO]    Entry: $145.48 | Mark: $132.37
2025-12-06 09:35:52,490 [INFO]    PnL: -90.10% ($-9.04)
2025-12-06 09:35:52,490 [INFO]    Age: 56.0h / 72.0h
2025-12-06 09:35:52,991 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:35:53,076 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:35:53,721 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:35:53,722 [INFO]    âšª No signal - HOLD
2025-12-06 09:35:54,222 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:35:54,307 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:35:54,953 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:35:54,953 [INFO]    âšª No signal - HOLD
2025-12-06 09:35:55,454 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:35:55,543 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:35:56,180 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 12/15
2025-12-06 09:35:56,180 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:35:56,180 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 09:35:56,180 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:35:56,180 [INFO]    âš¡ RSI acceptable range
2025-12-06 09:35:56,180 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:35:56,181 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:35:56,186 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:35:56,186 [INFO]    âšª No signal - HOLD
2025-12-06 09:35:56,687 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:35:56,773 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:35:57,401 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:35:57,401 [INFO]    âšª No signal - HOLD
2025-12-06 09:35:57,401 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:38:57,493 [INFO] 
============================================================
2025-12-06 09:38:57,494 [INFO] ðŸ”„ LOOP #37 - 2025-12-06 09:38:57
2025-12-06 09:38:57,494 [INFO] ============================================================
2025-12-06 09:38:57,581 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:38:57,581 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:38:57,667 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:38:58,361 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:38:58,361 [INFO]    âšª No signal - HOLD
2025-12-06 09:38:58,862 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:38:58,944 [INFO]    Current position: LONG 0.11
2025-12-06 09:38:58,944 [INFO]    Entry: $924.70 | Mark: $883.15
2025-12-06 09:38:58,944 [INFO]    PnL: -44.93% ($-4.57)
2025-12-06 09:38:58,944 [INFO]    Age: 55.2h / 72.0h
2025-12-06 09:38:59,445 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:38:59,525 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:39:00,188 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:39:00,188 [INFO]    âšª No signal - HOLD
2025-12-06 09:39:00,689 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:39:00,777 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:39:01,463 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 12/15
2025-12-06 09:39:01,464 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:39:01,464 [INFO]    âš ï¸ Near EMA21
2025-12-06 09:39:01,464 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:39:01,464 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 09:39:01,464 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:39:01,464 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:39:01,469 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:39:01,470 [INFO]    âšª No signal - HOLD
2025-12-06 09:39:01,971 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:39:02,057 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:39:02,789 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:39:02,789 [INFO]    âšª No signal - HOLD
2025-12-06 09:39:03,290 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:39:03,376 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:39:04,068 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:39:04,068 [INFO]    âšª No signal - HOLD
2025-12-06 09:39:04,571 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:39:04,658 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:39:05,544 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:39:05,544 [INFO]    âšª No signal - HOLD
2025-12-06 09:39:06,045 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:39:06,132 [INFO]    Current position: LONG 0.69
2025-12-06 09:39:06,132 [INFO]    Entry: $145.48 | Mark: $132.51
2025-12-06 09:39:06,133 [INFO]    PnL: -89.15% ($-8.95)
2025-12-06 09:39:06,133 [INFO]    Age: 56.1h / 72.0h
2025-12-06 09:39:06,633 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:39:06,718 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:39:07,426 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:39:07,427 [INFO]    âšª No signal - HOLD
2025-12-06 09:39:07,928 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:39:08,013 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:39:08,698 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:39:08,698 [INFO]    âšª No signal - HOLD
2025-12-06 09:39:09,199 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:39:09,282 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:39:10,117 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:39:10,117 [INFO]    âšª No signal - HOLD
2025-12-06 09:39:10,618 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:39:10,705 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:39:11,376 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:39:11,377 [INFO]    âšª No signal - HOLD
2025-12-06 09:39:11,377 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:42:11,431 [INFO] 
============================================================
2025-12-06 09:42:11,431 [INFO] ðŸ”„ LOOP #38 - 2025-12-06 09:42:11
2025-12-06 09:42:11,432 [INFO] ============================================================
2025-12-06 09:42:11,521 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:42:11,521 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:42:11,607 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:42:12,269 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:42:12,269 [INFO]    âšª No signal - HOLD
2025-12-06 09:42:12,769 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:42:12,853 [INFO]    Current position: LONG 0.11
2025-12-06 09:42:12,853 [INFO]    Entry: $924.70 | Mark: $883.21
2025-12-06 09:42:12,853 [INFO]    PnL: -44.87% ($-4.56)
2025-12-06 09:42:12,853 [INFO]    Age: 55.2h / 72.0h
2025-12-06 09:42:13,354 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:42:13,438 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:42:14,109 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:42:14,109 [INFO]    âšª No signal - HOLD
2025-12-06 09:42:14,610 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:42:14,692 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:42:15,332 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 12/15
2025-12-06 09:42:15,332 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:42:15,332 [INFO]    âš ï¸ Near EMA21
2025-12-06 09:42:15,333 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:42:15,333 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 09:42:15,333 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:42:15,333 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:42:15,337 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:42:15,338 [INFO]    âšª No signal - HOLD
2025-12-06 09:42:15,838 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:42:15,924 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:42:16,698 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:42:16,698 [INFO]    âšª No signal - HOLD
2025-12-06 09:42:17,199 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:42:17,289 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:42:17,980 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:42:17,980 [INFO]    âšª No signal - HOLD
2025-12-06 09:42:18,481 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:42:18,566 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:42:19,224 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:42:19,224 [INFO]    âšª No signal - HOLD
2025-12-06 09:42:19,725 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:42:19,810 [INFO]    Current position: LONG 0.69
2025-12-06 09:42:19,810 [INFO]    Entry: $145.48 | Mark: $132.60
2025-12-06 09:42:19,810 [INFO]    PnL: -88.53% ($-8.89)
2025-12-06 09:42:19,810 [INFO]    Age: 56.1h / 72.0h
2025-12-06 09:42:20,311 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:42:20,402 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:42:21,149 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:42:21,149 [INFO]    âšª No signal - HOLD
2025-12-06 09:42:21,650 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:42:21,735 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:42:22,391 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:42:22,391 [INFO]    âšª No signal - HOLD
2025-12-06 09:42:22,892 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:42:22,981 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:42:23,658 [INFO] ðŸŽ¯ AVAXUSDT SHORT Signal | Score: 12/15
2025-12-06 09:42:23,658 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:42:23,659 [INFO]    âš ï¸ Near EMA21
2025-12-06 09:42:23,659 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:42:23,659 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 09:42:23,659 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:42:23,659 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:42:23,668 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:42:23,668 [INFO]    âšª No signal - HOLD
2025-12-06 09:42:24,169 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:42:24,253 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:42:24,913 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:42:24,913 [INFO]    âšª No signal - HOLD
2025-12-06 09:42:24,914 [INFO] 
ðŸ’¤ Sleeping 180s...
2025-12-06 09:45:25,014 [INFO] 
============================================================
2025-12-06 09:45:25,015 [INFO] ðŸ”„ LOOP #39 - 2025-12-06 09:45:25
2025-12-06 09:45:25,015 [INFO] ============================================================
2025-12-06 09:45:25,108 [INFO] ðŸ’° Current balance: $29.10
2025-12-06 09:45:25,108 [INFO] 
ðŸ“Š Processing ADAUSDT...
2025-12-06 09:45:25,193 [INFO]    ðŸ” Analyzing ADAUSDT for entry signal...
2025-12-06 09:45:25,920 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:45:25,921 [INFO]    âšª No signal - HOLD
2025-12-06 09:45:26,422 [INFO] 
ðŸ“Š Processing BNBUSDT...
2025-12-06 09:45:26,504 [INFO]    Current position: LONG 0.11
2025-12-06 09:45:26,504 [INFO]    Entry: $924.70 | Mark: $882.91
2025-12-06 09:45:26,504 [INFO]    PnL: -45.20% ($-4.60)
2025-12-06 09:45:26,504 [INFO]    Age: 55.3h / 72.0h
2025-12-06 09:45:27,005 [INFO] 
ðŸ“Š Processing DOGEUSDT...
2025-12-06 09:45:27,094 [INFO]    ðŸ” Analyzing DOGEUSDT for entry signal...
2025-12-06 09:45:27,768 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:45:27,768 [INFO]    âšª No signal - HOLD
2025-12-06 09:45:28,269 [INFO] 
ðŸ“Š Processing UNIUSDT...
2025-12-06 09:45:28,352 [INFO]    ðŸ” Analyzing UNIUSDT for entry signal...
2025-12-06 09:45:29,017 [INFO] ðŸŽ¯ UNIUSDT SHORT Signal | Score: 11/15
2025-12-06 09:45:29,018 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:45:29,018 [INFO]    âš ï¸ Near EMA21
2025-12-06 09:45:29,018 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:45:29,018 [INFO]    âš¡ RSI acceptable range
2025-12-06 09:45:29,018 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:45:29,018 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:45:29,023 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:45:29,024 [INFO]    âšª No signal - HOLD
2025-12-06 09:45:29,524 [INFO] 
ðŸ“Š Processing LINKUSDT...
2025-12-06 09:45:29,612 [INFO]    ðŸ” Analyzing LINKUSDT for entry signal...
2025-12-06 09:45:30,261 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:45:30,262 [INFO]    âšª No signal - HOLD
2025-12-06 09:45:30,763 [INFO] 
ðŸ“Š Processing BTCUSDT...
2025-12-06 09:45:30,850 [INFO]    ðŸ” Analyzing BTCUSDT for entry signal...
2025-12-06 09:45:31,628 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:45:31,628 [INFO]    âšª No signal - HOLD
2025-12-06 09:45:32,129 [INFO] 
ðŸ“Š Processing ETHUSDT...
2025-12-06 09:45:32,210 [INFO]    ðŸ” Analyzing ETHUSDT for entry signal...
2025-12-06 09:45:32,859 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:45:32,860 [INFO]    âšª No signal - HOLD
2025-12-06 09:45:33,361 [INFO] 
ðŸ“Š Processing SOLUSDT...
2025-12-06 09:45:33,447 [INFO]    Current position: LONG 0.69
2025-12-06 09:45:33,447 [INFO]    Entry: $145.48 | Mark: $132.61
2025-12-06 09:45:33,447 [INFO]    PnL: -88.47% ($-8.88)
2025-12-06 09:45:33,448 [INFO]    Age: 56.2h / 72.0h
2025-12-06 09:45:33,948 [INFO] 
ðŸ“Š Processing XRPUSDT...
2025-12-06 09:45:34,031 [INFO]    ðŸ” Analyzing XRPUSDT for entry signal...
2025-12-06 09:45:34,825 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:45:34,825 [INFO]    âšª No signal - HOLD
2025-12-06 09:45:35,326 [INFO] 
ðŸ“Š Processing DOTUSDT...
2025-12-06 09:45:35,415 [INFO]    ðŸ” Analyzing DOTUSDT for entry signal...
2025-12-06 09:45:36,069 [INFO] ðŸŽ¯ DOTUSDT SHORT Signal | Score: 13/15
2025-12-06 09:45:36,069 [INFO]    âœ… Perfect alignment: All TFs DOWN
2025-12-06 09:45:36,069 [INFO]    âœ… Perfect pullback to EMA21
2025-12-06 09:45:36,069 [INFO]    ðŸ”‘ At swing low (support)
2025-12-06 09:45:36,069 [INFO]    âš¡ RSI neutral (good for entry)
2025-12-06 09:45:36,069 [INFO]    ðŸŒ London session (high liquidity)
2025-12-06 09:45:36,069 [INFO]    âœ… R:R = 2.0:1
2025-12-06 09:45:36,074 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:45:36,074 [INFO]    âšª No signal - HOLD
2025-12-06 09:45:36,575 [INFO] 
ðŸ“Š Processing AVAXUSDT...
2025-12-06 09:45:36,662 [INFO]    ðŸ” Analyzing AVAXUSDT for entry signal...
2025-12-06 09:45:37,442 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:45:37,442 [INFO]    âšª No signal - HOLD
2025-12-06 09:45:37,943 [INFO] 
ðŸ“Š Processing NEARUSDT...
2025-12-06 09:45:38,025 [INFO]    ðŸ” Analyzing NEARUSDT for entry signal...
2025-12-06 09:45:38,699 [INFO]    ðŸ“Š Analysis complete: Signal=HOLD, Score=0
2025-12-06 09:45:38,700 [INFO]    âšª No signal - HOLD
2025-12-06 09:45:38,700 [INFO] 
ðŸ’¤ Sleeping 180s...
