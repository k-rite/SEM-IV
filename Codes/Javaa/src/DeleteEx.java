import java.sql.*;
class Delete {
    public static void main(String[] args) {
        
    {
    try{
        String val="Anand";
        Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/student","root","");

        PreparedStatement ps = con.prepareStatement("DELETE FROM studenttable WHERE student_name = ?");
        ps.setString(1,"Anand");
        int rea=ps.executeUpdate();

        System.out.println("Number of records affected : " + rea);
    }
    catch (SQLException ex) {System.out.println(ex.getMessage());}
}
}
}
