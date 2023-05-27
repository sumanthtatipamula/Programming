package solid_principle.dependency_inversion;

public interface PaymentGateway {
    boolean processPayment(String paymentToken, double amount);
}
