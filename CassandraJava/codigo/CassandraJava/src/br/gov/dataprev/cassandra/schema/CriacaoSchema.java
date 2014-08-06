package br.gov.dataprev.cassandra.schema;

import com.datastax.driver.core.Cluster;
import com.datastax.driver.core.Host;
import com.datastax.driver.core.Metadata;
import com.datastax.driver.core.Session;

/**
 * Classe respons�vel por criar a estrutura do Cassandra para o servi�o de m�sicas
 * 
 * @author jose.mvieira
 *
 */
public class CriacaoSchema {

	private Cluster cluster; //representa��o do cluster de m�quinas Cassandra
	private Session sessao; //representa��o da sess�o de persist�ncia do Cassandra atrav�s da linguagem CQL

	
	public CriacaoSchema() {		
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
	 * Cria o keyspace para o servi�o de m�sica
	 */
	public void createKeyspace(){
		sessao = cluster.connect(); //conecta ao cluster obtendo uma sess�o de persist�ncia
		
		//elimina o banco de dados anterior
		sessao.execute("DROP KEYSPACE IF EXISTS song_service;");
		
		//executa o comando CQL para a cria��o do keyspace
		sessao.execute("CREATE KEYSPACE IF NOT EXISTS song_service " +
				"WITH REPLICATION = {'class':'SimpleStrategy','replication_factor':1};"); 
	}
	
	/**
	 * Cria as fam�lias de colunas songs e playlists
	 */
	public void createColumnFamilies(){
		sessao = cluster.connect();
		
		//escolhe o keyspace criado para executar scripts
		sessao.execute("use song_service");
		
		//executa o CQL de cria��o da fam�lia de coluna songs
		sessao.execute("CREATE TABLE IF NOT EXISTS song_service.songs(id uuid PRIMARY KEY," +
				"title text," +
				"album text," +
				"artist text," +
				"data blob);");
		
		//executa o CQL de cria��o da fam�lia de coluna playlists
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
