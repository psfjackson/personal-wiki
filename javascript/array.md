#Arrays

Notes extrapolated from [Js_Arrays](https://www.w3schools.com/js/js_arrays.asp) from w3Schools.com. 

##Resources

- [Complete Array Reference](https://www.w3schools.com/jsref/jsref_obj_array.asp)

## Methods for recongnising an Array

Create your own isArray() function: 

``` javascript
function isArray(x) {
  return x.constructor.toString().indexOf("Array") > -1;
}
```

- This will return `true` if object prototype contains the word array. 

## Numeric sorting

sort() views values as strings. Therefore, to sort numerically use a compare function:

```javascript
var points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return a - b});
```

reverse `return` to sort descending. 
