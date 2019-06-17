#Javascript

##Arrays

Notes extrapolated from [Js_Arrays](https://www.w3schools.com/js/js_arrays.asp) from w3Schools.com. 

## Methods for recongnising an Array

Create your own isArray() function: 

``` javascript
function isArray(x) {
  return x.constructor.toString().indexOf("Array") > -1;
}
```

- This will return `true` if object prototype contains the word array. 
