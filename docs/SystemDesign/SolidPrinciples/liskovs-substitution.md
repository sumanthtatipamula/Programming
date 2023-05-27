---
title: Liskov's Substitution Principle
tags:
  - Design Principles
  - System Design
  - Basics
  - SOLID
---

## Introduction

Liskov's Substitution Principle (LSP) states that objects of a superclass should be substitutable with objects of its subclasses without affecting the correctness of the program. In other words, if a program is designed to work with a certain type, it should also work correctly with any subtype of that type.

More formally, the principle can be defined as follows:

> Let q(x) be a property provable about objects x of type T. Then q(y) should be provable for objects y of type S, where S is a subtype of T.

## Example

### Interfaces and Payment Method Classes:

- The `PaymentMethod` interface defines the contract that all payment methods must adhere to. It declares the `processPayment()` method, responsible for processing a payment with a specific payment method.

```java
public interface PaymentMethod {
    void processPayment(double amount);
}
```

- Each payment method is implemented as a separate class that implements the `PaymentMethod` interface. In this example, we have three payment method classes: `CreditCardPayment`, `BankTransferPayment`, and `EWalletPayment`.

```java
package solid_principles.liskovs_principle;

public class CreditCardPayment implements CreditCardAdditional {
    private String cardNumber;
    private String cardHolderName;
    private String expiryDate;
    private String cvv;

    public CreditCardPayment(String cardNumber, String cardHolderName, String expiryDate, String cvv) {
        this.cardNumber = cardNumber;
        this.cardHolderName = cardHolderName;
        this.expiryDate = expiryDate;
        this.cvv = cvv;
    }

    @Override
    public void processPayment(double amount) {
        // Logic to process payment using credit card details
        System.out.println("Processing credit card payment of $" + amount);
        // Additional implementation specific to credit card payments
        // ...
    }

    @Override
    public void additionalMethod() {

    }
}
```

```java
public class EWalletPayment implements PaymentMethod {
    private String eWalletId;
    private String password;

    public EWalletPayment(String eWalletId, String password) {
        this.eWalletId = eWalletId;
        this.password = password;
    }

    @Override
    public void processPayment(double amount) {
        // Logic to process payment using e-wallet
        System.out.println("Processing e-wallet payment of $" + amount);
        // Additional implementation specific to e-wallet payments
        // ...
    }
}
```

```java
public class BankTransferPayment implements PaymentMethod {
    private String accountNumber;
    private String bankCode;

    public BankTransferPayment(String accountNumber, String bankCode) {
        this.accountNumber = accountNumber;
        this.bankCode = bankCode;
    }

    @Override
    public void processPayment(double amount) {
        // Logic to process payment via bank transfer
        System.out.println("Processing bank transfer payment of $" + amount);
        // Additional implementation specific to bank transfers
        // ...
    }
}
```

- Each payment method class contains specific data and logic related to that payment method. For example, the `CreditCardPayment` class stores the credit card number, cardholder name, expiry date, and CVV. The `BankTransferPayment` class stores the account number and bank code. The `EWalletPayment` class stores the e-wallet ID and password.

### PaymentSystem Class:

- The `PaymentSystem` class represents the core of the payment system. It contains the `makePayment()` method, responsible for handling the payment processing.
- The `makePayment()` method takes two parameters: the payment amount (`double`) and the selected payment method (`PaymentMethod`).
- Inside the `makePayment()` method, the `processPayment()` method of the selected payment method is called to perform the actual payment processing.
- By using the `PaymentMethod` interface as the parameter type, the `PaymentSystem` class can work with any class that implements the `PaymentMethod` interface, providing flexibility and extensibility to support new payment methods in the future.

```java
public class PaymentSystem {
    public void makePayment(double amount, PaymentMethod paymentMethod) {
        paymentMethod.processPayment(amount);
    }
}
```

### Main Class:

- The `Main` class serves as the entry point of the program and demonstrates how the payment system is used.
- In the `main()` method, an instance of the `PaymentSystem` class is created.
- Instances of different payment methods (`CreditCardPayment`, `BankTransferPayment`, and `EWalletPayment`) are created, representing different ways users can make payments.
- The `makePayment()` method is called on the `PaymentSystem` instance, passing the payment amount and the respective payment method as arguments.
- The payment system then delegates the payment processing to the appropriate payment method based on the provided `PaymentMethod` object.

```java
public class Main {
    public static void main(String[] args) {
        PaymentSystem paymentSystem = new PaymentSystem();

        // Credit card payment
        PaymentMethod creditCardPayment = new CreditCardPayment("1234567890123456", "John Doe", "12/25", "123");
        paymentSystem.makePayment(100.0, creditCardPayment);

        // Bank transfer payment
        PaymentMethod bankTransferPayment = new BankTransferPayment("1234567890", "ABC");
        paymentSystem.makePayment(200.0, bankTransferPayment);

        // E-wallet payment
        PaymentMethod eWalletPayment = new EWalletPayment("john.doe@example.com", "password123");
        paymentSystem.makePayment(50.0, eWalletPayment);
    }
}
```

### How Liskov's Principle is handled.

1. **Interface Contract**: The `PaymentMethod` interface establishes a contract that all payment methods must adhere to. It declares the `processPayment()` method, responsible for processing a payment. By defining this common method in the interface, it ensures that any class implementing the interface can be used interchangeably wherever a `PaymentMethod` object is expected. This adherence to a common contract is a key aspect of the LSP.

2. **Behavior Preservation**: The `PaymentMethod` interface guarantees that any class implementing it will provide the necessary behavior for processing a payment. This means that each payment method class (`CreditCardPayment`, `BankTransferPayment`, `EWalletPayment`) must implement the `processPayment()` method according to its specific requirements. Each implementation is responsible for performing the actual payment processing logic relevant to that payment method.

3. **Substitutability**: The payment system, represented by the `PaymentSystem` class, relies on the `PaymentMethod` interface for its functionality. The `makePayment()` method of the `PaymentSystem` class accepts any object that implements the `PaymentMethod` interface as its second argument. This demonstrates substitutability, as different payment method objects (`CreditCardPayment`, `BankTransferPayment`, `EWalletPayment`) can be passed to the `makePayment()` method without impacting the correctness or behavior of the system.

By adhering to the Liskov Substitution Principle, the payment system example ensures that any new payment method can be added by implementing the `PaymentMethod` interface, and it can seamlessly integrate into the system without breaking its functionality or causing unexpected behavior. This design approach promotes modularity, extensibility, and flexibility in the payment system, while maintaining a consistent interface contract for all payment methods.

Note: **In order to add new method, to the existing class or new class in that case we need to create new interface.**
