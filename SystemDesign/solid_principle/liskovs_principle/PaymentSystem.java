package solid_principle.liskovs_principle;

public class PaymentSystem {
    public void makePayment(double amount, PaymentMethod paymentMethod) {
        paymentMethod.processPayment(amount);
    }
}
