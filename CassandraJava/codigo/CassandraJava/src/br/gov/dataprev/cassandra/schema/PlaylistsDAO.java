package br.gov.dataprev.cassandra.schema;

import java.util.UUID;

import com.datastax.driver.core.BoundStatement;
import com.datastax.driver.core.Cluster;
import com.datastax.driver.core.Host;
import com.datastax.driver.core.Metadata;
import com.datastax.driver.core.PreparedStatement;
import com.datastax.driver.core.Session;
import com.datastax.driver.core.utils.UUIDs;

public class PlaylistsDAO {

	private Cluster cluster; //representação do cluster de máquinas Cassandra
	private Session sessao; //representação da sessão de persistência do Cassandra através da linguagem CQL
	
	public PlaylistsDAO() {
		this.connect("127.0.0.1"); //adiciona a máquina local ao cluster e inicializa o cluster
	}
	
	/**
	 * Adiciona um nó ao cluster e inicializa o cluster
	 * 
	 * @param node - O endereço IP do nó que deseja acessar
	 */
	private void connect(String node){

		//Adiciona o nó ao cluster e inicializa/monta o cluster
		cluster = Cluster.builder()
				.addContactPoint(node)
				.build();

		Metadata metadata = cluster.getMetadata(); //obtém informação a respeito do cluster

		System.out.printf("Connectado ao cluster: %s\n", 
				metadata.getClusterName()); //imprime o nome do cluster de máquinas configurado

		//Imprime informações sobre todos os nós do cluster
		for ( Host host : metadata.getAllHosts() ) {
			System.out.printf("Datacenter: %s; Host: %s; Rack: %s\n",
					host.getDatacenter(), host.getAddress(), host.getRack());
		}
	}
	
	/**
	 * Salva a playlist no banco de dados Cassandra.
	 * 
	 * @param title - titulo da musica
	 * @param album - album da musica
	 * @param artist - o artista que fez a música
	 */
	public void savePlaylist(int song_order, UUID song_id, String title, String album, String artist){
		
		sessao = cluster.connect();
		
		UUID id = UUIDs.random();
		
		sessao.execute("use song_service");
		
		//Cria um prepared statement para parametrizar o script
		PreparedStatement preparedStatement = sessao.prepare("INSERT INTO playlists (id, song_order, song_id, title, artist, album) "+  
			      				"VALUES (?, ?, ?, ?, ?, ?);");
		
		BoundStatement boundStatement = new BoundStatement(preparedStatement);
		
		//faz o binding dos parâmetros ao statement e executa
		sessao.execute(boundStatement.bind(id, song_order, song_id,  title, artist, album));		
		
	}
	
	public void close() {
		   cluster.close();
	}

	
}
