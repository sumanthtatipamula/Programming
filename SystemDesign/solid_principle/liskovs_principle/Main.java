package solid_principle.liskovs_principle;

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

