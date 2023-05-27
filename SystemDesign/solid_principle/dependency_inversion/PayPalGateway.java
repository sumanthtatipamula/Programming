package solid_principle.dependency_inversion;

public class PayPalGateway implements  PaymentGateway{

    @Override
    public boolean processPayment(String paymentToken, double amount) {
        return true;
    }
}
