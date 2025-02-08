# Assignment 1 

1. We can make an obstacle simply making sure that the cell does not move. We do this by setting a Volume (let's say 500), setting the Lambda_V very high (so it keeps it shape very well and does not move), and in the adhesion matrix we make the adhesion to all other cells high (so the other cells will avoid the obstacle instead of "sticking to it").
```js
conf: {
        T: 20,                              //Temperature
        J: [
            [0, 20, 1000],                  //Adhesion background cells
            [20, 100, 1000],                //Adhesion for moving cells
            [1000, 1000, 1000]              //Adhesion for obstacle
        ],                                  
        LAMBDA_V: [0, 50, 1000],            //High obstacle, not moving
        V: [0, 100, 500],                   //Volume of obstacle is 500
    },
```

2. Done
```js
    conf: {
        T: 20,                              
        J: [
            [0, 20],                  
            [20, 0]                    
        ],                                  
        LAMBDA_V: [0, 50],   
        V: [0, 200],
        LAMBDA_P: [0, 2],
        P: [0, 180],
        MAX_ACT: [0, 50],
        ACT_MEAN: "geometric",
        LAMBDA_ACT: [0, 200],               
    },
```