
export class Operation {
    /** 
    * Stwórz obiekt operacji 
    * @param {number} x - Wartość x.
    * @param {number} y - Wartość y.
    */
    constructor(x, y) {
        this.x = x;
        this.y = y;
      }
    /**
     * Sumuje podane przy tworzeniu klasy wartosci x i y
     * @returns {number} - wynik sumowania x i y
     */  
    sum() {
        return this.x + this.y;
    }
};
