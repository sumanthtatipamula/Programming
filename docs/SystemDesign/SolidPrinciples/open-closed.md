---
title: Open for Extension Closed for Modification
tags:
  - Design Principles
  - System Design
  - Basics
  - SOLID
---

## Introduction

## Example

- Consider a system that processes payments using different payment methods, such as credit card, PayPal, and bank transfer.

### Without OCP

- The payment logic is implemented within a single class:

  ```java
  class PaymentProcessor {
      public void processPayment(String paymentMethod) {
          if (paymentMethod.equals("credit_card")) {
          // Process credit card payment logic
          } else if (paymentMethod.equals("paypal")) {
          // Process PayPal payment logic
          } else if (paymentMethod.equals("bank_transfer")) {
          // Process bank transfer logic
          }
      }
  }

  ```

- In this example, the `processPayment()` method in the `PaymentProcessor` class checks the payment method type and performs the corresponding payment processing logic. However, if a new payment method is introduced, we would need to modify the `PaymentProcessor` class, violating the Open-Closed Principle.

### Following OCP

```java
interface PaymentMethod {
  void processPayment();
}

class CreditCardPayment implements PaymentMethod {
  public void processPayment() {
    // Process credit card payment logic
  }
}

class PayPalPayment implements PaymentMethod {
  public void processPayment() {
    // Process PayPal payment logic
  }
}

class BankTransferPayment implements PaymentMethod {
  public void processPayment() {
    // Process bank transfer logic
  }
}
```

- In the improved example, we define an interface called `PaymentMethod` with a `processPayment()` method. Each specific payment method class (`CreditCardPayment`, `PayPalPayment`, `BankTransferPayment`) implements this interface and provides its own implementation of the `processPayment()` method. This allows new payment methods to be added by creating additional classes that implement the `PaymentMethod` interface, without modifying existing classes.

- By following the Open-Closed Principle, we design our systems to be open for extension by allowing new functionality to be added through inheritance or interface implementation, while closed for modification, ensuring that existing code remains unchanged.
