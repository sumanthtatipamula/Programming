package solid_principle.dependency_inversion;

public class StripeGateway implements PaymentGateway {
    public boolean processPayment(String paymentToken, double amount) {
        // Implementation specific to Stripe payment gateway
        // Process the payment using the Stripe API
        return true; // Payment successful
    }
}
