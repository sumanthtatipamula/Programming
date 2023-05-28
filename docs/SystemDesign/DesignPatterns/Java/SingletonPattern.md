---
title: Singleton Design Pattern
tags:
  - Design Patterns
  - Creational
---

## Introduction

- Deals with object creation mechanism.

- It is used when we want to have only one object of a particular class.

- An application may require multiple object instances that all use one unique resource. This fact introduces instability because any of these objects can access such a resource. A singleton guarantees only one instance that provides a global access point to all clients within the desired scope of the running JVM.

## Real Time Usage in JDK

- The best example of using a singleton is a running Java application, or more precisely, the runtime. It is found in the _Runtime_ class and its method, _getRuntime_, resides in the **java.lang** package of the **java.base** module. The method returns an object associated with the current Java application. The runtime instance allows the client to add, for example, shutdown hooks to the running application.

## Implementation

- Make the constructor private - helps in restricting object creation outside of the class.

-
