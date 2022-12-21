/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
import java.sql.*;
/**
 *
 * @author krite
 */
 class insert {
    public static void main(String Args[])
    {
        try{
            String n="Anand";
            String c="BCA hons";
            Connection con= DriverManager.getConnection("jdbc:mysql://localhost:3306/student","root","");
            
            String str = "insert into studenttable values (?,?)";
            PreparedStatement ps = con.prepareStatement(str);
            ps.setString(1,n);
            ps.setString(2,c);
            ps.executeUpdate();
        } catch(SQLException ex){
            System.out.println(ex.getMessage());
        }
    }
}
