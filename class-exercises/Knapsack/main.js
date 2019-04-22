const values = [4, 3, 6, 7, 2, 9, 7, 6];
const weights = [12, 16, 8, 21, 16, 11, 6, 12];

const MAX_WEIGHT = 50;
const SOLUTION_LENGTH = 8;
const POPULATION_LENGTH = 10;
const MUTATION_PROB = 0.1;
const NUM_GENERATIONS = 1000;
const SAMPLE_MIN_SIZE = 2;

const calcFitness = (sol) => {
    let val = 0;
    let weight = 0;
    for (let i in sol) {
        val += sol[i]*values[i];
        weight += sol[i]*weights[i];
    }
    
    return (weight > MAX_WEIGHT ? 0 : val); 
}

const mutate = (sol) => sol.map(val => 
    + ((Math.random() < MUTATION_PROB) ? !val : val)   
);

const cross = (sol1, sol2) => sol1.map((elem, i) => 
    Math.round(Math.random()) ? elem : sol2[i]
);

const calcBestSolution = (population) => {
    let best = population[0];
    let best_fit = calcFitness(population[0]);
    population.forEach(sol => {
        let new_fit = calcFitness(sol);
        if (new_fit > best_fit) {
            best = sol;
            best_fit = new_fit;
        }
    })
    return best;
}

const getCrossoverChild = (population) => {
    parents = [];
    for (let i = 0; i < 2; i++) {
        const shuffled = population.sort(() => 0.5 - Math.random());
        const sampleSize = Math.floor(Math.random() * (population.length - SAMPLE_MIN_SIZE)) + SAMPLE_MIN_SIZE;
        const sample = shuffled.slice(0, sampleSize);
        const bestSol = calcBestSolution(sample);
        parents.push(bestSol);
    }
    return cross(parents[0], parents[1]);
}

const generateRandomPopulation = () => {
    let population = [];
    for (let i = 0; i < POPULATION_LENGTH; i++) {
        let sol = [];
        for (let j = 0; j < SOLUTION_LENGTH; j++) {
            sol.push(Math.round(Math.random()));
        }
        population.push(sol);
    }
    return population;
}

const computeNextGeneration = (population) => population.map(sol => {
    const child = getCrossoverChild(population);
    const mutated_child = mutate(child);
    return mutated_child;
});

let population = generateRandomPopulation();
console.log("Initial: ", calcFitness(calcBestSolution(population)));
for (let i = 0; i < NUM_GENERATIONS; i++) {
    population = computeNextGeneration(population);
}
console.log("Final: ", calcFitness(calcBestSolution(population)));
