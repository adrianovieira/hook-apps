package br.gov.dataprev.cassandra.teste;

import java.util.UUID;

import br.gov.dataprev.cassandra.schema.CriacaoSchema;
import br.gov.dataprev.cassandra.schema.SongDAO;

public class Main {
	
	public static void main(String[] args) {
		   CriacaoSchema cs = new CriacaoSchema();
		   cs.createKeyspace();	
		   cs.createColumnFamilies();
		   
		   SongDAO dao = new SongDAO();
		   UUID song_id = UUID.randomUUID();
		   dao.saveSong(song_id,"Beijinho no Ombro", "Qualquer Coisa", "Valesca Popozuda");	   
		   
		   cs.close();
	}
}
