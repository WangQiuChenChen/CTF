import java.util.Base64;

class base64 {
    public static void main(String argv[]) {
        if (argv.length == 1) {
            final Base64.Decoder decoder = Base64.getDecoder();
            final Base64.Encoder encoder = Base64.getEncoder();
            final String text = argv[0];
            final byte[] textByte = text.getBytes();
            final String encode = encoder.encodeToString(textByte);
            final String decode = new String(decoder.decode(text));
            System.out.println("Encode: " + encode);
            System.out.println("Decode: " + decode);
        }
    }
};