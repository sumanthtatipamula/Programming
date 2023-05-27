package solid_principle.dependency_inversion;

public class PaymentService {
    private PaymentGateway paymentGateway;
    public PaymentService(PaymentGateway paymentGateway){
        this.paymentGateway = paymentGateway;
    }
    public boolean makePayment(String paymentToken, double amount){
        return paymentGateway.processPayment(paymentToken, amount);
    }
}
