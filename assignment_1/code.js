let sim;
let config = {
    ndim: 2,
    field_size: [100, 100],

    conf: {
        T: 20, //Temperature
        J: [[1000, 20], [1000, 20]], //Adhesion
        LAMBDA_V: [1000, 50], //PerimeterConstraintLambda
        V: [0, 500] //PerimeterConstraint
    },

    simsettings: {
        NRCELLS: [1],
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