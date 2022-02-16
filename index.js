import { handler } from './build/handler.js';
import express from 'express';

const PORT = 80
const app = express();



app.use(handler);

app.listen(PORT, () => {
	console.log(`Server avviato con successo sulla porta ${PORT}\n`);
	console.log("Per accedere al sito, digitare http://locahost su un browser");
});