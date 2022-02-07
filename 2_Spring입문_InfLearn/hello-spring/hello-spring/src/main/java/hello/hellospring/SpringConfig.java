package hello.hellospring;

import hello.hellospring.repository.JdbcMemberRepository;
import hello.hellospring.repository.JpaMemberRepository;
import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;
import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.persistence.EntityManager;
import javax.sql.DataSource;

@Configuration
public class SpringConfig {

//    private DataSource dataSource;

    private EntityManager em;

    @Autowired
    public SpringConfig(EntityManager em) {
        this.em = em;
    }

    @Autowired
    public SpringConfig(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @Bean
    public MemberService memberService()
    {
        return new MemberService(memberRepository());
    }



    /**
     * DB를 변경할 경우, return new DBMemberRepository();로 변경하면 된다.
     */
    @Bean
    public MemberRepository memberRepository()
    {
//        return new MemoryMemberRepository();
//        return new JdbcMemberRepository(dataSource);
        return new JpaMemberRepository(em);
    }
}


/**
 * @ DI에는 필드, 생성자, Setter 주입 3 가지가 있다.
 *      필드 주입은 잘 안 씀
 *      Setter 주입은 public을 써야하지만 외부 유출이 될 수 있음
 *      생성자 주입을 가장 많이 씀
 */



