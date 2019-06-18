# Loops

Notes for Javascript loops. 

## Final loop concatenation

Example of how to change last item concat. during a loop output:

```javascript
for (let i = 0; i < myArray.length; i++) {
  if (i === myArray.length - 1) {
    info += 'and ' + myArray[i] + '.';
  } else {
    info += myArray[i] + ', ';
  }
}
```

