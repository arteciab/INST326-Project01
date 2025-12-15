# Project 3 Architecture Summary

This document explains the required advanced object oriented features added in Project 3 and the design choices behind them.

## Inheritance Hierarchy

We created one inheritance hierarchy for different race types:

- `AbstractRaceData` (base class)
- `NASCARData`
- `F1Data`
- `IndyCarData`

The subclasses share the same core structure but specialize the scoring behavior. This reflects a real is a relationship between race types.

## Abstract Base Class

`AbstractRaceData` is an abstract class that defines:

- `race_name`
- `laps`
- a required method `compute_performance_score()`

Every subclass must override this method, which keeps the system consistent.

## Polymorphism

All subclasses implement `compute_performance_score()`, but each one returns a different result:

- NASCAR uses laps times 1.2  
- F1 uses laps times 2.5  
- IndyCar uses laps times 1.8  

When race objects are stored together and looped over, the same method call produces different behavior. This demonstrates polymorphism.

## Composition

`RaceManager` shows composition since it stores race objects rather than inheriting from them. It can:

- add races  
- list races  
- compute a total combined score  

Composition was chosen because a manager is not a race type.

## Summary

Project 3 adds:

- one abstract base class  
- an inheritance hierarchy with three subclasses  
- polymorphic scoring behavior  
- a composition based manager  

All features were verified using the tests in the tests folder.
