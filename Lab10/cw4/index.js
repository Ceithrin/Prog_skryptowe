import {Operation} from "./mymodule.js";

const operation = new Operation(parseInt(process.argv[2]), parseInt(process.argv[3]));
const suma = operation.sum()
console.log(suma)