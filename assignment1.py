// Assignment 1: Design Your Own Class (Smartphone example)

// Base class representing a generic smartphone
class Smartphone {
    constructor(brand, model, storageGB, color) {
        this.brand = brand;
        this.model = model;
        this.storageGB = storageGB;
        this.color = color;
    }

    // Method to display basic info
    info() {
        return `${this.brand} ${this.model} with ${this.storageGB}GB storage in ${this.color}`;
    }

    // Method simulating making a call
    makeCall(number) {
        return `Calling ${number} from ${this.brand} ${this.model}...`;
    }
}

// Inherited class representing a smartphone with 5G capability
class Smartphone5G extends Smartphone {
    constructor(brand, model, storageGB, color, supports5G) {
        super(brand, model, storageGB, color);
        this.supports5G = supports5G;
    }

    // Override info to include 5G support info (polymorphism)
    info() {
        let baseInfo = super.info();
        return `${baseInfo} | 5G Support: ${this.supports5G ? 'Yes' : 'No'}`;
    }
}

// Example usage
const phone1 = new Smartphone("Apple", "iPhone 14", 128, "Midnight");
const phone2 = new Smartphone5G("Samsung", "Galaxy S21", 256, "Phantom Gray", true);

console.log(phone1.info());
console.log(phone1.makeCall("123-456-7890"));

console.log(phone2.info());
console.log(phone2.makeCall("098-765-4321"));