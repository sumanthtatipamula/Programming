package solid_principle.liskovs_principle;

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
