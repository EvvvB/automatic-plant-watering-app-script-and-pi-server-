const express = require('express')
const app = express()
const port = 8080
const spawn = require("child_process").spawn
//const waterTime = spawn('python',["waterTime.py", seconds]);
const url = require('url')
const bodyParser = require('body-parser')

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use(function(req, res, next){
	res.header("Access-Control-Allow-Origin", "*");
	res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
	next();
});

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
  res.render("../pages/main.ejs")
})
app.post('/waterpump', (req, res) =>{
	let time = req.body.time
	var waterTime = spawn('python' , ["./waterTime.py", parseInt(time)])
 	res.send("Done Pi")
})
app.post('/pump/:seconds', function (req, res) {

	console.log("you posted the route")
	var seconds = req.params.seconds
	console.log("seconds:" + seconds)
	var waterTime = spawn('python' ,["./waterTime.py", parseInt(seconds)])
	res.redirect('/test')
	//waterTime.stdout.on('data',(data) => {
	//	console.log(data)
	//})

})
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)

})


