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

2. We examined two parameter sets in 1.3. One with Max_Act set to 20 and one with with Max_Act set to 80. At 20 we saw cells moving in all directions and clumping together when meeting other cells. When enough cells were together there was very litlle movement. For the other parameter setting of 80 we saw different behaviour. Cells had more directional movement and would continue moving, even when faced with higher densities.
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
        MAX_ACT: [0, 80],
        ACT_MEAN: "geometric",
        LAMBDA_ACT: [0, 200],               
    },
```

3. Experiment setup is in `experiment.html`. We implemented an even spaced obstacle grid with migrating cells navigating between these obstacles.
 ![afbeelding](https://github.com/user-attachments/assets/da09e6b7-47d8-48d3-b834-b812de317a6b)


5. 
