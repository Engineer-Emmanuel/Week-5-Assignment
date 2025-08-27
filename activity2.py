// Activity 2: Polymorphism Challenge

// Base class Vehicle with generic move method
class Vehicle {
    move() {
        return "Vehicle is moving";
    }
}

// Car class overrides move()
class Car extends Vehicle {
    move() {
        return "Driving 🚗";
    }
}

// Plane class overrides move()
class Plane extends Vehicle {
    move() {
        return "Flying ✈️";
    }
}

// Animal base class
class Animal {
    move() {
        return "Animal is moving";
    }
}

// Dog class overrides move()
class Dog extends Animal {
    move() {
        return "Dog is running 🐕";
    }
}

// Fish class overrides move()
class Fish extends Animal {
    move() {
        return "Fish is swimming 🐟";
    }
}

// Test polymorphic behavior
const vehicles = [new Car(), new Plane()];
vehicles.forEach(v => console.log(v.move()));

const animals = [new Dog(), new Fish()];
animals.forEach(a => console.log(a.move()));