#Arrays

Notes extrapolated from [Js_Arrays](https://www.w3schools.com/js/js_arrays.asp) from w3Schools.com. 

##Resources

- [Complete Array Reference](https://www.w3schools.com/jsref/jsref_obj_array.asp)

- [Sorting Arrays](https://www.w3schools.com/js/js_array_sort.asp)

## Methods for recongnising an Array

Create your own isArray() function: 

``` javascript
function isArray(x) {
  return x.constructor.toString().indexOf("Array") > -1;
}
```

- This will return `true` if object prototype contains the word array. 

## Numeric sorting

sort() views values as strings. Therefore, to sort numerically use a compare function    :

```javascript
var points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return a - b});
```

reverse `return` to sort descending. 

- If the result is `negative` a is sorted before b.
- If the result is `positive` b is sorted before a.
- If the result is `0` no changes are done with the sort order of the two values.

## Max & Min

Once sorted, indexes can show max and min values.

```javascript
var points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return a - b});
// now points[0] contains the lowest value
// and points[points.length-1] contains the highest value
```

Custom function: 

`Max`:

```javascript
function myArrayMax(arr) {
  var len = arr.length
  var max = -Infinity;
  while (len--) {
    if (arr[len] > max) {
      max = arr[len];
    }
  }
  return max;
}
```

`Min`:

```javascript
function myArrayMax(arr) {
  var len = arr.length
  var min = Infinity;
  while (len--) {
    if (arr[len] > min) {
      min = arr[len];
    }
  }
  return min;
}
```

## Sorting Strings


```javascript
myArray.sort(function(a, b){
  var x = a.type.toLowerCase();
  var y = b.type.toLowerCase();
  if (x < y) {return -1;}
  if (x > y) {return 1;}
  return 0;
});
```

