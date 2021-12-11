# FastAPI+SvelteでWebSocketを動かしてみた

## frontendをビルドする
frontendのモジュールをビルドし、バックエンド側にビルド結果を出力する
```
cd fastapi_websocket/src/chatapp-frontend
npm run build
```

fastapi_websocket/src/chatapp/public/build　に出力される


## chatpapを起動する
chatappを起動する
```
cd fastapi_websocket/src/chatapp
uvicorn main:app --reload
```