title: Introduction
output: ../../out/session2/hello-$.html
controls: false

--

# Introduction to JQuery

--

### JQuery

JQuery is a Javascript library which makes it easier to manipulate the DOM

---

### Initializing the Document

```javascript

$( document ).ready(function() {
  // your code here
});

$(function(){
	// your code here
});

```

---

### Selecting elements

```javascript

$('li'); //selects all list elements
$('#Home');
$('.home');

$('li')[0]; //first selected list element

```

---

### Modifing elements

```javascript
$('li').html('batee5');
```

---

### Events

listening to events is an integral part of Javascript

```javascript
$('input').on('click', function(event){
	$(this).css('background-color', 'red');
	console.log('clicked')
});

$('input').on('change', function(event){
	console.log($(this).val())
});

```

---

### Simple Animations

```javascript
$('input').on('click', function(event){
	$('li').hide(1000);
	$('li').show(1000);
});

```

