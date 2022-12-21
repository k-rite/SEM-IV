import java.sql.*,
class update {
    public static void main(String[] args) {
        try(
            Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/student","root","");
            Statement statement = con.createStatement();
            ResultSet resultSet=statement.executeQuery("Select * from studenttable");
            
        )
    }
    
}
