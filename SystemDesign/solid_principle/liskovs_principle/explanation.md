### Interfaces and Payment Method Classes:
- The `PaymentMethod` interface defines the contract that all payment methods must adhere to. It declares the `processPayment()` method, responsible for processing a payment with a specific payment method.
- Each payment method is implemented as a separate class that implements the `PaymentMethod` interface. In this example, we have three payment method classes: `CreditCardPayment`, `BankTransferPayment`, and `EWalletPayment`.
- Each payment method class contains specific data and logic related to that payment method. For example, the `CreditCardPayment` class stores the credit card number, cardholder name, expiry date, and CVV. The `BankTransferPayment` class stores the account number and bank code. The `EWalletPayment` class stores the e-wallet ID and password.

### PaymentSystem Class:
- The `PaymentSystem` class represents the core of the payment system. It contains the `makePayment()` method, responsible for handling the payment processing.
- The `makePayment()` method takes two parameters: the payment amount (`double`) and the selected payment method (`PaymentMethod`).
- Inside the `makePayment()` method, the `processPayment()` method of the selected payment method is called to perform the actual payment processing.
- By using the `PaymentMethod` interface as the parameter type, the `PaymentSystem` class can work with any class that implements the `PaymentMethod` interface, providing flexibility and extensibility to support new payment methods in the future.

### Main Class:
- The `Main` class serves as the entry point of the program and demonstrates how the payment system is used.
- In the `main()` method, an instance of the `PaymentSystem` class is created.
- Instances of different payment methods (`CreditCardPayment`, `BankTransferPayment`, and `EWalletPayment`) are created, representing different ways users can make payments.
- The `makePayment()` method is called on the `PaymentSystem` instance, passing the payment amount and the respective payment method as arguments.
- The payment system then delegates the payment processing to the appropriate payment method based on the provided `PaymentMethod` object.

### How Liskov's Principle is handled.

1. **Interface Contract**: The `PaymentMethod` interface establishes a contract that all payment methods must adhere to. It declares the `processPayment()` method, responsible for processing a payment. By defining this common method in the interface, it ensures that any class implementing the interface can be used interchangeably wherever a `PaymentMethod` object is expected. This adherence to a common contract is a key aspect of the LSP.

2. **Behavior Preservation**: The `PaymentMethod` interface guarantees that any class implementing it will provide the necessary behavior for processing a payment. This means that each payment method class (`CreditCardPayment`, `BankTransferPayment`, `EWalletPayment`) must implement the `processPayment()` method according to its specific requirements. Each implementation is responsible for performing the actual payment processing logic relevant to that payment method.

3. **Substitutability**: The payment system, represented by the `PaymentSystem` class, relies on the `PaymentMethod` interface for its functionality. The `makePayment()` method of the `PaymentSystem` class accepts any object that implements the `PaymentMethod` interface as its second argument. This demonstrates substitutability, as different payment method objects (`CreditCardPayment`, `BankTransferPayment`, `EWalletPayment`) can be passed to the `makePayment()` method without impacting the correctness or behavior of the system.

By adhering to the Liskov Substitution Principle, the payment system example ensures that any new payment method can be added by implementing the `PaymentMethod` interface, and it can seamlessly integrate into the system without breaking its functionality or causing unexpected behavior. This design approach promotes modularity, extensibility, and flexibility in the payment system, while maintaining a consistent interface contract for all payment methods.

Note: **In order to add new method, to the existing class or new class in that case we need to create new interface.**


