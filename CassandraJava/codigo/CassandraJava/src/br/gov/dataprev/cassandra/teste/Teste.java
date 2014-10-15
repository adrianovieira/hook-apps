package br.gov.dataprev.cassandra.teste;

import com.datastax.driver.core.BoundStatement;
import com.datastax.driver.core.Cluster;
import com.datastax.driver.core.Host;
import com.datastax.driver.core.Metadata;
import com.datastax.driver.core.PreparedStatement;
import com.datastax.driver.core.ResultSet;
import com.datastax.driver.core.Row;
import com.datastax.driver.core.Session;

public class Teste {

	private Cluster cluster;
	private Session sessao;
	
	public void connect(String node){
		cluster = Cluster.builder()
		         .addContactPoint(node)
		         .build();
		   Metadata metadata = cluster.getMetadata();
		   
		   System.out.printf("Connectado ao cluster: %s\n", 
		         metadata.getClusterName());
		   
		   for ( Host host : metadata.getAllHosts() ) {
		      System.out.printf("Datacenter: %s; Host: %s; Rack: %s\n",
		         host.getDatacenter(), host.getAddress(), host.getRack());
		   }
	}
	
	public void imprimeListaUsuarios(){
		sessao = cluster.connect();
		
		sessao.execute("use teste1");
		
		ResultSet retorno = sessao.execute("select * from usuarios");
		System.out.println(String.format("%-30s\t%-20s\t%-20s\n%s", "uid", "nome", "senha",
			       "-------------------------------+-----------------------+--------------------"));
		for (Row row : retorno) {
			    System.out.println(String.format("%-30s\t%-20s\t%-20s", row.getInt("uid"),
			    row.getString("nome"),  row.getString("senha")));
		}
		System.out.println();
	}	
	
	public void salvaUsuario(int id, String nome, String senha){
		sessao = cluster.connect();
		
		sessao.execute("use teste1");
		
		PreparedStatement preparedStatement = sessao.prepare("INSERT INTO teste1.usuarios " +
			      "(uid, nome, senha)" +
			      "VALUES (?, ?, ?);");
		
		BoundStatement boundStatement = new BoundStatement(preparedStatement);
		
		sessao.execute(boundStatement.bind(id,nome,senha) );
		
	}
	
	public void close() {
		   cluster.close();
	}
}
