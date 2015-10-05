title: Introduction
output: ../../out/session2/hello-js.html
controls: false

--

# Introduction to Javascript

--

### Javascript

javascript is an interpreted programming language, and its run on the browser. used to modify DOM add animations ...etc

---

### Syntax: Variables

you don't define the variable type in Javascript, its automatically done.

```javascript
var cool = "batee5";
var ten = 10;

foo = "bar"; // this is a global variable

console.log(cool); //logs the value of cool
alert(ten); //makes an alert

```

---

### Syntax: Functions

```javascript
var add = function(a,b) {
	return a+b;
}
```

---

### Syntax: Functions - Async

```javascript
var addAsync = function(a,b,first){
	first();
	return a+b;
}

console.log(addAsync(1,2,function(){
	alert("in the function");
}));
```

---

### Syntax: Objects

everything in javascript is an object

```javascript
var person = {
	firstname : "John",
	lastname : "Doe",
	friends: ["Jane Doe", "Some Person"]
};

person.firstname; // "John"
person["lastname"] // "Doe"

person.friends[0] // "Jane Doe"

```

---

### Syntax: Object Methods

```javascript
var person = {
	firstname : "John",
	lastname : "Doe",
	friends: ["Jane Doe", "Some Person"],
	logName: function(){
		console.log(this.firstname + " " + this.lastname);
	}
};

person.logName();

```

---

### Syntax: Other

- if statement and for loop are exactly like c++

- equality operator is ===