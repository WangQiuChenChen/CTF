import java.util.Base64;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.lang.Exception;

class base64tofile {
    public static void main(String[] args) throws Exception {
        if (args.length == 2) {
            File file = new File(args[0]);
            FileInputStream in = new FileInputStream(file);
            byte[] buffer = new byte[(int) file.length()];
            in.read(buffer);
            in.close();
            decode(buffer, args[1]);
        }
    }

    public static void decode(byte[] base64Code, String targetPath) throws Exception {
        final Base64.Decoder decoder = Base64.getDecoder();
        byte[] buffer = decoder.decode(base64Code);
        FileOutputStream out = new FileOutputStream(targetPath);
        out.write(buffer);
        out.close();
    }
};