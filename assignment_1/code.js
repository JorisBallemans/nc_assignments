let sim;
let config = {
    ndim: 2,
    field_size: [100, 100],

    // Part 1
    // conf: {
    //     T: 20,                              //Temperature
    //     J: [
    //         [0, 20, 1000],                  //Adhesion background cells
    //         [20, 100, 1000],                //Adhesion for moving cells
    //         [1000, 1000, 1000]              //Adhesion for obstacle
    //     ],                                  
    //     LAMBDA_V: [0, 50, 1000],            //High obstacle, not moving
    //     V: [0, 100, 500],                   //Volume of obstacle is 500
    //     MAX_ACT: [0, 100, 1000],            //Maximal volume of cells
    //     ACT_MEAN: "geometric",              
    //     LAMBDA_ACT: [0, 100, 1000],         //Volume constraint
    // },

    // Part 2
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

    simsettings: {
        NRCELLS: [10],
        RUNTIME: 500,
        CANVASCOLOR: "eaecef",
        zoom: 4	
    }
}

function init() {
    sim = new CPM.Simulation(config)
    sim.run()
    step()
}

function step() {
    sim.step()
    requestAnimationFrame(step)
}