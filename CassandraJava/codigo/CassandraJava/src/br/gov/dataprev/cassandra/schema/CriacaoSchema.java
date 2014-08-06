package br.gov.dataprev.cassandra.schema;

import com.datastax.driver.core.Cluster;
import com.datastax.driver.core.Host;
import com.datastax.driver.core.Metadata;
import com.datastax.driver.core.Session;

/**
 * Classe responsável por criar a estrutura do Cassandra para o serviço de músicas
 * 
 * @author jose.mvieira
 *
 */
public class CriacaoSchema {

	private Cluster cluster; //representação do cluster de máquinas Cassandra
	private Session sessao; //representação da sessão de persistência do Cassandra através da linguagem CQL

	
	public CriacaoSchema() {		
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
	 * Cria o keyspace para o serviço de música
	 */
	public void createKeyspace(){
		sessao = cluster.connect(); //conecta ao cluster obtendo uma sessão de persistência
		
		//elimina o banco de dados anterior
		sessao.execute("DROP KEYSPACE IF EXISTS song_service;");
		
		//executa o comando CQL para a criação do keyspace
		sessao.execute("CREATE KEYSPACE IF NOT EXISTS song_service " +
				"WITH REPLICATION = {'class':'SimpleStrategy','replication_factor':1};"); 
	}
	
	/**
	 * Cria as famílias de colunas songs e playlists
	 */
	public void createColumnFamilies(){
		sessao = cluster.connect();
		
		//escolhe o keyspace criado para executar scripts
		sessao.execute("use song_service");
		
		//executa o CQL de criação da família de coluna songs
		sessao.execute("CREATE TABLE IF NOT EXISTS song_service.songs(id uuid PRIMARY KEY," +
				"title text," +
				"album text," +
				"artist text," +
				"data blob);");
		
		//executa o CQL de criação da família de coluna playlists
		sessao.execute("CREATE TABLE IF NOT EXISTS song_service.playlists (id uuid," +
				"song_order int," +
				"song_id uuid," +
				"title text," +
				"album text," +
				"artist text," +
				"PRIMARY KEY  (id, song_order ) );");
		
		sessao.execute("CREATE INDEX ON song_service.playlists(artist);");
	}
	
	public void close() {
		   cluster.close();
	}


}
