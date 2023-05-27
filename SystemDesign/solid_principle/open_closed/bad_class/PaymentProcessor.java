package solid_principle.open_closed.bad_class;

/***
 * Consider a system that processes payments using different payment methods,
 * such as credit card, PayPal, and bank transfer.
 * Initially, the payment logic is implemented within a single class:
 */
public class PaymentProcessor {
    /**
     * The processPayment() method in the PaymentProcessor class checks the payment method type
     * and performs the corresponding payment processing logic.
     * However, if a new payment method is introduced,
     * we would need to modify the PaymentProcessor class,
     * violating the Open-Closed Principle.
     * @param paymentMethod
     */
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

