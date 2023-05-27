---
title: Dependency Inversion Principle
tags:
  - Design Principles
  - System Design
  - Basics
  - SOLID
---

## Introduction

The Dependency Inversion Principle states that high-level modules should not depend on low-level modules. Both should depend on abstractions. This principle emphasizes the importance of designing modules and components in a way that they depend on abstractions or interfaces rather than concrete implementations. By doing so, the system becomes more flexible, maintainable, and easily testable.

## Example

The PaymentService example demonstrates the usage of Dependency Inversion Principle (DIP) and Inversion of Control (IoC) in designing a payment service.

First, we define an abstraction called `PaymentGateway` using an interface. This abstraction represents the operations related to processing payments. It includes a method `processPayment` that takes a payment token and an amount, and returns a boolean indicating whether the payment was successful.

```java
public interface PaymentGateway {
    boolean processPayment(String paymentToken, double amount);
}
```

The `PaymentService` class represents the high-level module that provides payment functionality. It depends on the `PaymentGateway` abstraction rather than a specific implementation. This dependency is injected through the constructor, following the principle of Dependency Inversion.

The `PaymentService` class has a method called `makePayment` that takes a payment token and an amount. Inside this method, the payment logic is performed, and the `PaymentGateway` abstraction is used to process the payment by calling the `processPayment` method.

```java

public class PaymentService {
    private PaymentGateway paymentGateway;
    public PaymentService(PaymentGateway paymentGateway){
        this.paymentGateway = paymentGateway;
    }
    public boolean makePayment(String paymentToken, double amount){
        return paymentGateway.processPayment(paymentToken, amount);
    }
}

```

To demonstrate the flexibility provided by DIP and IoC, we provide an implementation of the `PaymentGateway` interface called `PayPalGateway`. This class includes the specific logic to process payments using the PayPal API.

```java
public class PayPalGateway implements  PaymentGateway{

    @Override
    public boolean processPayment(String paymentToken, double amount) {
        return true;
    }
}
```

By following DIP and IoC, the `PaymentService` is decoupled from the specific implementation of the payment gateway. This allows us to easily swap the payment gateway implementation by providing a different implementation of the `PaymentGateway` interface, such as a `StripeGateway` class that processes payments using the Stripe API.

```java
public class StripeGateway implements PaymentGateway {
    public boolean processPayment(String paymentToken, double amount) {
        // Implementation specific to Stripe payment gateway
        // Process the payment using the Stripe API
        return true; // Payment successful
    }
}
```

Overall, this design promotes modularity, flexibility, and maintainability in the payment service, enabling easy integration of different payment gateways without modifying the core logic of the `PaymentService` class.
