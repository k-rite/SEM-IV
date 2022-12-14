

import java.sql.*;   
 class JavaApplication1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try{
               Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/student","root","");
            Statement statement=con.createStatement();
             ResultSet resultSet=statement.executeQuery("SELECT * FROM studenttable");
            while(resultSet.next())
             {
                System.out.println("NAME :"+resultSet.getString(1));
                System.out.println("Course :"+resultSet.getString(2));
            }
        }
        catch(SQLException ex){
            System.out.println(ex.getMessage());
        }
        // TODO code application logic here
        
        
    }
    
}
