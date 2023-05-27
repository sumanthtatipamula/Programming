package solid_principle.interface_segregation_principle;

public class CreditCardPayment implements OnlinePayment {
    public void processOnlinePayment() {
        // Process credit card payment online
    }
}
