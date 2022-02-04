package hello.hellospring;

import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;
import hello.hellospring.service.MemberService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SpringConfig {

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
        return new MemoryMemberRepository();
    }
}


/**
 * @ DI에는 필드, 생성자, Setter 주입 3 가지가 있다.
 *      필드 주입은 잘 안 씀
 *      Setter 주입은 public을 써야하지만 외부 유출이 될 수 있음
 *      생성자 주입을 가장 많이 씀
 */



