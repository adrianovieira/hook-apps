package br.gov.dataprev.cassandra.schema;

import java.util.UUID;

import com.datastax.driver.core.BoundStatement;
import com.datastax.driver.core.Cluster;
import com.datastax.driver.core.Host;
import com.datastax.driver.core.Metadata;
import com.datastax.driver.core.PreparedStatement;
import com.datastax.driver.core.Session;
import com.datastax.driver.core.utils.UUIDs;

public class SongDAO {

	private Cluster cluster; //representa��o do cluster de m�quinas Cassandra
	private Session sessao; //representa��o da sess�o de persist�ncia do Cassandra atrav�s da linguagem CQL
	
	public SongDAO() {
		this.connect("127.0.0.1"); //adiciona a m�quina local ao cluster e inicializa o cluster
	}
	
	/**
	 * Adiciona um n� ao cluster e inicializa o cluster
	 * 
	 * @param node - O endere�o IP do n� que deseja acessar
	 */
	private void connect(String node){

		//Adiciona o n� ao cluster e inicializa/monta o cluster
		cluster = Cluster.builder()
				.addContactPoint(node)
				.build();

		Metadata metadata = cluster.getMetadata(); //obt�m informa��o a respeito do cluster

		System.out.printf("Connectado ao cluster: %s\n", 
				metadata.getClusterName()); //imprime o nome do cluster de m�quinas configurado

		//Imprime informa��es sobre todos os n�s do cluster
		for ( Host host : metadata.getAllHosts() ) {
			System.out.printf("Datacenter: %s; Host: %s; Rack: %s\n",
					host.getDatacenter(), host.getAddress(), host.getRack());
		}
	}
	
	/**
	 * Salva a m�sica no banco de dados Cassandra.
	 * 
	 * @param title - titulo da musica
	 * @param album - album da musica
	 * @param artist - o artista que fez a m�sica
	 */
	public void saveSong(UUID song_id, String title, String album, String artist){
		
		sessao = cluster.connect();
		
		sessao.execute("use song_service");
		
		//Cria um prepared statement para parametrizar o script
		PreparedStatement preparedStatement = sessao.prepare("INSERT INTO song_service.songs " +
			      "(id, title, album, artist)" +
			      "VALUES (?, ?, ?, ?);");
		
		BoundStatement boundStatement = new BoundStatement(preparedStatement);
		
		//faz o binding dos par�metros ao statement e executa
		sessao.execute(boundStatement.bind(song_id, title, album, artist));		
		
	}
	
	public void close() {
		   cluster.close();
	}

	
}
