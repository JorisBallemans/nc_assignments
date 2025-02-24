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

   <img src="https://github.com/user-attachments/assets/da09e6b7-47d8-48d3-b834-b812de317a6b" width="200"/>
  
4. We notice various behaviour changes

   
   **Obstacle movement:** The cells still move around the grid but considerably slower. When encountering an obstacle they often stop for a while as their movement direction is now obstructed.

    Sometimes they also get stuck around an obstacle if it is directly in the middle of their movement direction, as seen in the left middle of this picture:
   
   <img src="https://github.com/user-attachments/assets/a8af7ff3-124d-44cc-b52a-7724e2169c05" width="200"/>
   
   **Obstacle density reactions:** Our base obstacle density was half the cell volume.

   We have also experimented with a factor 4 smaller (compared to cell volume):

   <img src="https://github.com/user-attachments/assets/2471f375-5b25-4ab4-b560-21aba9a5ad1b" width="200"/>

   This resulted in much freer movement of the cells, The previous getting stuck behaviour when an obstacle was in the middle of the cell no longer occured.

   At 75% obstacle volume we noticed considerable clumping and fewer movements.

   <img src="https://github.com/user-attachments/assets/883c404a-275a-4758-b784-939f10af49c5" width ="200"/>
   
   
   and any obstacle as big as the cells themselves or bigger obstruced lanes and gave no movement possibilities at all:

   <img src="https://github.com/user-attachments/assets/fab8b30f-e2e8-4bc1-9aa3-046f62763bff" width="200"/>
   
5. Where the cells could continue moving in their preferred direction in the base simulation, this changed considerably when they were introduced to obstacles. We found cells **staying near obstacles**, struggling to continue their path. We also noticed cells **clumping around obsacles**, where a larger group would stay together. After a while these groups sometimes resolved. A typical simulation often had two situations concurrenctly: **some cells moving freely while other cells were clumped together not moving**.
   The following picure shows examples of all these occuring:
   
   <img src="https://github.com/user-attachments/assets/9a4d4bb3-8aa8-4bce-a684-5e193a0c5d61" width="200"/>

<<<<<<< HEAD

=======
7. / 
>>>>>>> e4795955e934352d79b31d2477552e946b503749
